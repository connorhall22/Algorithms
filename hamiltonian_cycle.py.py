#Note if you want me to explain any parts of the code I would be more then happy to explain how it works

#We can define our strong tournament by using a dictionary where the vertice is the key and the verticies it points to are in a list as its value
graph = {'A': ['C','F'],
         'B': ['A','E'],
         'C': ['B'],
         'D': ['A','B','C','F'],
         'E': ['A','C','D'],
         'F': ['B','C','E']}

#Simplest Strong Tournament
graph2 = {'A': ['B'],
         'B': ['C'],
         'C': ['A']}

#Function does the job of picking a vertice to chose from
def vertice_picker(graph):
    print(f"All Possible Hamiltonian Cycles for Strong Tournament")
    cycle = []
    for i in graph.keys():
        cycle =[i]
        hamiltion_cycle(graph,cycle,i)

#Function runs through all possible edge possibilites given our starting vertice
def hamiltion_cycle(graph,cycle,start):
    for vertice in graph[start]:
        if vertice in cycle:
            continue
        cycle.append(vertice)
        hamiltion_cycle(graph,cycle,vertice)
        #Once all edges have been added to the path must ensure we can get back to where we began to complete the cycle
        if len(cycle) == len(graph) and cycle[0] in graph[cycle[-1]]:
            cycle.append(cycle[0])
            print(cycle)
            cycle.pop(-1)
        cycle.pop(-1)

def main():
    vertice_picker(graph)
    #vertice_picker(graph2)

    
if __name__ == "__main__":
    main()