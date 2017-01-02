import sys
sys.path.append('C:\\Program Files\\Anaconda3\\lib\\site-packages')
import matplotlib.pyplot as plt
import networkx as nx
name2node = {}
G = nx.DiGraph()
def addNode(A):
	G.add_node(A.bName)
	name2node[A.bName] = A
def delNode(A):
	G.remove_node(A.bName)
	name2node.pop(A.bName)
def addEdge(A,B):
	if not A.bName in name2node:
		name2node[A.bName] = A
	if not B.bName in name2node:
		name2node[B.bName] = B
	G.add_edge(A.bName,B.bName)
	if not nx.is_directed_acyclic_graph(G):
		G.remove_edge(A.bName,B.bName)
		raise Exception('cyclic link')
def delEdge(A,B):
	G.remove_edge(A.bName,B.bName)
def nodeRename(fname,tname):
	if tname in name2node:
		raise Exception('Dup name')
	from_edges = G.edges()
	to_edges = []
	for e in from_edges:
		x = tname if e[0] == fname else e[0]
		y = tname if e[1] == fname else e[1]
		to_edges.append((x,y))
	from_nodes = G.nodes()
	to_nodes = []
	for n in from_nodes:
		if n == fname:
			to_nodes.append(tname)
		else:
			to_nodes.append(n)
	G.clear()
	name2node[tname] = name2node[fname]
	name2node.pop(fname)
	G.add_edges_from(to_edges)
	G.add_nodes_from(to_nodes)
def getDep(node):
	anc = nx.ancestors(G,node.bName)
	ts = nx.topological_sort(G)
	res = []
	for x in ts:
		if x in anc:
			res.append(x)
	res = [name2node[x] for x in res]
	return res
def getGraph():
	plt.clf()
	pos = nx.spring_layout(G,scale = 0.3)
	nx.draw(G,pos,arrows = True,with_labels = True,font_size = 20)
	#nx.draw_networkx_nodes(G,pos)
	#nx.draw_networkx_edges(G,pos)
	#nx.draw_networkx_labels(G,pos)

	plt.axis('off')
	plt.grid(True)
	plt.savefig('currentStructure.png')
	return ''
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
