import matplotlib.pyplot as plt
import numpy as np
import csv

def int_to_tuple(Ks):
    lst = []
    for i in range(Ks):
        lst.append((i+1))
    return tuple(lst)

def read_data(fname, size):
    data_path = "dataset/cleaned/"
    fpath = data_path + fname

    result = [0.0 for i in range(size)]
    with open(fpath, 'r') as f:
        reader = csv.reader(f)
        for line in list(reader):
            idx = int(line[0]) - 1
            result[idx] = float(line[1]) # sorted
    return result

if __name__ == '__main__':
    # Define number of iteration (K)
    K = 57
    ks = int_to_tuple(K)  # used to plot the results

    gpu_proc_latency = read_data('result_gpu.csv', K)
    cpu_proc_latency = read_data('result_cpu.csv', K)

    mean_gpu_acc_proc_latency = round(np.mean(np.array(gpu_proc_latency)), 2)
    mean_cpu_acc_proc_latency = round(np.mean(np.array(cpu_proc_latency)), 2)

    print(" ## mean_gpu_acc_proc_latency = ", mean_gpu_acc_proc_latency)
    print(" ## mean_cpu_acc_proc_latency = ", mean_cpu_acc_proc_latency)

    fig = plt.figure()
    title = "Recognition Latency of TM-04: CPU vs GPU"
    plt.title(title)
    plt.plot(ks, gpu_proc_latency, label='GPU Recognition Latency (ms)')
    plt.plot(ks, cpu_proc_latency, label='CPU Recognition Latency (ms)')
    # plt.axhline(mean_gpu_acc_proc_latency, color='green', linestyle='dashed', linewidth=1)
    # plt.axhline(mean_cpu_acc_proc_latency, color='orange', linestyle='dashed', linewidth=1)
    plt.xlabel('Frame ID')
    plt.ylabel('Latency (ms)')
    plt.legend()
    plt.show()
    fig.savefig('results/recognition-latency-comparison.png', dpi=fig.dpi, transparent=True)

    fig_gpu = plt.figure()
    title = "GPU Only Recognition Latency of TM-04"
    plt.title(title)
    plt.plot(ks, gpu_proc_latency, label='GPU Recognition Latency (ms)')
    plt.axhline(mean_gpu_acc_proc_latency, color='green', linestyle='dashed', linewidth=1)
    plt.xlabel('Frame ID')
    plt.ylabel('Latency (ms)')
    plt.legend()
    plt.show()
    fig_gpu.savefig('results/recognition-latency-gpu.png', dpi=fig_gpu.dpi, transparent=True)
