from collections import deque

def DFS(a, b, target):
    m = {}
    isSolvable = False
    path = []
    q = deque()
    
    q.append((0, 0))
    
    while len(q) > 0:
        u = q.popleft()
        if (u[0], u[1]) in m:
            continue
        
        if (u[0] > a or u[1] > b or u[0] < 0 or u[1] < 0):
            continue
        
        path.append([u[0], u[1]])
        m[(u[0], u[1])] = 1
        
        if u[0] == target or u[1] == target:
            isSolvable = True
            
            if u[0] == target and u[1] != 0:
                path.append([u[0], 0])
            elif u[1] == target and u[0] != 0:
                path.append([0, u[1]])
            
            sz = len(path)
            for i in range(sz):
                print("(", path[i][0], ",", path[i][1], ")")
            break
