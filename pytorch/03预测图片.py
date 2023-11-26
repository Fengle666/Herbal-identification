import warnings
warnings.filterwarnings("ignore")
import torch
from PIL import Image
import torch.nn as nn
import matplotlib.pyplot as plt
from torchvision import transforms,models


classes = ['三七','乳薊','人参','首乌','六角英','决明子','千里光','半夏','尖叶苦菜','山药',
            '当归','旱莲草','曼陀罗','枳实','枸杞子','桔梗','沉香','浮小麦','熟地','牛筋草',
            '玫瑰花','珍珠草','生姜','白刺苋','白术','百合','石莲花','罗汉果','羊蹄草','芡实',
            '芦荟','苦菜','茯苓','荨麻','莲子','菊花','葵菜','蒲公英','薄荷','蚶壳草',
            '贝母','郁金','鱼腥草','鸡屎藤','鸡蛋花','鹿茸','黄芪','黄花菜','黄连','龙葵']  #标签序号对应类名
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')  #是否使用gpu加速
num_classes = 12

class MobileNet(nn.Module):
    def __init__(self, num_classes=num_classes):   # num_classes
        super(MobileNet, self).__init__()
        net = models.mobilenet_v2(pretrained=True)   # 从预训练模型加载mobilenet_v2网络参数
        net.classifier = nn.Sequential()
        self.features = net
        self.classifier = nn.Sequential(    # 定义自己的分类层
                nn.Linear(1280, 1000),
                nn.ReLU(True),
                nn.Dropout(0.5),
                nn.Linear(1000, num_classes),
        )

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x

def test_mydata(a):   #定义预测函数
    # 调整图片大小
    im = plt.imread(a)     #读入图片
    images = Image.open(a)     #将图片存储到images里面
    images = images.resize((224, 224))   #调整图片的大小为224*224的大小
    images = images.convert('RGB')    #RGB化

    transform = transforms.ToTensor()
    images = transform(images)   #图像转化成tensor类型
    images = images.resize(1, 3, 224, 224)    #调整输入网络图片大小
    images = images.to(device)   #gpu加速

    path_model = "./model.ckpt"   #调用训练好的模型
    model = torch.load(path_model)
    model = model.to(device)

    model.eval()
    outputs = model(images)    #将图片传入模型预测
    values, indices = outputs.data.max(1)  #返回最大概率值和下标  output不是tensor类型所以要加.data
    print(classes[int(indices[0])])   #输出类名
    plt.title(int(indices[0]))   #输出标签
    plt.imshow(im)    #展示结果
    plt.show()


while True:
    img = input('Input image filename:')
    try:
        image = Image.open(img)
    except:
        print('Open Error! Try again!')
        continue
    else:
        r_image = test_mydata(img)



