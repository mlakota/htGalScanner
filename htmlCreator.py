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
		pass


def main():
	html = HTMLCreator()
	html.destPath = 'E:\Galeria'
	html.destFile = 'galeria.html'
	html.destDiv = 'gallery'

if __name__ == '__main__':
	main()
