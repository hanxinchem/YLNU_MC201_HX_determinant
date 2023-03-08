#输入行列式
det=[]
line=input("请输入（空格隔开）：")
while line !="":
    det.append(line.split())
    line=input("请输入（空格隔开）：")
#定义二阶行列式的计算法则
def f(det2):
    return float(det2[0][0])*float(det2[1][1])-float(det2[0][1])*float(det2[1][0])
#定义划线计算的法则
def h(detn):
    #扩列
    for n in range(len(detn)):
        for m in range(len(detn)-1):
            detn[n] += detn[n]
    #计算正对角线的值
    sum1 = 0
    for j in range(0,len(det)):
        que1= 1
        for i in range(0,len(det)):
            que1 *= int(det[i][i+j])
        sum1 +=que1
    print("正对角线",sum1)
    #计算负对角线的值
    sum2 = 0
    for a in range(0,len(det)):
        que2= 1
        for b in range(1,len(det)+1):
            que2 *= int(det[-b][b+a])
        sum2 +=que2
    print("负对角线",sum2)  
    return sum1 - sum2        
#如果是二阶行列式直接利用二阶行列式法则
if len(det) == 2 :
    print(f(det))
#如果不是二阶行列式则利用划线法则
else:
    print(h(det))
