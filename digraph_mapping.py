

def main(digraph):
    #Define the mapping array at negative one this allows us to keep track of the colors and if the node has been visited at the same time.
    k = int(input("What is k-value? "))
    map = [-1 for i in range(len(digraph)+1)]
    map[1] = 0
    queue=[1]
    BFS(digraph,map,k,queue)
    #This will print only in the case BFS fully returns which only happens when the digraph can be mapped to C_k.
    print(f"The digraph can be mapped to a directed cycle of length {k}.")
    print("The mapping is:")
    print(map[1:])


def BFS(digraph,mapping,k,queue):

    #Set up our BFS queue
    while queue:
        u = queue.pop(0)

        #Checking for out vertices
        for v in digraph[u]:
            #Check if v has been visited
            if mapping[v] != -1:
                if (mapping[v] - 1)%k == mapping[u]%k:
                    continue
                else:
                    print(f"The digraph can not be mapped to a directed cycle of length {k}.")
                    print(f"Edge {u}->{v} failed, Vertice {u} is {mapping[u]} while Vertice {v} is {mapping[v]}.")
                    exit() 
            else:
                #Since its an out neighbor, v will be one more than u
                mapping[v] = (mapping[u] + 1)%k
                queue.append(v) 
 
        #Checking for in vertices
        for v in range(1,len(digraph)+1):
            if u in digraph[v]:
                #Check if v has been visited
                if mapping[v] != -1:
                    if (mapping[v] + 1 )%k == mapping[u]%k:
                        continue
                    else:
                        print(f"The digraph can not be mapped to a directed cycle of length {k}.")
                        print(f"Edge {v}->{u} failed, Vertice {v} is {mapping[v]} while Vertice {u} is {mapping[u]}.")
                        exit() 
                else:
                    #Since its an in neighbor, v will be one less than u
                    mapping[v] = (mapping[u] - 1)%k
                    queue.append(v)


if __name__ == "__main__":

    #Works with 2 and 4
    digraph1 = {
        1 :[2,3,5],
        2 :[4,6],
        3 :[7],
        4 :[8], 
        5 :[6,7],
        6 :[8],
        7 :[8],
        8 :[1]
        }
    
    #Works with 3
    digraph2 = {
        1 :[2,3],
        2 :[4],
        3 :[4],
        4 :[1],
        5 :[1] 
        }
    
    #Works with 5
    digraph3 = {
        1 :[2],
        2 :[3],
        3 :[4],
        4 :[5],
        5 :[1] 
        }
    
    
    
    main(digraph1)
    #main(digraph2)
    #main(digraph3)