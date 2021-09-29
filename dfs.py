import sys

class Vertex:
	def __init__(self, value):
		self.node_num = value
		self.discovery = 0
		self.finish = 0
		self.pi = None
		self.adj = []

def DFS_check(node_info, global_time):
	for node in node_info:
		if node.discovery == 0:
			DFS(node_info, node, global_time)
	return

def DFS(node_info, selected_node, global_time):
	if(selected_node.discovery == 0):
		global_time += 1
		selected_node.discovery = global_time
	
	for node in selected_node.adj:
		if node.discovery == 0:
			node.pi = selected_node
			DFS(node_info, node, global_time)
	global_time += 1
	selected_node.finish = global_time
	if selected_node.pi == None:
		DFS_check(node_info, global_time)
		for node in node_info:
			print("({0}, {1})".format(node.discovery, node.finish), end = " ")
		sys.exit(0)
	selected_node = selected_node.pi
	DFS(node_info, selected_node, global_time)
	


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

	global_time = 0
	DFS(node_info, node_info[0], global_time)
