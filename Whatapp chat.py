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
		return "WhatsApp Chat"

	def CreateFragments(self):
		self.AddFragment("06/12/2023,", Category.DateTime, FragmentType.DateTime)
		self.AddFragment("18:08", Category.DateTime, FragmentType.DateTime)
		self.AddFragment("-", Category.None, FragmentType.String)
		self.AddFragment("Messages", Category.None, FragmentType.String)
		self.AddFragment("and", Category.None, FragmentType.String)
		self.AddFragment("calls", Category.None, FragmentType.String)
		self.AddFragment("are", Category.None, FragmentType.String)
		self.AddFragment("end-to-end", Category.None, FragmentType.String)
		self.AddFragment("encrypted.", Category.None, FragmentType.String)
		self.AddFragment("No", Category.None, FragmentType.String)
		self.AddFragment("one", Category.None, FragmentType.String)
		self.AddFragment("outside", Category.None, FragmentType.String)
		self.AddFragment("of", Category.None, FragmentType.String)
		self.AddFragment("this", Category.None, FragmentType.String)
		self.AddFragment("chat,", Category.None, FragmentType.String)
		self.AddFragment("not", Category.None, FragmentType.String)
		self.AddFragment("even", Category.None, FragmentType.String)
		self.AddFragment("WhatsApp,", Category.None, FragmentType.String)
		self.AddFragment("can", Category.None, FragmentType.String)
		self.AddFragment("read", Category.None, FragmentType.String)
		self.AddFragment("or", Category.None, FragmentType.String)
		self.AddFragment("listen", Category.None, FragmentType.String)
		self.AddFragment("to", Category.None, FragmentType.String)
		self.AddFragment("them.", Category.None, FragmentType.String)
		self.AddFragment("Tap", Category.None, FragmentType.String)
		self.AddFragment("to (row 26)", Category.None, FragmentType.String)
		self.AddFragment("learn", Category.None, FragmentType.String)
		self.AddFragment("more.", Category.None, FragmentType.String)

class ReadCSV(Hunter):
	def Register(self, registrar):
		registrar.RegisterFileRegex("WhatsApp Chat with Papa - Copy.txt")

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

			csv_reader = csv.reader(csv_file, delimiter=" ")

			for row in csv_reader:
				if csv_reader.line_num == 1:
					if row[0] != "06/12/2023," or row[1] != "18:08" or row[2] != "-" or row[3] != "Messages" or row[4] != "and" or row[5] != "calls" or row[6] != "are" or row[7] != "end-to-end" or row[8] != "encrypted." or row[9] != "No" or row[10] != "one" or row[11] != "outside" or row[12] != "of" or row[13] != "this" or row[14] != "chat," or row[15] != "not" or row[16] != "even" or row[17] != "WhatsApp," or row[18] != "can" or row[19] != "read" or row[20] != "or" or row[21] != "listen" or row[22] != "to" or row[23] != "them." or row[24] != "Tap" or row[25] != "to" or row[26] != "learn" or row[27] != "more." or len(row) != 28:
						break
					else:
						continue

				foundHit = Hit()
				foundHit.SetLocation("Line Number: " + str(csv_reader.line_num))
				try:
					foundHit.AddValue("06/12/2023,", datetime.datetime.strptime(row[0],'%d-%m-%y %H:%M:%S'))
				except:
					foundHit.AddValue("06/12/2023,", datetime.datetime.fromtimestamp(0))
				try:
					foundHit.AddValue("18:08", datetime.datetime.strptime(row[1],'%d-%m-%y %H:%M:%S'))
				except:
					foundHit.AddValue("18:08", datetime.datetime.fromtimestamp(0))
				try:
					foundHit.AddValue("-", row[2])
				except:
					foundHit.AddValue("-", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("Messages", row[3])
				except:
					foundHit.AddValue("Messages", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("and", row[4])
				except:
					foundHit.AddValue("and", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("calls", row[5])
				except:
					foundHit.AddValue("calls", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("are", row[6])
				except:
					foundHit.AddValue("are", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("end-to-end", row[7])
				except:
					foundHit.AddValue("end-to-end", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("encrypted.", row[8])
				except:
					foundHit.AddValue("encrypted.", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("No", row[9])
				except:
					foundHit.AddValue("No", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("one", row[10])
				except:
					foundHit.AddValue("one", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("outside", row[11])
				except:
					foundHit.AddValue("outside", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("of", row[12])
				except:
					foundHit.AddValue("of", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("this", row[13])
				except:
					foundHit.AddValue("this", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("chat,", row[14])
				except:
					foundHit.AddValue("chat,", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("not", row[15])
				except:
					foundHit.AddValue("not", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("even", row[16])
				except:
					foundHit.AddValue("even", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("WhatsApp,", row[17])
				except:
					foundHit.AddValue("WhatsApp,", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("can", row[18])
				except:
					foundHit.AddValue("can", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("read", row[19])
				except:
					foundHit.AddValue("read", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("or", row[20])
				except:
					foundHit.AddValue("or", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("listen", row[21])
				except:
					foundHit.AddValue("listen", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("to", row[22])
				except:
					foundHit.AddValue("to", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("them.", row[23])
				except:
					foundHit.AddValue("them.", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("Tap", row[24])
				except:
					foundHit.AddValue("Tap", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("to (row 26)", row[25])
				except:
					foundHit.AddValue("to (row 26)", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("learn", row[26])
				except:
					foundHit.AddValue("learn", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				try:
					foundHit.AddValue("more.", row[27])
				except:
					foundHit.AddValue("more.", 'Error: {}. {}, script line: {}'.format(sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2].tb_lineno))
				self.PublishHit(foundHit)

RegisterArtifact(CSVReader())
