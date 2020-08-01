import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

def get_products(data):
    # 生成客户订单独热编码表
    hot_encoded_df = data.groupby(data['客户ID'])['产品名称'].value_counts().unstack().fillna(0)
    hot_encoded_df[hot_encoded_df > 1] = 1
    return hot_encoded_df


def get_rule(encoded_transaction, min_support=0.05, min_threshold=1):
    # 挖掘频繁项集
    frequent_itemsets = apriori(encoded_transaction, min_support=min_support, use_colnames=True)
    frequent_itemsets = frequent_itemsets.sort_values(by='support', ascending=False)
    print('频繁项集：\n', frequent_itemsets)
    # 挖掘关联规则
    rules = association_rules(frequent_itemsets, metric='lift', min_threshold=min_threshold)
    rules = rules.sort_values(by='lift', ascending=False)
    print('关联规则：\n', rules)
    return frequent_itemsets, rules


def main():
    # 读入数据
    data = pd.read_csv('./订单表.csv', encoding='gbk')
    # 生成客户订单独热编码表
    products = get_products(data)
    # 计算频繁项集和关联规则
    get_rule(products)


if __name__ == "__main__":
    main()