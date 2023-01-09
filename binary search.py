def BinarySearch(l1,key):
    low=0
    high=len(l1)-1
    found=False
    while low<=high and not found:
        mid=(low+high)//2
        if key == l1[mid]:
            found=True
        elif key>l1[mid]:
            low = mid+1
        else:
            high = mid-1
    if found == True:
        print("key is found")
    else:
        print("key is not found")
l1=[25,1,4,5,3]
l1.sort()
print(l1)
key=int(input("enter the key:"))
BinarySearch(l1,key)
