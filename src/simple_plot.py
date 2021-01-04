import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

#
# x_vals = [10, 11, 12, 13]
# y_vals = [10, 11, 12, 13]
# x1_vals = [14, 15, 16, 17]
# y1_vals = [14, 15, 16, 17]

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
# #     ax.annotate(n[i],(x_vals[i],y_vals[i]+0.2))
# plt.plot(x_vals,y_vals)
# plt.plot(x1_vals,y1_vals)
# plt.show()


# Some data:
dat = np.array([[5, 3, 4, 4, 6],
                [1, 5, 3, 2, 2]])

# This is the point you want to point out
point = dat[:, 2]

# Make the figure
plt.figure(1, figsize=(4, 4))
plt.clf()
ax = plt.gca()
# Plot the data
ax.plot(dat[0], dat[1], 'o', ms=10, color='r')
ax.set_xlim([2, 8])
ax.set_ylim([0, 6])


circle_rad = 15  # This is the radius, in points
ax.plot(point[0], point[1], 'o',
        ms=circle_rad * 2, mec='b', mfc='none', mew=2)
ax.annotate('Midici', xy=point, xytext=(60, 60),
            textcoords='offset points',
            color='b', size='large',
            arrowprops=dict(
                arrowstyle='simple,tail_width=0.3,head_width=0.8,head_length=0.8',
                facecolor='b', shrinkB=circle_rad * 1.2)
)
plt.show()