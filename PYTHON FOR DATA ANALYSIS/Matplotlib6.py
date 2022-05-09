# EX1
import matplotlib.pyplot as plt 
import numpy as np 
data = np.array(['Mercedis', 'Audi', 'BMW', 'Kai',
                'BMW', 'Mercedis', 'BMW', 'Mercedis','Kai', ])
plt.hist(data,histtype='bar',alpha=1,color='green',bins=5)#hist() function mentioned you number of times
# ['bar','barstacked','step','stepfilled']
plt.show()
# EX2 BARSTACKED
import matplotlib.pyplot as plt 
import numpy as np 
data = np.array(['Mercedis', 'Audi', 'BMW', 'Kai',
                'BMW', 'Mercedis', 'BMW', 'Mercedis','Kai', ])
plt.hist(data,histtype='barstacked',alpha=1,color='green',bins=5)#hist() function mentioned you number of times
# ['bar','barstacked','step','stepfilled']
plt.show()
# EX3 STEP alpha =>Opacity for color
# bins =>explain you how diagram take number of bars
import matplotlib.pyplot as plt 
import numpy as np 
data = np.array(['Mercedis', 'Audi', 'BMW', 'Kai',
                'BMW', 'Mercedis', 'BMW', 'Mercedis','Kai', ])
plt.hist(data,histtype='step',alpha=.5,color='green',bins=5)#hist() function mentioned you number of times
# ['bar','barstacked','step','stepfilled']
plt.show()
# EX4 STEPFILLED
import matplotlib.pyplot as plt 
import numpy as np 
data = np.array(['Mercedis', 'Audi', 'BMW', 'Kai',
                'BMW', 'Mercedis', 'BMW', 'Mercedis','Kai', ])
plt.hist(data,histtype='stepfilled',alpha=1,color='green',bins=5)#hist() function mentioned you number of times
# ['bar','barstacked','step','stepfilled']
plt.show()
# EX5 2D Array
import matplotlib.pyplot as plt 
import numpy as np 
data = np.array([['Mercedis', 'Audi', 'BMW'],['Kai',
                'BMW', 'Mercedis'], ['BMW', 'Mercedis','Kai']])
# you can't add color and browser will give a random value
plt.hist(data,histtype='stepfilled',alpha=.7,color='green',bins=10)#hist() function mentioned you number of times
# ['bar','barstacked','step','stepfilled']
plt.show()