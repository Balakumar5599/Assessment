array=list(map(int,input("enter array: ").split()))
sum=int(input("enter sum:"))
count = 0
pair_list=[]
for i in range(0,len(array)):
    for j in range(i+1,len(array)):
        if array[i]+array[j] == sum:
            pair_list.append((array[i],array[j]))
            count += 1
print("output:",count)
print(pair_list)