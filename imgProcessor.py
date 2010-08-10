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

	def process(self):
		for i in self.imgTree:
			self.__processElement(self.srcPath,
				self.destPath, i)
	
	def __processElement(self, source, dest, elem):
		if isinstance(elem,dict):
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
		pass

def main():
	img = IMG()
	img.srcPath = 'E:\Fotki'
	img.destPath = 'E:\Galeria\zdjecia'
	img.imgW = 600
	img.imgH = 600
	img.thumbW = img.thumbH = 100
	img.thumbPrefix="th_"
	img.imgTree = ['Chrysanthemum.jpg', 'Desert.jpg', {'folder2' :
	['Koala.jpg', 'Lighthouse.jpg']}]
	img.process()

if __name__ == '__main__':
	main()
