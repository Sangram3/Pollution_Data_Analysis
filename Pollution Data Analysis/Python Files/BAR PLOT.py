

import matplotlib.pyplot as plt

fig= plt.figure(figsize=(30,15))


f=open('BAR PLOT.txt')
text=''
lower,upper=['*'],[]
for i in range(97,123):
    lower.append(chr(i))  
for i in range(65,91): 
    upper.append(chr(i)) 
for i in f:
    for x in i:
        if x in lower:
            text+=x
        if x in upper:
            text+=' '
            text+=x        
X=text.split()  
copy=X[:] 
for i in range(5):    
    X.remove(copy[i])
    


f=open('project3.txt') 
m=''  
num=[' ','0','1','2','3','4','5','6','7','8','9']  
for p in f:
    for j in p:
        if j in num:            
            m+=j
        
m=m.split()
M=m[:]
for i in range(2):
    m.remove(M[i])     

for i in range(len(m)):
    m[i]=int(m[i])

PM2=m[::2]
PM10=m[1::2] 

India=[]
IPM2=[]
IPM10=[]
sX=X[:]
for i in range(len(X)):
    if "*" in sX[i]:
        India.append(sX[i])
        X.remove(sX[i])
for i in range(len(India)):
    IPM2.append(PM2[i])
    IPM10.append(PM10[i])

for i in range(len(India)):
    PM2.remove(PM2[i])
    PM10.remove(PM10[i])
 

plt.bar(X , PM10,tick_label=X,label='Guido',color='blue')
plt.bar(India , IPM10,tick_label=India,label='Guido',color='red')
plt.xlabel('Cities')
plt.ylabel('PM10(microgm/metercube)')
plt.title("World's Most Polluted Cities")

plt.show()
print('                                    COMPARISON BETWEEN INDIAN CITIES AND THE OTHER')
 
