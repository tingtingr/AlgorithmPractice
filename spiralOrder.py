
class Solution(object):
    def __init__(self, n):
        self.matrix = self.generateMatrix(n)
        
    def printVertical(self):
        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix)):
                print(self.matrix[j][i])
            print("\n")
    
    def spiralOrder(self):
        res = []
        if len(self.matrix) == 0:
            return res
        x1 = y1 = 0
        y2 = len(self.matrix[0]) - 1
        x2 = len(self.matrix) - 1
        print(x1,y1,x2,y2)
        while(x1 <= x2 and y1 <= y2):
            stack = []
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    print(i,j)
                    if i == x1 or i == x2 or j == y1 or j == y2:
                        if i > x1 and j == y1 or i == x2 :
                            print("insert"),
                            print(i,j)
                            stack.insert(0,self.matrix[i][j])
#                            print("%2d" % self.matrix[i][j]),
                        else:
                            print("printing"),
                            print(i,j)
                            res.append(self.matrix[i][j])
                            print(res)
#                            print("%2d" % self.matrix[i][j]),

            for i in range(len(stack)):
                res.append(stack[i])
#            print(lst)
            x1 += 1
            y1 += 1
            y2 -= 1
            x2 -= 1
        print(res)
        return res
        
        
    def printPath(self, x1, y1, x2, y2):
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                print("%2d" % self.matrix[i][j]),
            else:
                print(" "),
            print("\b")
        print("\n")
        lst = []
        
        while(x1 < x2 and y1 < y2):
            stack = []
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    if i == x1 or i == x2 or j == y1 or j == y2:
                        if i > x1 and j == y1 or i == x2 :
                            stack.insert(0,self.matrix[i][j])
                            print("%2d" % self.matrix[i][j]),
                        else:
                            lst.append(self.matrix[i][j])
                            print("%2d" % self.matrix[i][j]),
                    else:
                        print("  "),
                print("\b")
            for i in range(len(stack)):
                lst.append(stack[i])
            print(lst)
            x1 += 1
            y1 += 1
            y2 -= 1
            x2 -= 1
            
    def printMatrix(self,matrix):
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                print("%2d" % matrix[i][j]),
            print("\b")
        
    def printDia1(self):
        row = len(self.matrix)
        col = len(self.matrix[0])
        for i in range(row):
            for j in range(col):
                if i == j:
                    print (self.matrix[i][j]),
                else:
                    print("X"),
            print("\b")
    def printDia2(self):
        row = len(self.matrix)
        col = len(self.matrix[0])
        for i in range(row):
            for j in range(col):
                if i + j == col - 1:
                    print(self.matrix[i][j]),
                else:
                    print(" "),
            print("\b")
    def printDia3(self):
        row = len(self.matrix)
        col = len(self.matrix[0])
        for i in range(row):
            for j in range(col):
                if i + j == col - 1 or i == j:
                    print(self.matrix[i][j]),
                else:
                    print("x"),
            print("\b")
            
    def generateMatrix(self, n):
        res = [[i + 1 for i in range(n)]]
        for i in range(n ):
            res.append([ j + n for j in res[-1]])
        self.printMatrix(res)
        return res
        

#matrix = [[ 1, 2, 3],[ 4, 5, 6 ],[ 7, 8, 9 ]]
#Solution(5).printPath(1,1,4,4)
Solution(3).spiralOrder()
#Solution().printDia2(matrix)
#Solution().printDia3(matrix)