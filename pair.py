import numpy as np

with open('objects.txt') as f: obj=f.readlines()
with open('colors.txt') as f: col=f.readlines()
obj,col=[[x.strip() for x in dic] for dic in [obj,col]]
m='the '+' '.join([np.random.choice(d) for d in [col,obj]])
print(m)




