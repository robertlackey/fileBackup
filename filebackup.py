'''
Created on September 02, 2018
@author: robertLackey
'''
import os
import datetime
import shutil
from datetime import datetime, timedelta
from os import path

filePath0 = os.path.abspath("<INSERT FILE LOCATION>" ) #ADD THE DIRECTORY OF THE FILE TO BACKUP
fileName0 = "tmp.txt" #INSERT THE FILE NAME THAT YOU WANT TO BACKUP
backupPath = os.path.abspath("<INSERT BACKUP LOCATION>") # ADD THE BACKUP LOCATION

today = datetime.now()
oldFileDate = today - timedelta(days=30)

class fileBackup:

	def __init__(self, filePath, file, backupLocation):
		self.filePath = filePath
		self.file = file
		self.backupLocation = backupLocation

	def main(self):
		try:
			if os.path.isfile(self.backupLocation + "/" + self.file):
				print "print file already exists"
				newFileName = today.strftime("%Y-%m-%d") + "-" + self.file
				shutil.copy(self.filePath + "/" + self.file, os.path.join(self.backupLocation, newFileName))
				#shutil.copy(self.filePath + "/" + self.file, os.path.join(self.backupLocation + "/", self.filePath + "/" + newFileName))
				print "File moved with new name"
			else: #elif not os.path.isfile(self.backupLocation + "/" + self.file):
				print "copying file without new name"
				shutil.copy(self.filePath + "/" + self.file, self.backupLocation)
		except OSError:
			raise
		#getting the date and time the backup file was last modified
		try:
			modifiedTime = int(os.path.getmtime(self.backupLocation + self.file))
		except OSError:
			modifiedTime = 0
		lastModifed = datetime.fromtimestamp(modifiedTime)
		#If the backup file was last modified greater than 30 days ago, delete the file
		if os.path.isfile(self.backupLocation + self.file) and lastModifed > oldFileDate:
			#os.remove(self.backupLocation + self.file)
			print "File removed"
		else:
			errorDescription = "File not old enough or File Doesn't exist"
			print errorDescription

if __name__ == '__main__':
	class0 = fileBackup(filePath0, fileName0, backupPath)
	class0.main()
