import numpy as np
import matplotlib.pyplot as plt

a=int(input('xuehao='))
x=np.linspace(0,10,200)
y=pow(x,a)

plt.figure()

plt.plot(x,y,color="red",linewidth=1.0,linestyle="--",label="mi")
plt.xlabel('hengzhou:x')
plt.ylabel('zongzhou:y')
plt.scatter([0],[0],s=30,color="red")
plt.annotate("(0,0)",xy=(0.5,0),fontsize=16)
plt.rcParams['font.sans-serif']=['SimHei']

plt.show()