import sys

configFile = 'config.ini'

class HTScan(object):

	def __init__(self,args):
		self.args = args

	def debug(self):
		print self.args

	def getConfig(self):
		lines = open(configFile).readlines()
		for i in lines:
			option = i.split('=')[0].strip()
			print option

def main(*args):
	HT = HTScan(args)
	HT.debug()
	HT.getConfig()

if __name__ == '__main__':
	main(sys.argv[0],'arg1','arg2')
