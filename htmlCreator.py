import os
from os import path as osp
import HTMLParser

class HTMLCreator(HTMLParser):

	destPath = ""
	destFile = ""
	destDiv = ""
	fileTree = {}


	def __init__(self):
		pass

	def handle_starttag(self,tag,attrs):
		pass

def main():
	html = HTMLCreator()
	html.destPath = 'E:\Galeria'
	html.destFile = 'galeria.html'
	html.destDiv = 'gallery'
	print html.destPath, html.destFile, html.destDiv

if __name__ == '__main__':
	main()
