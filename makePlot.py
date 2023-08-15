import matplotlib.pyplot as plt
import json

# our data
with open("mem_results.json") as jobj:
    data = json.load(jobj)

#data = [(20000, 3.671875), (40000, 4.953125), (60000, 10.25), (80000, 12.921875), (100000, 13.015625)]

xVal = [item[1] for item in data]
yVal = [item[0] for item in data]

fig, ax = plt.subplots()
ax.plot(xVal, yVal)

ax.set(xlabel='USS Memory (MB)', ylabel='Num of objects', title='Flat dictionary')
ax.grid()

plt.show()
