import matplotlib.pyplot as plt

fig= plt.figure(figsize=(16,14))


f=open('GAYA 2016 NOV.txt') 
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

for i in range(2,len(m)-1):
    if i%2==0:
        M.remove(m[i])
M[0]=2
M[1]=6        
X=["CO",'SO2','NO2','O3','PM2.5','BENZENE']
print(M)

plt.pie(M, labels = X, colors=['r','y','g','b','m','dimgrey'],  
        startangle=90, shadow = True, explode = (0, 0, 0, 0,0,0),
        radius = 1.2, autopct = '%1.1f%%')
plt.legend() 
plt.show()
print('                           GAYA 2016 NOV,POLLUTANT CONTRIBUTION')

    
 
    
    
    
    
    
    
    
    