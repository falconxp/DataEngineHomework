import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

#   生成训练数据、Categorical数据编码&min/max转换
def training_data_norm(data):
    tran_x = data.drop(['car_ID','CarName'], axis=1)
    # 将数据标签化
    symbolic_index = ['fueltype','aspiration','doornumber','carbody','drivewheel','enginelocation','enginetype','cylindernumber','fuelsystem']
    le = LabelEncoder()
    for item in symbolic_index:
        tran_x[item] = le.fit_transform(tran_x[item])
    # 将数据0-1标准化
    min_max_scaler = preprocessing.MinMaxScaler()
    tran_x = min_max_scaler.fit_transform(tran_x)
    return tran_x

#   K-Means手肘法寻找最佳K值
def k_value_cal(data):
    train_data_norm = training_data_norm(data)
    N = range(1, 20)
    sse = []
    for k in N:
        # K-Means算法
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(train_data_norm)
        # 计算inertia簇内误差平方和
        sse.append(kmeans.inertia_)
    x = N
    plt.xlabel('K')
    plt.ylabel('SSE')
    plt.plot(x, sse, 'o-')
    plt.show()

#   聚类算法
def K_means(data, n_clusters):
    train_data_norm = training_data_norm(data)
    # 使用KMeans聚类
    kmeans = KMeans(n_clusters)
    kmeans.fit(train_data_norm)
    predict_y = kmeans.predict(train_data_norm)

    result = data.copy()
    # 提取车辆品牌
    result['CarSeries'] = [x.split(' ')[0] for x in result['CarName']]
    # 合并聚类结果，插入到原数据最后一列
    result['聚类结果'] = predict_y
    return result

#   VW竞品筛选
def vw_competitor(result):
    # 提取品牌为volkswagen的记录
    result_vw = pd.concat([result[result['CarSeries'] == 'volkswagen'],
                           result[result['CarSeries'] == 'vw'],
                           result[result['CarSeries'] == 'vokswagen']])
    competitor = []
    # 获取和volkswagen品牌相同聚类结果的品牌
    for i in result_vw['聚类结果'].unique():
        competitor += list(result[result['聚类结果'] == i]['CarSeries'].unique())
    # 品牌去重
    competitor = list(set(competitor))
    # 去掉volkswagen自身
    competitor.remove('volkswagen')
    competitor.remove('vw')
    competitor.remove('vokswagen')
    return competitor

def main():
    data = pd.read_csv('./CarPrice_Assignment.csv', encoding='gbk')
    k_value_cal(data)
    result = K_means(data, n_clusters=6)
    competitor = vw_competitor(result)
    print("Volkswagen品牌竞品：")
    print(competitor)

if __name__ == '__main__':
    main()