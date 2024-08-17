import csv
import matplotlib.pyplot as plt
f = open('python_data_A\yp.csv', 'r', encoding='utf8')
data  = csv.reader(f, delimiter=',')
# print(f, type(f), type(data))
header = next(data)
# print(header)
min = 0
min_day = ""
max = 0
max_day = ""
my_min = 0 
my_max = 0
my_day = "2008-01-08"
my_birthday = []
my_temp = []
for row in data:
    row[0] = row[0].lstrip()
    if row[-1] == "" or row[-2] == "" or row[-3] == "":
        pass
    else:
        # row[-2], row[-1] = float(row[-2]), float(row [-1])
        # if row[-2] <= min:
        #     min = row[-2]
        #     min_day = row[0]
        # if row[-1] >= max:
        #     max = row[-1]
        #     max_day = row[0]



        row[2] = float(row[2])
        if int(row[0][:4]) >= 2008:
            if row[0][5:] == "10-11":
                my_birthday.append(int(row[0][:4]))
                my_temp.append(row[2])




        # if row[0] == my_day:
        #     my_min, my_max = row[-2], row[-1]




# print(f"양평최저기온 : {min_day} : {min}")
# print(f"양평최고기온 : {max_day} : {max}")
# print(f"{my_day} 최고 {my_max} 최저 {my_min}")
plt.title("jung si woo fool")
plt.plot(my_birthday, my_temp, 'r', linestyle = '--', label = 'every year temp')
plt.plot(my_birthday, my_temp, 'k.' )
plt.legend()
plt.show()
# print(my_birthday, my_temp)
f.close()