import sys
import os

configFile = 'config.ini'
pathOption = 'path'

class HTScan(object):

	scanned = []

	def __init__(self,args):
		self.args = args

	def debug(self):
		print 'ARGS:',self.args
		print 'SCANNED: [',
		for item in self.scanned:
			print "'" + item + "',",
		print ']'

	def getConfig(self):
		lines = open(configFile).readlines()
		for i in lines:
			option = i.split('=')
			if option[0].strip() == pathOption:
				for item in option[1].split(','):
					self.scanned.append(item.strip())

	def scanFolders(self):
		for folder in self.scanned:
			print folder,
			if os.path.exists(folder) and \
				os.path.isdir(folder):
				print '+'
			else:
				print '-'


def main(*args):
	HT = HTScan(args)
	HT.getConfig()
	HT.scanFolders()
	HT.debug()

if __name__ == '__main__':
	main(sys.argv[0],'arg1','arg2')
