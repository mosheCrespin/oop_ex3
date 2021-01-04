import numpy as np
import matplotlib.pyplot as plt

x_vals = [10, 11, 12, 13]
y_vals = [10, 11, 12, 13]
x1_vals = [14, 15, 16, 17]
y1_vals = [14, 15, 16, 17]

# plt.title("oop")
# plt.xlabel(" x axis ")
# plt.ylabel(" y axis ")
#
# plt.plot(x_vals, y_vals, "o")
# plt.show()
#
# x = np.arange(0, 10, 0.1)
# y = np.sin(x)
#
# plt.title("oop")
# plt.xlabel(" x axis ")
# plt.ylabel(" y axis ")
#
# plt.plot(x, y)
# plt.plot(x_vals, y_vals,"D-")  # union
# plt.show()
# n=[10,20,30,40]
# fig, ax=plt.subplots()
# ax.scatter(x_vals,y_vals)
# my_list=[10,20,30,40,50]
# for i,v in enumerate(my_list):
#     print(i,v)
# for i , txt in enumerate(n):
#     ax.annotate(n[i],(x_vals[i],y_vals[i]+0.2))
plt.plot(x_vals,y_vals)
plt.plot(x1_vals,y1_vals)
plt.show()