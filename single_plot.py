import matplotlib.pyplot as plt
import os
from read_data import read_data

post_fix = '.png'

def draw_acc(epoch, accuracies, file_path):
    epochs = [i for i in range(epoch)]
    # epochs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 迭代次数
    # accuracies = [0.5, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.88, 0.9, 0.92]  # 准确率列表
    # 绘制准确率曲线图
    # plt.figure(figsize=(10, 5))  # 设置图表大小
    plt.plot(epochs, accuracies[0:epoch], label='Accuracy')  # 绘制曲线
    plt.xlabel('Round')  # 设置横轴标签
    plt.ylabel('Accuracy')  # 设置纵轴标签
    #plt.title('Training Accuracy over Epochs')  # 设置图表标题
    plt.legend()  # 显示图例
    # plt.grid(True)  # 显示网格
    plt.savefig(file_path+ '_acc'+post_fix)  # 保存为pdf
    plt.show()  # 显示图表


def draw_loss(epoch, losses, file_path):
    epochs = [i for i in range(epoch)]
    # 如果要绘制损失曲线图，只需要将上面的准确率列表换成损失列表即可
    # losses = [0.2, 0.15, 0.12, 0.1, 0.08, 0.06, 0.04, 0.02, 0.01, 0.005]

    # plt.figure(figsize=(10, 5))  # 设置图表大小
    plt.plot(epochs, losses[0:epoch], label='Loss')  # 绘制曲线
    plt.xlabel('Round')  # 设置横轴标签
    plt.ylabel('Loss')  # 设置纵轴标签
    #plt.title('Training Loss over Epochs')  # 设置图表标题
    plt.legend()  # 显示图例
    # plt.grid(True)  # 显示网格
    plt.savefig(file_path + '_loss'+post_fix)
    plt.show()  # 显示图表


def draw_singel_plot():
    # 读取数据（需要修改的部分）
    file_dir = '24-07-22/'
    file_name = 'FashionMNIST_FedAvg_cl20_iid.h5'
    epoch = 200
    # 以下无需修改
    read_result = read_data('data/' + file_dir + file_name)
    # 生成保存目录
    plot_dir='plot/' + file_dir + '/'
    if not os.path.exists(plot_dir):
        os.makedirs(plot_dir)
    plot_file_name = plot_dir + file_name.split('.')[0]

    # 绘制曲线图
    draw_acc(epoch, read_result['acc'], plot_file_name)
    draw_loss(epoch, read_result['loss'], plot_file_name)

draw_singel_plot()