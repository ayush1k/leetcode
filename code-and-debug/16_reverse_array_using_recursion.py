def reverse(arr,left,right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverse(arr, left+1, right-1)
        
arr = [12,12,5,4,21,7,23,65,32,12,6,5]
reverse(arr,1,len(arr)- 1)
print(arr)