class Solution(object):
    def strStr(self, haystack,needle):
        g = {}
        for i in range(len(needle) - 1):
            g[needle[i]] = len(needle) - i - 1
        print g 
        i = 0
        while  i <= len(haystack) - len(needle):
            j = len(needle) - 1
            step = 0
            while haystack[i + j] == needle[j]:
                print('same %s %s' % (haystack[i + j], needle[j]))
                if j == 0:
                    return i
                j -= 1
            print('not the same  %s %s' % (haystack[i + j], needle[j]))
            if haystack[i+len(needle) - 1] in g:
                print('the one to look up move is %s' % (haystack[i+len(needle) - 1]))
                step = g[haystack[i+len(needle) - 1]]
            else:
                print('the one to look up move is %s' % (haystack[i+len(needle) - 1]))
                step = len(needle)
            print('step %s' % (step))
            i += step
        return -1

haystack = 'we hold these truth to be self-evident'
needle = 'truth'
# haystack ="aaaaaa"
# needle ="aaaaaa"
# haystack = "ababbbbaaabbbaaa"
# needle =   "bbbb"
print(haystack)
print(needle)
print(Solution().strStr(haystack,needle))

#     T = g
#     i = 0
#     while  i >= len(haystack) - len(needle):
#         j = len(needle) - 1
#         while haystack[i + j] = needle[j]:
#             if j = 0:
#                 return i
#             j -= 1
#         i += g[haystack[i+len(needle) - 1]]
#     return -1