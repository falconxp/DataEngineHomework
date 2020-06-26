### use numpy to calculate
import numpy as np
persontype = np.dtype({'names':['name','chinese','math','english','total'],'formats':['S32','i','i','i','i']})
peoples = np.array([('zhangfei',68,65,30,0),('guanyu',95,76,98,0),('dianwei',90,88,77,0),('xuzhu',80,90,90,0)],dtype=persontype)

student_name = peoples[:]['name']
chineses = peoples[:]['chinese']
maths = peoples[:]['math']
englishs = peoples[:]['english']
#calculate total score
peoples[:]['total']=chineses+maths+englishs

#output result
print('所有人的语文平均成绩：',np.average(chineses))
print('所有人的数学平均成绩：',np.average(maths))
print('所有人的英语平均成绩：',np.average(englishs))
print('---------------------------------------')
print('所有人的语文最小成绩：',np.min(chineses))
print('所有人的数学最小成绩：',np.min(maths))
print('所有人的英语最小成绩：',np.min(englishs))
print('---------------------------------------')
print('所有人的语文最大成绩：',np.max(chineses))
print('所有人的数学最大成绩：',np.max(maths))
print('所有人的英语最大成绩：',np.max(englishs))
print('---------------------------------------')
print('所有人的语文成绩方差：',np.var(chineses))
print('所有人的数学成绩方差：',np.var(maths))
print('所有人的英语成绩方差：',np.var(englishs))
print('---------------------------------------')
print('所有人的语文成绩标准差：',np.std(chineses))
print('所有人的数学成绩标准差：',np.std(maths))
print('所有人的英语成绩标准差：',np.std(englishs))
print('---------------------------------------\n')

#rank
df = sorted(peoples, key=lambda peoples:peoples[4], reverse=True)  
print(df)

#output rank result
for i in range(len(df)):
    print("排名: {} 姓名: {} 总成绩: {} ".format(i+1, df[i][0], df[i][4]))
