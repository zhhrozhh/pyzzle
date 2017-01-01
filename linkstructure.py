import sys
try:
	sys.path.append('C:\\Program Files\\Anaconda3\\lib\\site-packages')
except:
	pass
import networkx as nx
#import matplotlib.pyplot as plt

name2node = {}
G = nx.DiGraph()
def addEdge(A,B):
	G.add_edge(A.bName,B.bName)
def delEdge(A,B):
	G.remove_edge(A.bName,B.bName)
def rename(fname,tname):
	from_edges = G.edges()
	to_edges = []
	for e in from_edges:
		x = tname if e[0] == fname else e[0]
		y = tname if e[1] == fname else e[1]
		to_edges.append((x,y))
	G = nx.DiGraph()
	G.add_edges_from(to_edges)
def getDep(node):
	anc = nx.ancestors(G,node.bName)
	ts = nx.topological_sort(G)
	res = []
	for x in ts:
		if x in anc:
			res.append(x)
	return res
#def showStructure():
#	pos = nx.spring_layout(G)
#	nx.draw(G,pos)
#	nx.draw_networkx_labels(G,pos)
#	plt.show()
class test:
	def __init__(self,x):
		self.bName = x
	def __repr__(self):
		return self.bName
if __name__ == '__main__':
	addEdge(test('A'),test('B'))
	addEdge(test('B'),test('C'))
	addEdge(test('S'),test('A'))
	print(getDep(test('C')))
