import os
from os import path as osp
import Image

class IMG(object):

	thumbW, thumbH = 0,0
	imgW, imgH = 0,0
	srcPath = ""
	destPath = ""
	imgTree = []
	thumbPattern = ""


	def __init__(self):
		pass

	def process(self,tree=[]):
		if tree:
			self.imgTree = tree
		for i in self.imgTree:
			self.__processElement(self.srcPath,
				self.destPath, i)
	
	def __processElement(self, source, dest, elem):
		assert(self.__checkNecessaryFields())
		if isinstance(elem,dict):
			if not osp.exists(dest):
				os.mkdir(dest)
			for i in elem.values()[0]:
				self.__processElement(source+os.sep+
					elem.keys()[0], dest+os.sep+
					elem.keys()[0], i)
		else:
			if not osp.exists(dest):
				os.mkdir(dest)
			im = Image.open(source+os.sep+elem)
			im.thumbnail((self.imgW,self.imgH))
			im.save(dest+os.sep+elem)
			im.thumbnail((self.thumbW,self.thumbH))
			im.save(dest+os.sep+self.thumbPrefix+elem)

	def __checkNecessaryFields(self):
		try:
			assert self.srcPath,'src'
			assert self.destPath,'dest'
			assert self.thumbPrefix,'pref'
			assert self.thumbW and self.thumbH,'thumb'
			assert self.thumbW < self.imgW and \
				self.thumbH < self.imgH,'size'
			return True
		except AssertionError,e:
			print "EEEE:",str(e)
			return False

	def set(self,**args):
		for item in args.keys():
			if item == 'source':
				self.srcPath = args[item]
			elif item == 'dest':
				self.destPath = args[item]
			elif item == 'size':
				self.imgW,self.imgH = args[item]
			elif item == 'thumbSize':
				self.thumbW,self.thumbH = args[item]
			elif item == 'prefix':
				self.thumbPrefix = args[item]
