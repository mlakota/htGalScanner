


class HTScan(object):

	def __init__(self,args):
		self.args = args

	def print(self):
		print self.args

def main(*args):
	print args

if __name__ == '__main__':
	main('arg1','arg2')
