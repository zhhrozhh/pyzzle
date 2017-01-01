labelPool = list(range(2000))
pSet = {}
allWindow = []
allName = []
linkObj = None
linkTarget = None
def getLabel():
	global labelPool
	return labelPool.pop(0)
def returnLabel(l):
	global labelPool
	labelPool = [int(l)]+labelPool
def isInt(x):
	try:
		int(x)
		return True
	except:
		return False