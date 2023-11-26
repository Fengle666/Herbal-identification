import os
import random

#设置随机种子 确保对图片每次打乱顺序都是一样的
def setup_seed(seed):
    random.seed(seed)
setup_seed(20)

#生成训练集文本
b = 0
dir = './dataset/'
#os.listdir的结果就是一个list集合
#可以使用一个list的sort方法进行排序，有数字就用数字排序
files = os.listdir(dir)          #获得扩增后图片文件夹路径
files.sort()
#print("files:", files)  #创建txt文件用于后续数据储存
train = open('./train.txt', 'w')
test = open('./test.txt', 'w')
a = 0
a1 = 0
while(b < 50):#50是因为50个文件夹 循环50次
    label = a #设置要标记的标签
    ss = './dataset/' + str(files[b]) + '/' #训练图片
    pics = os.listdir(ss) #得到train文件夹下的图片
    i = 1
    train_percent = 0.8  # 训练集样本占比 训练集0.8 则测试集0.2

    num = len(pics)  # 得到样本总数
    list = range(num)
    train_num = int(num * train_percent)  # 训练集总数
    train_sample = random.sample(list, train_num)  # 在list中随机选择 train_num个长度，并乱序
    test_num = num - train_num     #获得测试样本数

    for i in list:  # 循环输出文件
        name = str(dir) + str(files[b]) + '/' + pics[i] + ' ' + str(int(label)) + '\n'  # 获得当前文件夹下所有图片序列名称
        if i in train_sample:  # 判断i是否在训练集中
            train.write(name)  # 如果在，输出图片做训练文本中
        else:
            test.write(name)    #其余的做测试文本中
    a = a + 1
    b = b + 1
train.close()  #操作完成后一定要记得关闭文件
test.close()