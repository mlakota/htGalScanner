


class HTScan(object):

	def __init__(self,args):
		self.args = args

	def debug(self):
		print self.args

def main(*args):
	HT = HTScan(args)
	HT.debug()

if __name__ == '__main__':
	main('arg1','arg2')
