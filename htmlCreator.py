import os
from os import path as osp
import HTMLParser

class HTMLCreator(HTMLParser.HTMLParser):

	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)

	def handle_starttag(self,tag,attrs):
		if tag == 'div':
			print attrs[0]
			if attrs[0][0] == 'id' and attrs[0][1] == self.divName:
				print tag + ' ' + attrs[0][1] + ':',
				line,char = self.getpos()
				print 'line:' + str(line),
				print 'pos:' + str(char)

	def process(self, tree=[]):
		file = open(self.destPath+os.sep+self.file)
		for eachLine in file:
			self.feed(eachLine)

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
			elif item == 'htmlFile':
				self.file = args[item]
			elif item == 'div':
				self.divName == args[item]

def main():
	html = HTMLCreator()
	html.set(
		dest = 'E:\Galeria',
		htmlFile = 'galeria.html',
		divName = 'gallery'
		)
	html.process()

if __name__ == '__main__':
	main()
