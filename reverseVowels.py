class Solution(object):
    def reverseVowels(self, s):
        start = 0
        end = len(s) - 1
        arr = list(s.lower())
        vowels = ['a','e','i','o','u']
        while start < end:
            if arr[start] in vowels and arr[end] in vowels:
                print(start,end)
                arr[start],arr[end] = arr[end],arr[start]
                start += 1
                end -= 1
            elif arr[start] not in vowels:
                start += 1
            else:
                end -= 1
            
        return "".join(arr)

print(Solution().reverseVowels("leetcode"))
print(Solution().reverseVowels("hello"))