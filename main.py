import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3,4])
y = np.array([32,20,48,37,33])
avg = int((np.sum(y)/len(y)))
#avg_arr = np.array([])
""" made obsolete byplt.axhline
avg_arr = np.full((len(y)), avg)
for i in range(0, len(y)):
    np.append(avg_arr, avg)
"""
#print(avg_arr)
#print(avg)
my_xticks = ['24.11.','25.11.','01.12.','02.12.', '08.12.']
#plt.title('The Punctuality of \n F. M. B.')
plt.title('Punctuality')
plt.xticks(x, my_xticks)
plt.xlabel("Datum")
plt.ylabel("Zeit nach Vorlesungsbeginn(in min)")
plt.ylim([0, 60])
"""
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.set_xlabel('Datum')
ax.set_ylabel('Zeit nach Vorlesungsbeginn in min');
"""
#Other form of displaying the data, currently replaced by plt.bar
#plt.plot(x, y, linestyle=':', label='Verspätung')
#plt.scatter(x,y)

#average currently replaced by plt.axhline
#plt.plot(x, avg_arr, color='r', label='Durchschnitt')
plt.axhline(y=avg, color='r', linestyle='-', label='Durchschnitt')
plt.bar(x, y, width=0.8, bottom=None, align='center', label='Verspätung')
#currently broken attempt to display average over tardiness of every day
#plt.bar(x, avg_arr, width=0.8, bottom=None, align='center', color='r', label='Durchschnitt')
plt.title('Pünktlichkeit')
plt.legend()
plt.xlabel("Datum")
plt.ylabel("Zeit nach Vorlesungsbeginn(in min)")
plt.show()
