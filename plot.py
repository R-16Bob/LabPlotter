import matplotlib.pyplot as plt
import os
from read_data import read_data,is_h5

post_fix = '.png'

def draw_acc(epoch, acc_lists, labels, colors, save_path):
    epochs = list(range(epoch))

    # draw multiple accuracy curves
    for i, (accuracies, label, color) in enumerate(zip(acc_lists, labels, colors)):
        plt.plot(epochs, accuracies[0:epoch], label=label, color=color)

    plt.xlabel('Round')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.savefig(save_path + '_acc' + post_fix)
    plt.show()


def draw_loss(epoch, loss_lists, labels, colors, save_path):
    epochs = list(range(epoch))

    # draw multiple loss curves
    for i, (losses, label, color) in enumerate(zip(loss_lists, labels, colors)):
        plt.plot(epochs, losses[:epoch], label=label, color=color)

    plt.xlabel('Round')
    plt.ylabel('Loss')
    plt.legend()
    plt.savefig(save_path + '_loss' + post_fix)
    plt.show()


def draw_plot(epoch, files, labels, colors, save_name):
    # create save dir
    save_path=save_name[0:14]
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    # Read data
    loss_list = []
    acc_list = []
    for file in files:
        if is_h5(file) :
            read_result = read_data(file)
        # else:
        #     losses, accuracies,rounds= read_data(file)
        loss_list.append(read_result['loss'])
        acc_list.append(read_result['acc'])
    # 设置字体大小和加粗
    plt.rcParams['font.size'] = 14  # 设置字体大小
    plt.rcParams['axes.labelweight'] = 'bold'  # 设置坐标轴标签为加粗
    plt.rcParams['legend.fontsize'] = 14  # 设置图例字体大小，可根据需要调整

    # draw
    draw_acc(epoch, acc_list, labels, colors, save_name)
    draw_loss(epoch, loss_list, labels, colors, save_name)


if __name__ == '__main__':
    default_colors = ["#4169E1", "#32CD32", "#40E0D0", "#FF8C00", "#FF0000", "#9400D3"]

    # 自定义设置
    files = ['data/24-07-22/FashionMNIST_FedAvg_cl20_iid.h5',
             'data/24-07-22/FashionMNIST_FedAvg_cl20_dir.h5',
             'data/24-07-22/FashionMNIST_FedAvg_cl20_pat.h5',
             'data/24-07-22/FashionMNIST_FedAvg_cl20_pat_ub.h5',
             ]
    labels = ['iid', 'dir', 'pat','pat_ub']
    colors = default_colors
    save_name = 'plot/24-07-22/FashionMNIST_FedAvg_cl20'
    epochs = 200

    draw_plot(epochs, files, labels, colors, save_name)