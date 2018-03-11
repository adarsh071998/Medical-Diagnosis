import matplotlib.pyplot as plt
#data ={}
#slices = [10, 20, 30, 40, 50, 60, 70]
#data['lymph']=20
#data['mono']=6
#data['eosin']=3
#data['baso']=0.5
def pie(data):
#create a bar graph
	slices= [data['lymph'],data['mono'],data['eosin'],data['baso']]
	depts = ['LYMPH','Mono','Eosin','Baso']
	cols = ['magenta','cyan','brown','gold']
	plt.pie(slices, labels=depts, colors=cols, startangle=90, explode=(0,0,0,0), shadow=True, autopct='%.1f%%')
	plt.title('WBC differentual count')
	plt.legend()
	#plt.show()
	plt.savefig('/home/pritesh/Desktop/COM/pie')

#pie(data)