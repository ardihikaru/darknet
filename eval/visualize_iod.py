import matplotlib.pyplot as plt
import numpy as np
# import csv

def int_to_tuple(Ks):
    lst = []
    for i in range(Ks):
        lst.append((i+1))
    return tuple(lst)

# def read_data(fname):
#     data_path = "hw5/dataset/saved_csv/"
#     fpath = data_path + fname
#
#     with open(fpath, 'r') as f:
#         reader = csv.reader(f)
#         # dataset = list(reader)
#         return [float(line[0]) for line in list(reader)]
#         # print(" >> dataset = ", dataset)
#         # print(" >> LEN dataset = ", len(dataset))
#         # print(" >> data = ", data)
#         # print(" >> dataset = ", reader)

if __name__ == '__main__':
    # Define number of iteration (K)
    K = 10
    ks = int_to_tuple(K)  # used to plot the results

    #           00  01  02  03  05  07  09
    # Person     1   2   1   0   2   1   2
    # Flag       1   0   1   1   2   2   3

    # Test Dataset: 00, 01, 02, 05, 07, 09
    person = [
        34,
        32, 26,
        90,

        51, 37,
        51, 85,
        60, 29
    ]

    flag = [
        69,

        72,
        72,
        68, 82,
        68, 83,
        69, 71, 94
    ]

    print(" total len = ", len(person), len(flag))

    mean_acc_person = round(np.mean(np.array(person)), 2)
    # min_acc_person = round(np.min(np.array(person)), 2)
    mean_acc_flag = round(np.mean(np.array(flag)), 2)
    # min_acc_flag = round(np.min(np.array(flag)), 2)

    fig = plt.figure()

    print("MEAN_ACC(Person) = " + str(mean_acc_person) + "; MEAN_ACC(Flag) = " + str(mean_acc_flag))
    title = "Classification Accuracy between Person and Flag label"
    plt.title(title)
    plt.plot(ks, person, label='Person Average Precision (AP)')
    plt.plot(ks, flag, label='Flag Classification Accuracy')
    plt.axhline(mean_acc_person, color='blue', linestyle='dashed', linewidth=1)
    plt.axhline(mean_acc_flag, color='orange', linestyle='dashed', linewidth=1)
    # plt.axhline(min_acc_person, color='red', linestyle='dashed', linewidth=1)
    # plt.axhline(min_acc_flag, color='green', linestyle='dashed', linewidth=1)
    plt.legend()
    plt.show()
    fig.savefig('eval/results/oid-accuracy.png', dpi=fig.dpi)

