import json
import torch

import h5py
import re
from pathlib import Path
def read_h5(file_path):
    '''
    :param file_path:
    :return: loss_list,acc_list
    '''
    with h5py.File(file_path, 'r') as f:
        data_dict={}
        keys=list(f.keys())
        # print(keys)
        if len(keys)==4:
            acc_data = f[keys[1]]
            loss_data = f[keys[3]]
            cost_time = f[keys[0]]
            cost_time_list = cost_time[()]
            data_dict['cost_time']=cost_time_list
        else:
            acc_data=f[keys[0]]
            loss_data=f[keys[2]]

        # print(loss_data,acc_data)
        acc_list = acc_data[()]
        loss_list = loss_data[()]

        data_dict['acc']=acc_list
        data_dict['loss']=loss_list
        return data_dict

def read_html(file_path,join_clients=10):
    # 从PFedLa中提取数据
    # 匹配模式
    pattern = r'client\s*.*="r3">(\d+)\s*.*\s*="r9">(\d+.\d+).*="r9">(\d+.\d+).*="r10">(\d+.\d+).*="r10">(\d+.\d+)'
    pat2= r'ROUND:\s*<span class="r3">(\d+)</span>.*'
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
        # 查找匹配项
        matches = re.findall(pattern, html_content)
        results = []
        for match in matches:
            results.append(match)
        # 查找round
        mat2 = re.findall(pat2, html_content)
        rounds=[]
        for mat in mat2:
            rounds.append(int(mat))
    print(rounds)
    data_dict={}
    for i in range(len(rounds)):
        data_dict[rounds[i]]=results[i*join_clients:(i+1)*join_clients]
    # 对每一轮的loss与acc分别求平均，并以float形式存储到list
    loss_list=[]
    acc_list=[]
    for key in data_dict.keys():
        print(key)
        print(data_dict[key])
        losses=[]
        acccs=[]
        for i in range(len(data_dict[key])):
            losses.append(float(data_dict[key][i][2]))
            acccs.append(float(data_dict[key][i][4]))
        loss_list.append(sum(losses)/len(losses))
        acc_list.append(sum(acccs)/len(acccs))
    print(loss_list)
    print(acc_list)
    return loss_list,acc_list, rounds


def is_h5(file_path):
    p=Path(file_path)
    suffix=p.suffix
    if suffix=='.h5':
        return True
    else:
        return False
def read_data(file_path):
    p=Path(file_path)
    suffix=p.suffix
    if suffix=='.h5':
        read_result=read_h5(file_path)
        return read_result
    elif suffix=='.html':
        loss_list,acc_list, rounds=read_html(file_path)
        return loss_list, acc_list,rounds
    else:
        raise Exception('suffix error')
def read_json(file_path):
    # 打开并读取JSON文件
    with open(file_path, 'r') as file:
        data_distributions = json.load(file)['Size of samples for labels in clients']
        print(data_distributions)
        return data_distributions

