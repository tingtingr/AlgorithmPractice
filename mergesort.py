class Solution(object):
    def mergeSort(self, arr):
        if len(arr) < 2:
            print("length < 2, return the array")
            return arr
        mid = len(arr) / 2
        print("mid is {0}".format(mid))
        leftArr = arr[0:mid]
        rightArr = arr[mid:len(arr)]
        leftArr = self.mergeSort(leftArr)
        rightArr = self.mergeSort(rightArr)
        return self.merge(leftArr, rightArr)

    def merge(self, arr1, arr2):
        len1 = len(arr1)
        len2 = len(arr2)
        result = [0 for i in range(len1 + len2)]
        i = 0
        j = 0
        while i != len1 or j != len2:
            if i == len1:
                result[i + j] = arr2[j]
                j += 1
            elif j == len2:
                result[i + j] = arr1[i]
                i += 1
            elif arr1[i] <= arr2[j]:
                result[i + j] = arr1[i]
                i += 1
            else:
                result[i + j] = arr2[j]
                j += 1
        return result

    def printArr(self, arr):
        for i in range(len(arr)):
            print(arr[i]),

arr = [3,5,1,6,1,8,9,1,9,4,7,8]
a = Solution().mergeSort(arr)
Solution().printArr(a)