# implemented Greedy Algorithm to find minimum number of coins

denom=[1,2,5,10,20,50,100,200,500]
denom.reverse()
amt=117
out=[]
n=len(denom)
i=0
while(i<n):
    while(amt>=denom[i]):
        amt-=denom[i]
        out.append(denom[i])
    i+=1
for i in range(len(out)):
    print(out[i])

