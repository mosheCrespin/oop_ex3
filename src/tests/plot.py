import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def plot():
    barWidth = 0.2

    # set height of bar

    networkX = [0.0,0.0,0.0]
    java = [0.0,0.0,0.0]
    python = [0.0,0.0,0.0]

    print("networkX")
    networkX[0] = float(input("shortest path: "))
    networkX[1] = float(input("connected components: "))

    print("java")
    java[0] = float(input("shortest path: "))
    java[1] = float(input("connected components: "))
    java[2] = float(input("connected component: "))


    print("python")
    python[0] = float(input("shortest path: "))
    python[1] = float(input("connected components: "))
    python[2] = float(input("connected component: "))

    # Set position of bar on X axis
    r1 = np.arange(len(networkX))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]

    # Make the plot
    plt.bar(r1, networkX, color='blue', width=barWidth, edgecolor='black', label='networkX')
    plt.bar(r2, java, color='purple', width=barWidth, edgecolor='black', label='java')
    plt.bar(r3, python, color='orange', width=barWidth, edgecolor='black', label='python')

    # Add xticks on the middle of the group bars
    plt.xlabel('methods', fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(networkX))], ['shortest path', 'connected components', 'connected component'])

    # Create legend & Show graphic
    plt.xlabel("methods")
    plt.ylabel("run-time in Seconds ")
    plt.title("avg run-time")

    plt.legend()
    plt.show()

if __name__ == '__main__':
    plot()
    #
    # sum_sp=0.0
    # print("networkx")
    # for i in range(0,6):
    #     sum_sp+=float(input(f"shortest path {i}->"))
    # sum_ccs=0.0
    # for i in range(0,6):
    #     sum_ccs+=float(input(f"connected components{i}->"))
    #
    # print(f"shortest path: {sum_sp/6}\n connected components: {sum_ccs/6}")
    # print("-"*10)
    #
    # sum_sp=0.0
    # print("python")
    # for i in range(0,6):
    #     sum_sp+=float(input(f"shortest path {i}->"))
    # sum_ccs=0.0
    # for i in range(0,6):
    #     sum_ccs+=float(input(f"connected components{i}->"))
    #
    # sum_cc=0.0
    # for i in range(0,6):
    #     sum_cc+=float(input(f"connected component{i}->"))
    #
    # print(f"shortest path: {sum_sp / 6}\n connected components: {sum_ccs / 6}\n connected component: {sum_cc/6}")
    # print("-" * 10)

    #
    # sum_sp = 0.0
    # print("java")
    # for i in range(0, 6):
    #     sum_sp += float(input(f"shortest path {i}->"))
    # sum_ccs = 0.0
    # for i in range(0, 6):
    #     sum_ccs += float(input(f"connected components{i}->"))
    #
    # sum_cc = 0.0
    # for i in range(0, 6):
    #     sum_cc += float(input(f"connected component{i}->"))
    #
    # print(f"shortest path: {sum_sp / 6}\n connected components: {sum_ccs / 6}\n connected component: {sum_cc / 6}")
    # print("-" * 10)
    #






