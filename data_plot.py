import os

import matplotlib.pyplot as plt
from read_data import read_json



def save_plot(save_name):
    post_fix = '.png'
    save_path = save_name[0:18]
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    plt.savefig(save_name+post_fix)

def data_plot(file_path, class_number,save_name):
    # 读取json
    data_distributions=read_json(file_path)
    # 设置字体大小和加粗
    plt.rcParams['font.size'] = 14  # 设置字体大小
    plt.rcParams['axes.labelweight'] = 'bold'  # 设置坐标轴标签为加粗
    plt.rcParams['legend.fontsize'] = 14  # 设置图例字体大小，可根据需要调整

    # 创建一个图和轴
    fig, ax = plt.subplots()

    # 对于每个客户机的数据分布
    for client_id, distribution in enumerate(data_distributions):
        # 对于每个类标签和对应的样本数量
        for class_label, count in distribution:
            # 在散点图上绘制一个点
            ax.scatter(client_id, class_label, s=count*0.1, c='red', alpha=1)

    # 设置标题和坐标轴标签
    # ax.set_title('Data Distribution Across Clients')
    ax.set_xlabel('Client ID')
    ax.set_ylabel('Class Labels')
    # 设置x轴范围为0至data_distributions的大小
    ax.set_xlim(0, len(data_distributions))
    # 设置y轴范围为
    ax.set_ylim(0, class_number-1)
    # ax.margins(x=0.5, y=0.5)  # x和y方向上分别增加5%的边际空间
    # 设置x轴和y轴的刻度为整数
    ax = plt.gca()  # 获取当前坐标轴
    ax.xaxis.set_major_locator(plt.MultipleLocator(2))  # x轴刻度间隔设为1
    ax.yaxis.set_major_locator(plt.MultipleLocator(1))  # y轴刻度间隔设为1

    # 添加网格，网格线会根据刻度自动设置
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # 添加网格线，包括主网格和次网格
    # save
    save_plot(save_name)
    # 显示图表
    plt.show()



if __name__ == '__main__':
    data_plot('gen_data/cifar10_cl20_pat.json', 10, 'gen_plot/24-10-09/data_cifar10_cl20_pat')
    data_plot('gen_data/cifar10_cl20_dir.json', 10, 'gen_plot/24-10-09/data_cifar10_cl20_dir')
