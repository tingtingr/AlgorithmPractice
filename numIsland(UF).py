class Solution(object):
    def numIslands(self, grid):
        copy = [list(x) for x in grid]
        row = len(copy)
        col = len(copy[0])
        p = [i for i in range(row*col)]
        count = 0
        def find (i):
            if p[i] != i:
                p[i] = find(p[i])
            return p[i]
        
        def union(i,j):
            rooti = find(i)
            rootj = find(j)
            p[rootj] = rooti

        def expand(i,j,m,p):
            col = len(m[0])
            while 0 < i+ 1 < len(m) and 0 <  j+ 1 < len(m[0]):
                if m[i][j + 1] == '1':
                    print('reached'),
                    print(i,j+1)
                    m[i][j+1] = '-1'
                    union(i*col+j, (i)*col + j + 1)
                    expand(i, j+ 1, m, p)
                elif m[i + 1][j] == '1':
                    print('reached'),
                    print(i+1,j)
                    m[i+1][j] = '-1'
                    union(i*col + j, (i + 1)*col + j)
                    expand(i+1,j, m, p)
                else:

                    break
            
            


        # self.printArrM(p,len(grid[0]))
        for i in range(row):
            for j in range(col):
                if copy[i][j] == '1':
                    copy[i][j] = '-1'
                    count += 1
                    # if p[i*col+j] == i*col+j:
                    print('starting to find island'),
                    print(i,j)
                    expand(i,j,copy,p)
                    print('finished find this island'),
                    print(i,j)
                    self.printMatrix(copy)
                    self.printArrM(p,len(copy[0]))
        return count

    def printMatrix(self, m):
        for i in range(len(m)):
            for j in range(len(m[0])):
                print('%2s' % (m[i][j])),
            print('\b')
        print('\n')
    def printArrM (self, m, width):
        dp = [[j for j in range(width)] for i in range(len(m) / width)]
        
        for i in range(len(m)):
            j =  i / width
            dp[j][i % width] = m[i]
        
        self.printMatrix(dp)



grid = ["11110","11010","11000","00000"]

grid= ["11000","11000","00100","00011"]
[
"11110",
"11010",
"11000",
"00000"]
print(Solution().numIslands(grid))