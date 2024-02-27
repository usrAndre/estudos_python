import math
import matplotlib.pyplot as plt

math.sqrt(3)

print('\nsomente um teste\n')

def divisao(a, b):
    return a / b


print('fração de a com b: ', divisao(23, 9), '\n\n\n')
    

data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Categorical Plotting')


print('Hello\t'*8)

nome = 'Pedro'
sobrenome = 'Souza'
print('Olá '+nome+' '+sobrenome)