class Solution(object):
    def convert(self, s, numRows):
        if numRows  < 2:
            return s
        l = (numRows * 2) - 2
        res = ""
        for i in range(numRows):
            temp = [0]
            d1 = l - 2*i
            d2 = 2*i
            j = i
            # print(j, d1, d2, l)
            # counter = True
            d = d1
            pre = None
            while j <len(s):
                if pre != j:
                    temp.append(s[j])
                if counter:
                    j = j + d1
                if not counter:
                    j = j + d2
                counter = not counter
            print(str(temp))
            res += "".join([str(i) for i in temp[1:]])
        print(res)
        return res

s = "abcdefghijklmno"
# s ="PAYPALISHIRING"
n = 2
Solution().convert(s,n)