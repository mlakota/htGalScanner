import sys
import os
from os import path as osp

configFile = 'config.ini'
pathOption = 'path'
acceptedExts = ('jpg','png','gif')

class HTScan(object):

	scanned = []
	tree = {}
	recursive = False

	def __init__(self,args):
		self.args = args

	def debug(self):
		print 'ARGS:',self.args
		print 'SCANNED: [',
		for item in self.scanned:
			print "'" + item + "',",
		print ']'

	def getConfig(self):
		lines = open(configFile).readlines()
		for i in lines:
			option = i.split('=')
			if option[0].strip() == pathOption:
				for item in option[1].split(','):
					self.scanned.append(item.strip())

	def scanFolders(self):
		for folder in self.scanned:
			if osp.exists(folder) and osp.isdir(folder):
				print self.scanElement(folder)

	def scanElement(self, folderPath):
		fileList = []
		for i in os.listdir(folderPath):
			tempPath = folderPath+os.sep+i
			if osp.isfile(tempPath) and \
				i.split('.')[1] in acceptedExts:
				fileList.append(i)
			elif self.recursive:
				if osp.isdir(tempPath):
					fileList.append({i : 
						self.scanElement(tempPath)})
		return fileList


def main(*args):
	HT = HTScan(args)
	HT.getConfig()
	HT.scanFolders()
#	HT.debug()

if __name__ == '__main__':
	main(sys.argv[0],'arg1','arg2')
