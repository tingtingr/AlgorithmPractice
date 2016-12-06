class Solution(object):
#    def heapSort(self, arr):

#        def swap(arr, j, i):
#            temp = arr[i]
#            arr[i] = arr[j]
#            arr[j] = temp

#        def heapify(arr, size):
#            p = size / 2 - 1
#            while p >= 0:
#                siftdown(arr, p, size)
#                p -= 1
                
#        def siftdown(arr, i, heapsize):
#            print("i is {0}".format(i))
#            i_left = 2 * i + 1
#            i_right = 2 * i + 1
#            largest = i
#            if i_left <= heapsize - 1 and arr[i_left] > arr[i]:
#                largest = i_left
#            else:
#                largest = i
#            if i_right <= heapsize - 1 and arr[largest] < arr[i_right]:
#                    largest = i_right
#            if largest != i:
#                swap(arr, i, largest)
#                siftdown(arr, largest, heapsize)

#        heapsize = len(arr)
#        heapify(arr, heapsize)
#        end = heapsize - 1
#        while end > 0:
#            swap(arr, 0, end)
#            siftdown(arr, 0, heapsize)
#            end -= 1
    def heapsort(self,a):  
      
        def swap(a,i,j):  
            tmp = a[i]  
            a[i] = a[j]  
            a[j] = tmp    
              
        def siftdown(a, i, size):  
            l = 2*i+1  
            r = 2*i+2  
            largest = i  
            if l <= size-1 and a[l] > a[i]:  
                largest = l  
            if r <= size-1 and a[r] > a[largest]:  
                largest = r  
            if largest != i:  
                swap(a, i, largest)  
                siftdown(a, largest, size)  
                  
        def heapify(a, size):  
            p = (size/2)-1  
            while p>=0:  
                siftdown(a, p, size)  
                p -= 1  
                  
        size = len(a)          
        heapify(a, size)  
        end = size-1  
        while(end > 0):  
            swap(a, 0, end)  
            siftdown(a, 0, end)  
            end -= 1  

arr = [3,2,1]

Solution().heapsort(arr)

for i in range(len(arr)):
    print(arr[i])