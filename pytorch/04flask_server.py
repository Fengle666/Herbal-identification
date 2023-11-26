# 导入常用的库
import time
import os
import torch
from PIL import Image
from torchvision import transforms,models
# 导入flask库的Flask类和request对象
from flask import request, Flask
import torch.nn as nn

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #当前文件地址
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
# # 定义字典className_list，把种类索引转换为种类名称
classes = ['三七','乳薊','人参','首乌','六角英','决明子','千里光','半夏','尖叶苦菜','山药',
            '当归','旱莲草','曼陀罗','枳实','枸杞子','桔梗','沉香','浮小麦','熟地','牛筋草',
            '玫瑰花','珍珠草','生姜','白刺苋','白术','百合','石莲花','罗汉果','羊蹄草','芡实',
            '芦荟','苦菜','茯苓','荨麻','莲子','菊花','葵菜','蒲公英','薄荷','蚶壳草',
            '贝母','郁金','鱼腥草','鸡屎藤','鸡蛋花','鹿茸','黄芪','黄花菜','黄连','龙葵']  #标签序号对应类名

#------------------------------------------------------1.加载模型--------------------------------------------------------------
num_classes = 50
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

path_model="./model.ckpt"
model=torch.load(path_model)
model = model.to(device)
#------------------------------------------------------2.获取测试图片--------------------------------------------------------------

# 根据图片文件路径获取图像数据矩阵
def get_imageNdarray(imageFilePath):
    input_image = Image.open(imageFilePath).convert("RGB")
    return input_image


#------------------------------------------------------3.定义图片预处理--------------------------------------------------------------
# 模型预测前必要的图像处理
def process_imageNdarray(input_image):
    preprocess = transforms.Compose([
        transforms.ToTensor(),
    ])
    img_chw = preprocess(input_image)
    return img_chw  # chw:channel height width

#------------------------------------------------------4.模型预测--------------------------------------------------------------
# 使用模型对指定图片文件路径完成图像分类，返回值为预测的种类名称

def predict(imageFilePath):
    input_image = get_imageNdarray(imageFilePath)      #打开单张图片
    input_image = input_image.resize((224,224))
    img_chw = process_imageNdarray(input_image)

    if torch.cuda.is_available():
        img_chw = img_chw.view(1, 3, 224, 224).to(device)
    else:
        img_chw = img_chw.view(1, 3, 224, 224)
    model.eval()
    with torch.no_grad():
        torch.no_grad()
        out = model(img_chw)

        score = torch.nn.functional.softmax(out, dim=1)[0] * 100  #获得所有目标的准确率

        predicted = torch.max(out, 1)[1]
        # print(predicted)

        score = score[predicted.item()].item()    #获得最大目标的准确率
        # print(score)

        if predicted <= 50 and score>50:
            result1 = str(classes[predicted.item()])

            if result1 == '白刺苋':
                result1 = '白刺苋 ---------------------------------------------------------'

            elif result1 == '白术':
                result1 = '白术 -----------------------------------------------------'
            elif result1 == '百合':
                result1 = '百合 -----------------------------------------------------'
            elif result1 == '茯苓':
                result1 = '茯苓 -131321321412----------------------------------------------------'
            elif result1 == '半夏':
                result1 = '半夏 又名地文、守田等，属天南星目、天南星科、半夏属植物。药用植物，具有燥湿化痰，降逆止呕，生用消疖肿作用，兽医用以治锁喉癀。广泛分布于中国长江流域以及东北、华北等地区，在西藏也有分布，生长于海拔2500米以下。'

        else:
            result1 = '无法识别'
        return result1


#------------------------------------------------------5.服务返回--------------------------------------------------------------
# 定义回调函数，接收来自/的post请求，并返回预测结果
@app.route("/", methods=['POST'])
def return_result():
    startTime = time.time()
    received_file = request.files['file']
    imageFileName = received_file.filename
    if received_file:
        received_dirPath = './resources/received_images'
        if not os.path.isdir(received_dirPath):
            os.makedirs(received_dirPath)
        imageFilePath = os.path.join(received_dirPath, imageFileName)
        received_file.save(imageFilePath)
        print('图片文件保存到此路径：%s' % imageFilePath)
        usedTime = time.time() - startTime
        usedTime = usedTime * 1000
        print('接收图片并保存，总共耗时%.2fms' % usedTime)
        startTime = time.time()
        print(imageFilePath)
        result = predict(imageFilePath)
        usedTime = time.time() - startTime
        print('完成对接收图片的检测，总共耗时%.2fms' % usedTime)
        print("testtest",result)
        result = result + str(' ') + str('%.2fms'%usedTime)
        return result
    else:
        return 'failed'


# 主函数
if __name__ == "__main__":
    print('在开启服务前，先测试predict_image函数')
    print('\n')
    app.run("127.0.0.1", port=4399)


