import matplotlib.pyplot as plt

fig= plt.figure(figsize=(16,14))


f=open('DELHI 2015 NOV.txt') 
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
M=m[:]  
for i in range(len(m)):
    if i%2==1:
        M.remove(m[i])
        
X=['PM10','PM2.5','NO2',"SO2"]        

plt.pie(M, labels = X, colors=['r','y','g','b'],  
        startangle=90, shadow = True, explode = (0, 0, 0, 0), 
        radius = 1.2, autopct = '%1.1f%%') 
plt.legend()
plt.show()
print('                   DELHI 2015 NOV,POLLUTANT CONTRIBUTION')

    
    
    
    
    
    
    
    
    
    
    
    