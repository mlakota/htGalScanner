import os
from os import path as osp
import HTMLParser

class HTMLCreator(HTMLParser.HTMLParser):

	def __init__(self):
		pass

	def handle_starttag(self,tag,attrs):
		pass

	def process(self, tree=[]):
		pass

	def set(**args):
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
			elif item == 'div':
				self.divName == args[item]

def main():
	html = HTMLCreator()
	html.destPath = 'E:\Galeria'
	html.destFile = 'galeria.html'
	html.destDiv = 'gallery'

if __name__ == '__main__':
	main()
