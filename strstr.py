class Solution(object):
    def strStr(self, haystack, needle):
        if not haystack:
            return -1

        if needle[0] in haystack:
            print("has a possible match")
            start = haystack.index(needle[0])
            print(start, haystack[start])
            while start < len(haystack):
                print("start is "),
                # print(start, haystack[start])
                # if needle[0] in haystack[start:]:
                #     start = haystack.index(needle[0])
                for j in range(len(needle)):
                    print("j is "),
                    print(j)
                    if start + j >= len(haystack):
                        print("break")
                        break
                    if haystack[start + j] == needle[j]:
                        print("equal")
                        print(start, haystack[start + j])
                        continue
                    if haystack[start + j] != needle[j]:
                        progress = j
                        start = start + progress
                        haystack[:] = haystack[start:]
                        print("not equal"),
                        print(start, haystack[start])
                        break
            if j == len(needle):
                return start
        return -1
#     def Search(String txt)
# {
#     int N = txt.length();
#     int M = pat.length();
#     int skip;
#     for (int i = 0; i < N-M; i += skip)
#     {
#         skip = 0;
#         for (int j = M-1; j >= 0; j--)
#         {
#             if (pat.charAt(j) != txt.charAt(i+j))
#             {
#                 skip = Math.max(1, j - right[txt.charAt(i+j)]);
#                 break;
#             }
#         }
#         if (skip == 0)
#         {
#             return i;
#         }
#     }
#     return N;
# }
    def search(self,txt, pat):
        N = len(txt)
        M = len(pat)
        i = 0
        skip  = 0
        while i < N-M:
            print(N,M,skip)
            skip = 0
            j = M - 1
            while j >= 0:
                if pat[j] == txt[i + j]
                    skip = max(1,j-[:txt[i+j]])
                    break
                j -= 1
            if skip == 0:
                return i
            i += skip
        return N

haystack = "djhfskjdasdsedcas"
needle = "das"
Solution().search(haystack,needle)