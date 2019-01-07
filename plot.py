import matplotlib.pyplot as plt
import numpy as np

a = np.array([0,1,2,0,0.7,0.7,1.3,1.3,2,0,1,2])
b = np.array([0,0,0,1,0.7,1.3,1.3,0.7,2,2,2,2])
c = np.array([0,0,0,0,50,50,50,50,0,10,0,0])

plt.figure('Sketch')
cm = plt.cm.get_cmap('binary')
sc = plt.scatter(a,b,c=c, marker='o', cmap=cm, s=100)
plt.colorbar(sc)
plt.plot([2.3,2.3],[-0.3,2.3], c='orange', label='Morning (20 degrees)', linewidth=5)
plt.plot([-0.3,2.3],[-0.3,-0.3], c='yellow', label='Afternoon (60 degrees)', linewidth=5)
plt.plot([-0.3,-0.3],[-0.3,2.3], c='red', label='Evening (10 degrees)', linewidth=5)
plt.legend(bbox_to_anchor=(1.0, 1.1))
plt.xlim([-1,3])
plt.ylim([-1,3])
plt.show()

### Morning ###
angle = 20
angle_rad = np.deg2rad(angle)

length = c/np.tan(angle_rad)
l_norm = length/100

plt.figure('Morning')
sc = plt.scatter(a,b,c=c, marker='o', cmap=cm, s=100)
plt.colorbar(sc)
plt.plot([2.3,2.3],[-0.3,2.3], c='orange', label='Morning (20 degrees)', linewidth=5)

for i in range(len(l_norm)):
    if l_norm[i] != 0:
        plt.plot([a[i]-l_norm[i],a[i]],[b[i],b[i]], c='grey', linestyle='dashed')

plt.legend(bbox_to_anchor=(1.0, 1.1))
plt.xlim([-1,3])
plt.ylim([-1,3])
plt.show()

### Afternoon ###                                                                 
angle = 40
angle_rad = np.deg2rad(angle)

length = c/np.tan(angle_rad)
l_norm = length/100

plt.figure('Afternoon')
sc = plt.scatter(a,b,c=c, marker='o', cmap=cm, s=100)
plt.plot([-0.3,2.3],[-0.3,-0.3], c='yellow', label='Afternoon (60 degrees)', linewidth=5)
plt.colorbar(sc)

for i in range(len(l_norm)):
    if l_norm[i] != 0:
        plt.plot([a[i],a[i]],[b[i]+l_norm[i],b[i]], c='grey', linestyle='dashed\
')

plt.legend(bbox_to_anchor=(1.0, 1.1))
plt.xlim([-1,3])
plt.ylim([-1,3])
plt.show()

### Evening ###                                                                                                      
angle = 10
angle_rad = np.deg2rad(angle)

length = c/np.tan(angle_rad)
l_norm = length/100

plt.figure('Evening')
sc = plt.scatter(a,b,c=c, marker='o', cmap=cm, s=100)
plt.plot([-0.3,-0.3],[-0.3,2.3], c='red', label='Evening (10 degrees)', linewidth=5)
plt.colorbar(sc)


for i in range(len(l_norm)):
    if l_norm[i] != 0:
        plt.plot([a[i]+l_norm[i],a[i]],[b[i],b[i]], c='grey', linestyle='dashed')

plt.legend(bbox_to_anchor=(1.0, 1.1))
plt.xlim([-1,3])
plt.ylim([-1,3])
plt.show()
