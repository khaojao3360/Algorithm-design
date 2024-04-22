"""
Compettion 2: Connected component algorithm.

Group member
    1. Krong        Krongyuth           6405009 (Submitter)
    2. Nattawat     Trisatheanpisan     6405025
    3. Shothibutr   Tansiri             6405203
    4. Phumioat     kamthong            6405310

Instructions
    •Find connected component in an image.
    •Given an array of integers (any size), find all connected components
    (pixels with the same value as the adjacent pixel).
    •Return list of arrays that separate each component apart in its own array.
    •Make it runs as fast as possible.

    •Submit in MS teams before 23.59 of April 2nd.
    •Speed test in class of April 4th

Module owner: Tonkhao
"""
def find_connected(Graph):

    max_val = max(map(max, G))
    equivalent = {}
    Group_id = {}
    Ans=[]
    Group=[[None]*len(Graph) for i in range(len(Graph[0]))] # เอาไว้เก็บ Group ID
    for i,v in enumerate(Graph):
        visited=[]
        for j,k in enumerate(Graph[i]):
            if Graph[i][j] in Group_id:
                if i == 0:
                    if Graph[i][j-1] == Graph[i][j]:
                        Group_id[Group[i][j-1]].append([i,j])
                        Group[i][j] = Group[i][j-1]
                    else:
                        Group[i][j] = Graph[i][j]+max(max_val,max(Group_id))
                        Group_id[Graph[i][j]+max(max_val,max(Group_id))] = [[i,j]]
                        visited.append(Graph[i][j])
                elif j == 0:
                    if Graph[i-1][j] == Graph[i][j]:
                        Group_id[Group[i-1][j]].append([i,j])
                        Group[i][j] = Group[i-1][j]
                    else:
                        Group[i][j] = Graph[i][j]+max(max_val,max(Group_id))
                        Group_id[Graph[i][j]+max(max_val,max(Group_id))] = [[i,j]]
                        visited.append(Graph[i][j])
                else:
                    if Graph[i][j-1] == Graph[i][j]:
                        Group_id[Group[i][j-1]].append([i,j])
                        Group[i][j] = Group[i][j-1]
                        if Graph[i-1][j] == Graph[i][j] and Group[i][j] not in equivalent:
                            equivalent[Group[i][j]]=Group[i-1][j]
                    elif Graph[i-1][j] == Graph[i][j]:
                        Group_id[Group[i-1][j]].append([i,j])
                        Group[i][j] = Group[i-1][j]
                        if Graph[i][j-1] == Graph[i][j] and Group[i][j] not in equivalent:
                            equivalent[Group[i][j]]=Group[i][j-1]
                    else:
                        Group[i][j] = Graph[i][j]+max(max_val,max(Group_id))
                        Group_id[Graph[i][j]+max(max_val,max(Group_id))] = [[i,j]]
                        visited.append(Graph[i][j])
            else:
                Group_id[Graph[i][j]] = [[i,j]]
                Group[i][j] = Graph[i][j]
                visited.append(Graph[i][j])

    for i in equivalent:
        Group_id[equivalent[i]]+=Group_id[i]
        Group_id.pop(i)

    for i in Group_id:
        Group_Ans=[[None]*len(Graph) for i in range(len(Graph[0]))]
        for j in Group_id[i]:
            Group_Ans[j[0]][j[1]] = Graph[j[0]][j[1]]
        Ans.append(Group_Ans)

    return(Ans)
        


G=[[1,2,2,2,1],
   [1,3,3,2,1],
   [1,1,3,2,1],
   [3,3,3,2,1],
   [3,3,3,1,1]]

x=find_connected(G)
print(x)
for i,v in enumerate(x):
    print('this is ',i)
    print(v)
