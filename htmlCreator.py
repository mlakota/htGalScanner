import os
from os import path as osp
import string

import HTMLParser

class HTMLCreator(HTMLParser.HTMLParser):

	insideDiv = False
	openPosition = ()
	closePosition = ()
	lines = []
	text=""
	imgText = [ r'<img src="' ,r'" alt="', '" />\n' ]
	altText = 'Obrazek'

	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)

	def set(self,**args):
		for item in args.keys():
			if item == 'imgFolder':
				self.imgFolder = args[item]
			elif item == 'templatePath':
				self.templatePath = args[item]
			elif item == 'destDir':
				self.destDir = args[item]
			elif item == 'destFile':
				self.destFile = args[item]
			elif item == 'thumbSize':
				self.thumbW,self.thumbH = args[item]
			elif item == 'prefix':
				self.thumbPrefix = args[item]
			elif item == 'divName':
				self.divName = args[item]

	def process(self, tree=[]):
		if tree:
			self.tree = tree
		self.__findDiv()
		self.__createText()
		self.__insertText()
		self.__save()

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
		self.lines = open(self.templatePath).readlines()
		for eachLine in self.lines:
			self.feed(eachLine)
			if self.closePosition:
				break
		if self.openPosition[0] == self.closePosition[0]:
			self.singleLine = True
		else:
			self.singleLine = False

	def __createText(self):
		for element in self.tree:
			tempPath = string.replace(self.imgFolder,self.destDir+os.sep,'')
			self.text += string.join([self.imgText[0], tempPath, 
				'/', self.thumbPrefix, element, self.imgText[1],
				self.altText, self.imgText[2]],"")

	def __save(self):
		out = open(self.destDir+os.sep+self.destFile,"w")
		for i in self.lines:
			out.write(i)
		out.close()

	def __insertText(self):
		newLines = []
		for eachLine in self.lines[:self.openPosition[0]-1]:
			newLines.append(eachLine)
		if self.singleLine:
			newLines.append(self.lines[
				(self.openPosition[0]-1)][:self.closePosition[1]]+"\n")
		else:
			newLines.append(self.lines[self.openPosition[0]-1])
		newLines.append('\n')
		newLines.append(self.text+'\n')
		newLines.append('\n')
		newLines.append(self.lines[self.openPosition[0]-1][
			:self.openPosition[1]]+'</div>\n')
		for eachLine in self.lines[self.closePosition[0]:]:
			newLines.append(eachLine)
		self.lines = newLines


def main():
	html = HTMLCreator()
	html.set(
		imgFolder = r'E:\htGallery\n destination',
		templatePath = r'E:\htGallery\template.html',
		destDir = 'E:\htGallery',
		destFile = 'galeria.html',
		thumbSize = (100,100),
		prefix = 'th_',
		divName = 'galeria'
		)
	html.process(['Chrysanthemum.jpg','Desert.jpg'])

if __name__ == '__main__':
	main()
