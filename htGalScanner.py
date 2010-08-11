import sys
import os
from os import path as osp
import ConfigParser

import imgProcessor


configFile = 'config.ini'
cfgBool = {'yes':True, 'no':False}

sectionName = 'global'
pathOption = 'image_source'
destPathOption = 'image_destination'
recurseOption = 'recursive'

templateOption = 'html_template'
htmlFolderOption = 'html_destination_folder'
htmlFileOption = 'html_destination_filename'

sizeOption = 'image_size'
thumbOption = 'thumbnail_size'
prefixOption = 'thumbnail_prefix'

acceptedExts = ('jpg','png','gif')


class HTScan(object):

	srcPath = ''
	destPath = ''
	recursive = True
	tmplPath = ''
	htmlDir = ''
	htmlFile = ''
	imgSize = ()
	thumbSize = ()
	thumbPrefix = ''
	oldTree = {}
	tree = {}


	def __init__(self):
		self.__getConfig()
		self.imgProcessor = imgProcessor.IMG()
		self.imgProcessor.set(
			source=self.srcPath,
			dest=self.destPath,
			size=self.imgSize,
			thumbSize=self.thumbSize,
			prefix=self.thumbPrefix
		)

	def debug(self):
		print 'RECURSE:', self.recursive
		print 'SRCPATH:', self.srcPath
		print 'DESTPATH:', self.destPath
		print 'IMGSIZE:', self.imgSize
		print 'THUMBSIZE:', self.thumbSize
		print 'PREFIX:', self.thumbPrefix

	def __getConfig(self):
		cfg = ConfigParser.RawConfigParser()
		cfg.read(configFile)

		self.srcPath = cfg.get(sectionName,pathOption)
		self.destPath = cfg.get(sectionName,destPathOption)
		self.recursive = cfgBool[cfg.get(sectionName,recurseOption)]

		self.htmlDir = cfg.get(sectionName,htmlFolderOption)
		self.htmlFile = cfg.get(sectionName,htmlFileOption)

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
			return self.__scanElement(self.srcPath)

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
		while 1:
			self.tree = self.__scanFolders()
			if self.tree != self.oldTree:
				self.imgProcessor.process(self.tree)
				self.oldTree = self.tree


def main():
	HT = HTScan()
	HT.run()

if __name__ == '__main__':
	main()
