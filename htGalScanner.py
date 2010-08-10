import sys

configFile = 'config.ini'
pathOption = 'path'

class HTScan(object):

	def __init__(self,args):
		self.args = args

	def debug(self):
		print self.args

	def getConfig(self):
		lines = open(configFile).readlines()
		for i in lines:
			option = i.split('=')
			if option[0].strip() == pathOption:
				for item in option[1].split(','):
					print item.strip()

def main(*args):
	HT = HTScan(args)
	HT.debug()
	HT.getConfig()

if __name__ == '__main__':
	main(sys.argv[0],'arg1','arg2')
