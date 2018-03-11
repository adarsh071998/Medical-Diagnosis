import matplotlib.pyplot as plt

blood = [10, 20, 30, 40, 50, 60, 70] 
cbc = [20, 50, 40, 30, 10, 80, 90]

plt.plot(blood, cbc, 'blue')

plt.title('body checking')
plt.xlabel('blood')
plt.ylabel('cbc')
plt.show()

plt.savefig('line')
