

class HTMLCreator(object):

	destPath = ""
	destFile = ""
	destDiv = ""

	def __init__(self):
		pass


	def findDiv(self):
		pass

def main():
	html = HTMLCreator()
	html.destPath = 'E:\Galeria'
	html.destFile = 'galeria.html'
	html.destDiv = 'gallery'
	print html.destPath, html.destFile, html.destDiv

if __name__ == '__main__':
	main()
