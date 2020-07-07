import numpy as np
import pandas as pd
from math import sqrt
import numpy.linalg as nlg

inputfile='userDatas.xlsx'
outputfile="result0.xlsx"

X=pd.read_excel(inputfile,index_col='用户id')
X1=(X-X.mean())/X.std()
C=X1.corr()
eig_value,eig_vector=nlg.eig(C)
eig=pd.DataFrame()
eig['name']=X.columns
eig['eig_value']=eig_value
for k in range(1,5):  #确定公共因子个数
    if eig['eig_value'][:k].sum()/eig['eig_value'].sum()>=0.8:  #如果解释度达到80%, 结束循环
        print(k)
        break
col0=list(sqrt(eig_value[0])*eig_vector[:,0])
col1=list(sqrt(eig_value[1])*eig_vector[:,1])
A=pd.DataFrame([col0,col1]).T
A.columns=['factor1','factor2']
h=np.zeros(21) #变量共同度，反映变量对共同因子的依赖程度，越接近1，说明公共因子解释程度越高，因子分析效果越好
D=np.mat(np.eye(21))#特殊因子方差，因子的方差贡献度 ，反映公共因子对变量的贡献，衡量公共因子的相对重要性
A=np.mat(A) #将因子载荷阵A矩阵化
for i in range(5):
    a=A[i,:]*A[i,:].T #A的元的行平方和
    h[i]=a[0,0] #计算变量X共同度,描述全部公共因子F对变量X_i的总方差所做的贡献，及变量X_i方差中能够被全体因子解释的部分
    D[i,i]=1-a[0,0] #因为自变量矩阵已经标准化后的方差为1，即Var(X_i)=第i个共同度h_i + 第i个特殊因子方差
from numpy import eye, asarray, dot, sum, diag #导入eye,asarray,dot,sum,diag 函数
from numpy.linalg import svd #导入奇异值分解函数
def varimax(Phi, gamma = 1.0, q =20, tol = 1e-6): #定义方差最大旋转函数
    p,k = Phi.shape #给出矩阵Phi的总行数，总列数
    R = eye(k) #给定一个k*k的单位矩阵
    d=0
    for i in range(q):
        d_old = d
        Lambda = dot(Phi, R)#矩阵乘法
        u,s,vh = svd(dot(Phi.T,asarray(Lambda)**3 - (gamma/p) * dot(Lambda, diag(diag(dot(Lambda.T,Lambda)))))) #奇异值分解svd
        R = dot(u,vh)#构造正交矩阵R
        d = sum(s)#奇异值求和
        if d_old!=0 and d/d_old:
            return dot(Phi, R)#返回旋转矩阵Phi*R
rotation_mat=varimax(A)#调用方差最大旋转函数
rotation_mat=pd.DataFrame(rotation_mat)#数据框化
X1=np.mat(X1) #矩阵化处理
factor_score=(X1).dot(A) #计算因子得分
factor_score=pd.DataFrame(factor_score)#数据框化
factor_score.columns=['因子','因子'] #对因子变量进行命名
factor_score.to_excel(outputfile)#打印输出因子得分矩阵


