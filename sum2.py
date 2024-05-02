a=[5,6,5,3,9,7,1,5,15]
t=15
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==t:
            print([i,j])