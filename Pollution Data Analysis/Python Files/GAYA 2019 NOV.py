import matplotlib.pyplot as plt

fig= plt.figure(figsize=(16,14))


f=open('GAYA 2019 NOV.txt') 
m=''  
num=[' ','0','1','2','3','4','5','6','7','8','9']  
for p in f:
    for j in p:
        if j in num:            
            m+=j

m=m.split()
M=m[:]

M=m[:]  

for i in range(len(m)-1):
    if i%2==0:
        M.remove(m[i])
 
X=['CO','SO2','NO2',"O3","PM2.5"]


plt.pie(M, labels = X, colors=['r','y','g','b','m'],  
        startangle=90, shadow = True, explode = (0, 0, 0, 0,0), 
        radius = 1.2, autopct = '%1.1f%%') 
plt.legend()
plt.show()
print('                   GAYA 2019 NOV,POLLUTANT CONTRIBUTION')

    
 
    
    
    
    
    
    
    
    