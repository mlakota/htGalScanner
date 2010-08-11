import sys
import os
from os import path as osp
import ConfigParser

import imgProcessor

configFile = 'config.ini'
cfgBool = {'yes':True, 'no':False}
sectionName = 'global'
pathOption = 'path'
recurseOption = 'recursive'
acceptedExts = ('jpg','png','gif')

class HTScan(object):

	scanned = ''
	oldTree = {}
	tree = {}
	recursive = True

	def __init__(self):
		self.__getConfig()

	def debug(self):
		print 'ARGS:',self.args
		print 'SCANNED:', self.scanned
		print 'RECURSE:', self.recursive

	def __getConfig(self):
		cfg = ConfigParser.RawConfigParser()
		cfg.read(configFile)
		self.scanned = cfg.get(sectionName,pathOption)
		self.recursive = cfgBool[cfg.get(sectionName,recurseOption)]
		print self.scanned,self.recursive

	def __scanFolders(self):
		if osp.exists(self.scanned) and osp.isdir(self.scanned):
			print self.__scanElement(self.scanned)

	def __scanElement(self, folderPath):
		fileList = []
		for i in os.listdir(folderPath):
			tempPath = folderPath+os.sep+i
			if osp.isfile(tempPath) and \
				i.split('.')[1] in acceptedExts:
				fileList.append(i)
			elif self.recursive:
				if osp.isdir(tempPath) and \
					os.listdir(tempPath):
					fileList.append( { i :
						self.__scanElement(tempPath)})
		return fileList

	def run(self):
		self.__scanFolders()


def main():
	HT = HTScan()
	HT.run()
#	HT.debug()

if __name__ == '__main__':
	main()
