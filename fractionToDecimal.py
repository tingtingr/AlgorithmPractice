class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0 or denominator == 0:
            return 0 
        res = "x#"
        hmap = {}
        neg = False
        zc = False
        if numerator < 0 ^ denominator < 0:
            neg = True
        res = self.helper(abs(numerator),abs(denominator),res, hmap, zc)
        print(res)
        if neg:
            return '-' + res[2:]
        else:
            return res[2:]
    def helper(self, numerator,denominator,res,hmap,zc):
        print(res)
        if numerator < denominator:
            if numerator % denominator == 0:
                zc = True
            temp = str(0)
            res += temp
            if res[-len(temp)-1] == '#':
                    res += '.'
            return self.helper(numerator*10, denominator,res,hmap,zc)
        else:
            temp = str(numerator / denominator)
            if (numerator,denominator) not in hmap:
                hmap[(numerator,denominator)] = temp
                
                res += temp
                if res[-len(temp) - 1] == '#':
                    res += '.'
            else:
                print(hmap[(numerator,denominator)])
                repeat = hmap[(numerator,denominator)]
                res = res[:-len(repeat)]
                res += '('
                res += temp
                res += ")"
                return res
            x = numerator / denominator
            r = numerator - (x * denominator)
            # print("temp"),
            # print(temp)
            # print(res)
            # print(res)
            if r == 0:
                zc = True
                return res
            else:
                return self.helper(r * 10, denominator,res,hmap,zc)
            
numerator = -50
denominator = 8
# Solution().helper(numerator,denominator)
print(Solution().fractionToDecimal(numerator,denominator))