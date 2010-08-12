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
	imgText = '''
		<a href="%s" rel="lightbox[%s]">
		<img src="%s" alt="%s" />
		</a>\n'''
	dirText = '''
		<a href="%s">
		<img src="%s" alt="%s" />
		</a>\n'''
	relText = 'Galeria1'
	altText = 'Obrazek'
	returnText = '<div id="return"><a href="%s">Return</a></div>'

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
		self.__processLevel(self.tree, self.imgFolder, self.destFile,"")

	def __processLevel(self, tree, directory, fileName,parentName):
		fileText = ""
		index = 0
		for element in tree:
			if isinstance(element, dict):
				childDir = string.join([directory,os.sep,element.keys()[0]],"")
				childFile = string.join(fileName.split('.'),
					string.join(['_',str(index),'.'],""))
				self.__processLevel(element.values()[0], childDir, childFile,
					fileName)
				fileText += self.dirText % (childFile, "", element.keys()[0])
				index += 1
			else:
				fileText += self.imgText % (
					string.join([directory,'/',element],""),
					self.relText,
					string.join([directory,'/',self.thumbPrefix,element],""),
					self.altText
				)
		if parentName:
			fileText += self.returnText % parentName
		content = self.__insertText(fileText)
		self.__save(self.destDir+os.sep+fileName, content)

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
			self.text += self.imgtext % (
				string.join([self.imgfolder,'/',element],""),
				self.reltext,
				string.join([self.imgfolder,'/',self.thumbprefix,
					element],""),
				self.alttext
			)

	def __save(self, file, content):
		out = open(file,"w")
		for line in content:
			out.write(line)
		out.close()

	def __insertText(self,fileText):
		newLines = []
		for eachLine in self.lines[:self.openPosition[0]-1]:
			newLines.append(eachLine)
		if self.singleLine:
			newLines.append(self.lines[
				(self.openPosition[0]-1)][:self.closePosition[1]]+"\n")
		else:
			newLines.append(self.lines[self.openPosition[0]-1])
		newLines.append('\n')
		newLines.append(fileText+'\n')
		newLines.append('\n')
		newLines.append(self.lines[self.openPosition[0]-1][
			:self.openPosition[1]]+'</div>\n')
		for eachLine in self.lines[self.closePosition[0]:]:
			newLines.append(eachLine)
		return newLines

def main():
	html = HTMLCreator()
	html.set(
		imgFolder = r'n destination',
		templatePath = r'E:\htGallery\template.html',
		destDir = 'E:\htGallery',
		destFile = 'galeria.html',
		thumbSize = (100,100),
		prefix = 'th_',
		divName = 'galeria'
		)
	html.process(['Chrysanthemum.jpg','Desert.jpg',
		{'folder2':['Koala.jpg','Penguins.jpg']} ])

if __name__ == '__main__':
	main()
