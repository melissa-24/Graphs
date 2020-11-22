"""
Simple graph implementation
"""
from util import Stack, Queue
from collections import defaultdict  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def __repr__(self):
        return str(self.vertices)

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices or v2 not in self.vertices:
            print ("Trying to add edge to node that does not exist")
            return
        self.vertices[v1].add(v2)


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visit = set()
        queue = Queue()
        queue.enqueue(starting_vertex)
        while queue.size() > 0:
            v = queue.dequeue()
            if v not in visit:
                visit.add(v)
                print(v)
                for next_vertex in self.get_neighbors(v):
                    queue.enqueue(next_vertex)



    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visit = set()
        s = Stack()
        s.push(starting_vertex)


        while s.size() > 0:

            # Remove first item from stack
            v = s.pop()

            # If its not visited
            if v not in visit:
                print(v)
                # Mark visited
                visit.add(v)

                for next_vertex in self.get_neighbors(v):
                    s.push(next_vertex)


    def dft_recursive(self, starting_vertex, visit=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visit is None:
            visit = set()
        path = self.get_neighbors(starting_vertex)
        
        visit.add(starting_vertex)
        print(starting_vertex)

        for n in path - visit:
            self.dft_recursive(n, visit)
        return  visit

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue() 
        queue.enqueue([starting_vertex])
        while queue.size() > 0:
            path = queue.dequeue()
            node = path[-1]
            if node == destination_vertex:
                return path
            for adj in self.get_neighbors(node):
                new_path = list(path)
                new_path.append(adj)
                queue.enqueue(new_path)
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        lst = []
        visit = set()
        stack = Stack()
        stack.push(starting_vertex)
        while stack.size() > 0:
            v = stack.pop()
            if v not in visit:
                visit.add(v)
                print (v)
                lst.append(v)
                if v == destination_vertex:
                    return lst
                    break
                for next_vertex in self.get_neighbors(v):
                    stack.push(next_vertex)



    def dfs_recursive(self, starting_vertex, destination_vertex, visit = []):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        print("\n", visit, "<-- Visited Vertexes", "Current Vertex:", starting_vertex)
        if starting_vertex == destination_vertex:
            print ("Vertex Found", starting_vertex)
            return visit + [starting_vertex]
        else:
            visit.append(starting_vertex)
            for edge in self.get_neighbors(starting_vertex):
                print(f'edge: {edge} -- neighbors of {starting_vertex}: {self.get_neighbors(starting_vertex)}')
                if edge not in visit:
                    print(f'{edge} has not been visited, append {starting_vertex} if not in List')
                    path = self.dfs_recursive(edge, destination_vertex, visit)
                    if path is not None:
                        print(path, "PATH")
                        return path
            visit.remove(starting_vertex)
            print(f"Delete Node: {starting_vertex} its edge {edge} has been visited -- There is no path to {destination_vertex}")

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))