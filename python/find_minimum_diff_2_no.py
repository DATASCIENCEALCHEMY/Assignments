
arr = [5,32,45,4,12,18,25]
# print(arr[5]-arr[4])
# diff = []
# for i in range(len(arr)-1):
#     j=arr[i+1]-arr[i]
#     diff.append(j)
# print(diff)
# print("the minimum difference between the elements is  : ", sorted(diff)[0])

# step 1 : sort the array 
arr = sorted(arr)
print(arr)
diff = []
for i in range(len(arr)-1):
    j = arr[i+1] - arr[i]
    diff.append(j)
print("the minimum difference between the two elements is : ",sorted(diff)[0])