class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        def get_neighbors(i, j):
            neighbors = []
            for d in [[-1,0], [1,0], [0,1], [0,-1], [1,1], [-1,1], [1,-1], [-1,-1]]:
                if ((i+d[0]) < n) and ((i+d[0]) >= 0) and ((j+d[1]) <m) and ((j+d[1]) >=0):
                    neighbor = board[i+d[0]][j+d[1]]
                    neighbors.append(neighbor)
            return neighbors
        
        next_state = []
        for i in range(n):
            for j in range(m):
                neighbors = get_neighbors(i,j)
                if board[i][j] == 1:
                    s = sum(neighbors)
                    if s < 2:
                        t = 0
                    elif (s == 2) or (s == 3):
                        t = 1
                    elif s>3:
                        t = 0
                elif board[i][j] == 0:
                    s = sum(neighbors)
                    if s == 3:
                        t = 1
                    else:
                        t = 0
                next_state.append(t)
        k = 0
        for i in range(n):
            for j in range(m):
                board[i][j] = next_state[k]
                k+=1


                    



            
        