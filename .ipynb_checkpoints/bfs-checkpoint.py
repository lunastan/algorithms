import queue

class Vertex:
	def __init__(self, value):
		self.node_num = value
		self.color = 'w'
		self.distance = -1
		self.pi = None
		self.adj = []

def BFS_check(node_info):
	remain_node = []
	for node in node_info:
		if node.color == 'w':
			remain_node.append(node)
	if len(remain_node) != 0:
		BFS(remain_node)
	
def BFS(node_info):
	q = queue.Queue()
	
	starting_node = node_info[0]
	starting_node.color = 'g'
	print(starting_node.node_num, end = ' ')
	starting_node.distance = 0
	q.put(starting_node)
	while q.qsize() != 0:
		selected = q.get()
		for adjacent in selected.adj:
			if adjacent.color == 'w':
				adjacent.color = 'g'
				print(adjacent.node_num, end = ' ')
				adjacent.distance = selected.distance + 1
				adjacent.pi = selected
				q.put(adjacent)
		selected.color = 'b'
	BFS_check(node_info)
	


if __name__ == "__main__":
	user_input_n_v_n_e = input().split()
	n_vertex = int(user_input_n_v_n_e[0]) # numbers of vertices
	n_edge = int(user_input_n_v_n_e[1]) # numbers of directed edges
	node_info = []
	
	for idx in range(n_vertex):
		node_info.append(Vertex(idx))
		
	for i in range(n_edge):
		user_input_edge = input().split()
		s_point = int(user_input_edge[0])
		e_point = int(user_input_edge[1])
		node_info[s_point].adj.append(node_info[e_point])

	BFS(node_info)
	
