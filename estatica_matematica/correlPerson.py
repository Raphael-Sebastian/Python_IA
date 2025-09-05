import numpy as np

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 5, 4, 5]

# x = np.array([-1, 0, 1])
# y = np.array([-1, 0, 1]) #y = x(correlação -1)

#Agora vamos criar y que não tem correlação linear com x
x = np.array([-1, 0, 1])
y = np.array([1, 0, 1]) # y não e linearmente relacionada com x

corr = np.corrcoef(x,y)[0, 1]
print("Correlação de Pearson:", corr)

