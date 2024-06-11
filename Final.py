from axiom import *

import csv
import datetime
import sys
import codecs
import time
import io

class CSVReader(Artifact):
	def __init__(self):
		self.AddHunter(ReadCSV())

	def GetName(self):
		return "Output_Final.tsv"

	def CreateFragments(self):
		self.AddFragment("Timestamp", Category.DateTime, FragmentType.DateTime)
		self.AddFragment("Sender", Category.None, FragmentType.String)
		self.AddFragment("Message", Category.None, FragmentType.String)

class ReadCSV(Hunter):
	def Register(self, registrar):
		registrar.RegisterFileName("Output_Final.tsv.txt")

	def Hunt(self, context):
		temp_file_path = context.Searchable.SaveAsTempFile()

		skip_bom = False

		with io.open(temp_file_path, mode="rb") as csv_file:
			bom = csv_file.read(3)

			if bom == codecs.BOM_UTF8:
				skip_bom = True

		with codecs.open(temp_file_path,"rb","utf-8") as csv_file:
			if skip_bom:
				csv_file.seek(len(codecs.BOM_UTF8))

			csv_reader = csv.reader(csv_file, delimiter="\t")

			for row in csv_reader:
				if csv_reader.line_num == 1:
					if row[0] != "Timestamp" or row[1] != "Sender" or row[2] != "Message" or len(row) != 3:
						break
					else:
						continue

				foundHit = Hit()
				foundHit.SetLocation("Line Number: " + str(csv_reader.line_num))
				try:
					foundHit.AddValue("Timestamp", datetime.datetime.strptime(row[0],'%d/%m/%Y, %H:%M'))
				except:
					foundHit.AddValue("Timestamp", datetime.datetime.fromtimestamp(0))
				try:
					foundHit.AddValue("Sender", row[1])
				except:
					foundHit.AddValue("Sender", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("Message", row[2])
				except:
					foundHit.AddValue("Message", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				self.PublishHit(foundHit)

RegisterArtifact(CSVReader())
