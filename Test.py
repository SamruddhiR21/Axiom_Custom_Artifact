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
		return "Test"

	def CreateFragments(self):
		self.AddFragment("Date", Category.DateTime, FragmentType.DateTime)
		self.AddFragment("Sender", Category.DateTime, FragmentType.DateTime)
		self.AddFragment("Message", Category.DateTime, FragmentType.DateTime)

class ReadCSV(Hunter):
	def Register(self, registrar):
		registrar.RegisterFileName("Test.csv")

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

			csv_reader = csv.reader(csv_file, delimiter=",")

			for row in csv_reader:
				if csv_reader.line_num == 1:
					if row[0] != "Date" or row[1] != "Sender" or row[2] != "Message" or len(row) != 3:
						break
					else:
						continue

				foundHit = Hit()
				foundHit.SetLocation("Line Number: " + str(csv_reader.line_num))
				try:
					foundHit.AddValue("Date", datetime.datetime.strptime(row[0],'%d-%m-%y %H:%M'))
				except:
					foundHit.AddValue("Date", datetime.datetime.fromtimestamp(0))
				try:
					foundHit.AddValue("Sender", datetime.datetime.strptime(row[1],'%d-%m-%y %H:%M'))
				except:
					foundHit.AddValue("Sender", datetime.datetime.fromtimestamp(0))
				try:
					foundHit.AddValue("Message", datetime.datetime.strptime(row[2],'%d-%m-%y %H:%M'))
				except:
					foundHit.AddValue("Message", datetime.datetime.fromtimestamp(0))
				self.PublishHit(foundHit)

RegisterArtifact(CSVReader())
