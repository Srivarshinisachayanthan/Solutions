class Graph:
    def __init__(self, edges):
        self.edges = edges 
        self.graph = {}
        for start, end in edges:
            if start in self.graph:
                self.graph[start].append(end)
            else:
                self.graph[start]=[end]
    
    def print_graph(self):
        print(self.graph.values())
        
    def get_paths(self,start, end, path=[]):
        path = path + [start]
        if start==end:
            return [path]
        if start not in self.graph:
            return []
        paths=[]
        for node in self.graph[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)        
        return paths 
            
    
if __name__ == "__main__":
    routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru"),
        ("Chennai", "Hyderabad")
    ]
    
    route_graph=Graph(routes)
    # print(route_graph.print_graph())
    
    
    
    start = "Mumbai"
    end = "New York"
    print(f"start is {start} and end is {end}")

    print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start,end))
