
def main(graph):

    colors = [-1 for i in range(len(graph))]
    current_vertice = 1
    colors[current_vertice-1] = 0
    DFS(graph,current_vertice,colors)
    print("The graph is bipartite")
    print("The coloring is:")
    print(colors)


def DFS(graph,u,colors):
    
    for v in graph[u]:
        if colors[v-1] != -1:
            if colors[v-1] == colors[u-1]:
                print("The graph is not bipartite")
                print(f"Edge {u}{v} failed")
                exit()
            else:
                continue
        else:
            if colors[u-1] == 0:
                colors[v-1] = 1
            else:
                colors[v-1] = 0

            DFS(graph,v,colors)

if __name__ == "__main__":

    graph1 = {
        1 :[2,3,5],
        2 :[1,4,6],
        3 :[1,7],
        4 :[2,8], 
        5 :[1,6,7],
        6 :[2,5,8],
        7 :[3,5],
        8 :[4,6]
        }
    
    graph2 = {
        1 :[2,3,5],
        2 :[1,4,6],
        3 :[1,7],
        4 :[2,8], 
        5 :[1,6,7,8],
        6 :[2,5,8],
        7 :[3,5],
        8 :[4,5,6]
        }
    
    main(graph1)
    #main(graph2)