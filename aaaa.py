x=int(input())
y=input().split()
flag=False
for i in y:
    if y.count(i)>1:
        print(i,end='')
        flag=True
        break
if flag==False:
    print("unique")
