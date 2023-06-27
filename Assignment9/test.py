x=[2,3,4,5]
y=[1,2,3,4]
z=[]
for i in range(4):
    z.append(x[i]-y[i])
z.remove(1)
print(z)