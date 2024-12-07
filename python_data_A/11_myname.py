import csv
import matplotlib.pyplot as plt

f = open('python_data_A/csv_data/age2.csv', 'r', encoding='utf8')
data = csv.reader(f)
result = []
yp_all = []
# for row in data:
#     if "청운면" in row[0]:
#         for i in row[3:]:
#             if ',' in i:
#                 i = i.replace(',', "")
#             result.append(int(i))

# plt.bar(range(len(result)), result)
# plt.show()

label_ages = ["0~19", "20 ~ 39", "40~59", "60~"]

for i in data:
    result.append(i)

for da in range(len (result)):
    for change in range(len(result[da][3:])):
        if "," in result[da][change + 3]:
            result[da][change + 3] = int(result[da][change + 3].replace(",", ""))
        else:
            result[da][change + 3] = int(result[da][change + 3])

yp_all.append(sum(result[0][3:5]))
yp_all.append(sum(result[0][5:7]))
yp_all.append(sum(result[0][7:9]))
yp_all.append(sum(result[0][9:]))


plt.pie(yp_all, labels = label_ages, autopct="%.1f%%")
plt.show()