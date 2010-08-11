import sys
import os
from os import path as osp
import ConfigParser

configFile = 'config.ini'
cfgBool = {'yes':True, 'no':False}
sectionName = 'global'
pathOption = 'path'
recurseOption = 'recursive'
acceptedExts = ('jpg','png','gif')

class HTScan(object):

	scanned = ''
	tree = {}
	recursive = True

	def __init__(self,args):
		self.args = args

	def debug(self):
		print 'ARGS:',self.args
		print 'SCANNED:', self.scanned
		print 'RECURSE:', self.recursive

	def getConfig(self):
		cfg = ConfigParser.RawConfigParser()
		cfg.read(configFile)
		self.scanned = cfg.get(sectionName,pathOption)
		self.recursive = cfgBool[cfg.get(sectionName,recurseOption)]
		print self.scanned,self.recursive

	def scanFolders(self):
		if osp.exists(self.scanned) and osp.isdir(self.scanned):
			print self.scanElement(self.scanned)

	def scanElement(self, folderPath):
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
						self.scanElement(tempPath)})
		return fileList


def main(*args):
	HT = HTScan(args)
	HT.getConfig()
	HT.scanFolders()
#	HT.debug()

if __name__ == '__main__':
	main(sys.argv[0],'arg1','arg2')
