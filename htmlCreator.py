import os
from os import path as osp
import HTMLParser

class HTMLCreator(HTMLParser.HTMLParser):

	insideDiv = False
	openPosition = ()
	closePosition = ()

	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)

	def handle_starttag(self,tag,attrs):
		if tag == 'div':
			if attrs[0][0] == 'id' and attrs[0][1] == self.divName:
				self.openPosition = self.getpos()
				self.insideDiv = True

	def handle_endtag(self,tag):
		if tag == 'div' and self.insideDiv == True:
			self.closePosition = self.getpos()
			self.insideDiv = False

	def __findDiv(self):
		file = open(self.file)
		for eachLine in file:
			self.feed(eachLine)
			if self.closePosition:
				break
		if self.openPosition[0] == self.closePosition[0]:
			self.singleLine = True
		else:
			self.singleLine = False
		print "single line:",self.singleLine

	def process(self, tree=[]):
		self.__findDiv()

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
			elif item == 'htmlFile':
				self.file = args[item]
			elif item == 'divName':
				self.divName = args[item]

def main():
	html = HTMLCreator()
	html.set(
		dest = 'E:\Galeria\zdjecia',
		divName = 'galeria',
		htmlFile = 'E:\Galeria\galeria.html'
		)
	html.process()

if __name__ == '__main__':
	main()
