class Solution(object):
    def wordPattern(self, pattern, str):
        arr = str.split()
        print(arr)
        if len(set(arr)) != len(set(pattern)) or len(arr) != len(pattern):
            return False
        dic ={}
        for i in range(len(pattern)):
            k = pattern[i]
            if k not in dic:
                print("not in dic"),
                print(k)
                dic[k] = arr[i]
                print(dic)
            else:
                print("not in dic,"),
                v = dic[k]
                print(k, v)
                if arr[i] != v:
                    return False
                print(dic)
        return True

pattern= "abba"
str = "dog dog dog dog"

pattern="abba"
str = "dog cat cat dog"
print(Solution().wordPattern(pattern,str))
