import matplotlib.pyplot as plt
import json
#['HCT', 'RDW', 'Neu', 'LYMPH', 'Mono', 'Eosin', 'Baso']
x = [10, 20, 30, 40, 50, 60, 70] 
y = [20, 50, 40, 30, 10, 80, 90]
def Graph(data):
#create a bar graph
	x = [data['lymph'],data['mono'],data['eosin'],data['baso']]
	plt.bar(x,y, label='WBC differentual count', color='red')
	plt.xlabel('CBC Parameter')
	plt.ylabel('percentage')
	plt.title('body checking')
	plt.legend()
#display the bar graph
	#plt.show()
	plt.savefig('/home/pritesh/Desktop/COM/graph')