a=[2,5,-5,14,8,9,-11]
b=2
subarray=[]
for i in range(0,len(a),b):
    if i+b<=len(a):
        subarray.append(a[i:i+b])
x,y=max(((sum(sub),sub) for sub in subarray),key=lambda x:x[0])
print(x,y)