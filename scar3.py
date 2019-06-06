list = []
n=int(input())
for i in range(n):
    num=int(input())
    list.append(num)
j=len(list)//2
list.sort()
print(list[j])
    
