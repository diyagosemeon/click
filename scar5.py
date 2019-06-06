list= []
number=int(input())
for i in range(number):
    numb=int(input())
    list.append(numb)
list.sort()
print(*list)
