class Solution(object):
    def isValidSudoku(self, m):
        rowmap,colmap,boxmap = {},{},{}
        for i in range(9):
            rowmap[i] = set()
            colmap[i] = set()
            boxmap[i] = set()
        
        def inrow(i,val):
            return val in rowmap[i]
        def incol(i,val):
            return val in colmap[i]
        def inbox((i,j),val):
            return val in boxmap[i / 3 * 3 + j / 3] 

        def printm(m):
            for i in range(len(m)):
                for j in range(len(m[0])):
                    print(m[i][j]),
                print('\b')
            print('\n')
        printm(m)

        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] != '.':
                    val = m[i][j]
                    if inrow(i,val) or incol(j,val) or inbox((i,j),val):
                        return False
                    else:
                        rowmap[i].add(val)
                        colmap[j].add(val)
                        boxmap[i/3 * 3 + j / 3].add(val)
        return True


m = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
print(Solution().isValidSudoku(m))