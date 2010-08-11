import sys
import os
from os import path as osp
import ConfigParser

import imgProcessor

configFile = 'config.ini'
cfgBool = {'yes':True, 'no':False}
sectionName = 'global'
pathOption = 'path'
destPathOption = 'destPath'
recurseOption = 'recursive'
sizeOption = 'destMaxSize'
thumbOption = 'thumbMaxSize'
prefixOption = 'thumbPrefix'
acceptedExts = ('jpg','png','gif')

class HTScan(object):

	srcPath = ''
	oldTree = {}
	tree = {}
	recursive = True

	def __init__(self):
		self.__getConfig()
		self.imgProcessor = imgProcessor.IMG()

	def debug(self):
		print 'ARGS:',self.args
		print 'SRCPATH:', self.srcPath
		print 'RECURSE:', self.recursive

	def __getConfig(self):
		cfg = ConfigParser.RawConfigParser()
		cfg.read(configFile)
		self.srcPath = cfg.get(sectionName,pathOption)
		self.recursive = cfgBool[cfg.get(sectionName,recurseOption)]
		self.destPath = cfg.get(sectionName,destPathOption)
		tempList = (cfg.get(sectionName,sizeOption).split(','))
		for i,item in enumerate(tempList):
			tempList[i] = int(item.strip())
		self.imgSize = tuple(tempList)
		tempList = (cfg.get(sectionName,thumbOption).split(','))
		for i,item in enumerate(tempList):
			tempList[i] = int(item.strip())
		self.thumbSize = tuple(tempList)
		self.thumbPrefix = cfg.get(sectionName,prefixOption)

	def __scanFolders(self):
		if osp.exists(self.srcPath) and osp.isdir(self.srcPath):
			print self.__scanElement(self.srcPath)

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
#		while 1:
			self.tree = self.__scanFolders()
			if self.tree != self.oldTree:
				self.imgProcessor.process(self.tree)


def main():
	HT = HTScan()
	HT.run()

if __name__ == '__main__':
	main()
