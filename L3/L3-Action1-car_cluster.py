# 使用KMeans进行聚类
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np

# 数据加载
data = pd.read_csv('car_data.csv', encoding='gbk')
print(data)
train_x = data[["人均GDP","城镇人口比重","交通工具消费价格指数", "百户拥有汽车量"]]
print(train_x)


# 规范化到 [0,1] 空间
min_max_scaler=preprocessing.MinMaxScaler()
# train_x 是个矩阵，包括4列，每列分别做MinMaxScaler
train_x=min_max_scaler.fit_transform(train_x)
# pd.DataFrame(train_x).to_csv('temp.csv', index=False)
print(train_x)

### 使用KMeans聚类
kmeans = KMeans(n_clusters=3)
# 训练
kmeans.fit(train_x)
# 预测
predict_y = kmeans.predict(train_x)
# 合并聚类结果，插入到原数据中
result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类结果'},axis=1,inplace=True)
print(result)
# 将结果导出到CSV文件中
result.to_csv("car_cluster_result.csv",index=False, encoding='gbk')


### 使用层次聚类
from scipy.cluster.hierarchy import dendrogram, ward
from sklearn.cluster import KMeans, AgglomerativeClustering
import matplotlib.pyplot as plt
model = AgglomerativeClustering(linkage='ward', n_clusters=3)
y = model.fit_predict(train_x)
print(y)

linkage_matrix = ward(train_x)
dendrogram(linkage_matrix)
plt.show()