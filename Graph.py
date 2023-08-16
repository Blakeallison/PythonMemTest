import matplotlib.pyplot as plt
#import json

# our data
# with open("mem_results.json") as jobj:
#    data = json.load(jobj)

data = [(10000, 1.8489583), (20000, 3.729167), (30000, 6.4114583), (40000, 7.65625), (50000, 11.859375), (60000, 13.05729167), (70000, 14.5625), (80,000, 15.927083), (90000, 19.90625), (10000, 21.36979167)]

xVal = [item[0] for item in data]
yVal = [item[1] for item in data]

fig, ax = plt.subplots()
ax.plot(xVal, yVal)

ax.set(xlabel='Num of objects', ylabel='USS Memory (MB)', title='Flat dictionary')
ax.grid()

plt.show()
