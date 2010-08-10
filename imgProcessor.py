import os
from os import path as osp
import Image

class IMG(object):

	thumbW, thumbH = 0,0
	imgW, imgH = 0,0
	srcPath = ""
	destPath = ""
	imgTree = []


	def __init__(self):
		pass

	def process(self):
		pass


def main():
	img = IMG()
	img.srcPath = 'E:\Fotki'
	img.destPath = 'E:\Galeria'
	img.imgW = img.imgH = 600
	img.thumbW = img.thumbH = 100
	img.imgTree = ['Chrysantemum.jpg', 'Desert.jpg']
	img.process()

if __name__ == '__main__':
	main()
