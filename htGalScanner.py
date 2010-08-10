import sys


class HTScan(object):

	def __init__(self,args):
		self.args = args

	def debug(self):
		print self.args

	def getConfig(self):
		pass

def main(*args):
	HT = HTScan(args)
	HT.debug()

if __name__ == '__main__':
	main(sys.argv[0],'arg1','arg2')
