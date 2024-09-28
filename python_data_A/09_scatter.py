# import matplotlib.pyplot as plt
# plt.style.use('ggplot')
# plt.scatter([1, 2, 3, 4], [10, 30, 20, 100])
# plt.show()


# import matplotlib.pyplot as plt
# plt.style.use('ggplot')
# plt.scatter([1, 2, 3, 4], [10, 30, 20, 100], s=[100, 1000, 250, 300])
# plt.show()


# import matplotlib.pyplot as plt
# plt.style.use('ggplot')
# plt.scatter([1, 2, 3, 4], [10, 30, 20, 100], s=[100, 1000, 250, 300], c=['red', 'blue', 'green', 'gold'])
# plt.show()

# import matplotlib.pyplot as plt
# plt.style.use('ggplot')
# plt.scatter([1, 2, 3, 4], [10, 30, 20, 100], s=[100, 1000, 250, 300], c=range(4))
# plt.show()

# import matplotlib.pyplot as plt
# plt.style.use('ggplot')
# plt.scatter([1, 2, 3, 4], [10, 30, 20, 100], s=[100, 1000, 250, 300], c=range(4), cmap='cool')
# plt.show()

# import matplotlib.pyplot as plt
# plt.style.use('ggplot')
# plt.scatter([1, 2, 3, 4], [10, 30, 20, 100], s=[100, 1000, 250, 300], c=range(4), cmap='cool')
# plt.colorbar()
# plt.show()

# import matplotlib.pyplot as plt
# import random
# x = []
# y = []
# size = []
# for i in range(100):
#     x.append(random.randint(50,100))
#     y.append(random.randint(50,100))
#     size.append(random.randint(10,100))
# plt.style.use('ggplot')
# # plt.scatter(x, y, s=size)
# # plt.scatter(x, y, s=size, c=size, cmap='jet')
# plt.scatter(x, y, s=size, c=size, cmap="jet", alpha=0.7)
# plt.colorbar()
# plt.show()


import matplotlib.pyplot as plt
import csv
f = open('python_data_A/csv_data/age.csv', 'r', encoding='utf8')
data = csv.reader(f)
x = list(range(0, 101))
y1 = []
y2 = []
size1 = []
size2 = []
for row in data:
    if "개군면" in row[0]:
        for i in range(0, 101):
            y1.append(int(row[(i+3)]))
    if "청운면" in row[0]:
        for i in range(0, 101):
            y2.append(int(row[(i+3)]))
size = y1
size = y2
plt.style.use('ggplot')
# plt.scatter(x, y, s=size)
# plt.scatter(x, y, s=size, c=size, cmap='jet')
plt.scatter(x, y1, s=size, c=size, cmap="tab20", alpha=0.7)
plt.scatter(x, y2, s=size, c=size, cmap="YlGn_r", alpha=0.7)
plt.colorbar()
plt.show()
