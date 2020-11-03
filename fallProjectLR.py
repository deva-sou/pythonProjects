#Linear Regression Pure Python Model - SOU Deva
from matplotlib import pyplot as plt

###Part 1 - Classical implementation###

#Function for mean 
def mean(a):
    return sum(a)/len(a)

#LR classic
def linReg_classic(a,b):
    x = 0
    y = 0
    z = 0
    
    for i in range(len(a)):
        x += (a[i] - mean(a)) * (b[i] - mean(b))
        y += (a[i] - mean(a)) ** 2
        z += (b[i] - mean(b)) ** 2
    
    slope = x/y
    yIntercept = mean(b) - slope * mean(a)
    corrCoeff = 1 - (x/(y*z))
    
    return [yIntercept,slope,corrCoeff]

###Part 2 - Implementation with covariance###

#Functions for variance and covariance 
def variance(a): 
    varValue = 0 
    for i in range(len(a)): 
        varValue += (a[i] - mean(a)) ** 2 / len(a)
    return varValue

def covariance(a,b):
    covarValue = 0
    for i in range(len(a)):
        covarValue += ((a[i] - mean(a)) * (b[i] - mean(b))) / len(a)
    return covarValue

#LR with covariance
def linReg_cov(a,b):
    slope = covariance(a,b) / variance(a)
    yIntercept = mean(b) - slope * mean(a)
    return [yIntercept,slope]

###Part 3 - Implementation with Gradient Descent### 

#Functions rewrote from numpy
def hypothesis(theta,x): 
    hypothesisList=[]
    calculation = 0
    for i in range(len(x)): 
        calculation = theta[0] + theta[1] * x[i]
        hypothesisList.append(calculation)
    return hypothesisList

def cost_calc(theta,x,y): 
    m =len(x)
    h=hypothesis(theta,x)
    sumOfHypothesis = 0
    for i in range(m): 
        sumOfHypothesis += ((h[i] - y[i])**2)
    sumOfHypothesis = (1/2 * m) * sumOfHypothesis
    return sumOfHypothesis

def gradient_descent(theta,x,y,epoch,alpha):
    cost=[]
    i=0
    m=len(x)
    while i < epoch: 
        hx = hypothesis(theta, x)
        theta0 = 0
        theta1 = 0
        for j in range(m):
            theta0 += (hx[j] - y[j])
            theta1 += ((hx[j] - y[j]) * x[j])
        theta[0] -= alpha * (theta0 / m)
        theta[1] -= alpha * (theta1 / m)
        cost.append(cost_calc(theta,x,y))
        i += 1
    return theta,cost

def predict(theta,x,y,epoch,alpha):
    theta, cost = gradient_descent(theta,x,y,epoch,alpha)
    return hypothesis(theta,x), cost, theta

def linReg_GD(a,b,epoch,A):
    theta = [0,0]
    prediction = predict(theta,a,b,epoch,A)
    return prediction[2]

###Part 4 - Application with Data###
# def data
def test_dataset():
  return [
  [
    6.1101, 5.5277, 8.5186, 7.0032, 5.8598, 8.3829, 7.4764, 8.5781, 6.4862, 5.0546, 5.7107, 
    14.164, 5.734, 8.4084, 5.6407, 5.3794, 6.3654, 5.1301, 6.4296, 7.0708, 6.1891, 20.27, 
    5.4901, 6.3261, 5.5649, 18.945, 12.828, 10.957, 13.176, 22.203, 5.2524, 6.5894, 9.2482, 
    5.8918, 8.2111, 7.9334, 8.0959, 5.6063, 12.836, 6.3534, 5.4069, 6.8825, 11.708, 5.7737, 
    7.8247, 7.0931, 5.0702, 5.8014, 11.7, 5.5416, 7.5402, 5.3077, 7.4239, 7.6031, 6.3328, 
    6.3589, 6.2742, 5.6397, 9.3102, 9.4536, 8.8254, 5.1793, 21.279, 14.908, 18.959, 7.2182, 
    8.2951, 10.236, 5.4994, 20.341, 10.136, 7.3345, 6.0062, 7.2259, 5.0269, 6.5479, 7.5386, 
    5.0365, 10.274, 5.1077, 5.7292, 5.1884, 6.3557, 9.7687, 6.5159, 8.5172, 9.1802, 6.002, 
    5.5204, 5.0594, 5.7077, 7.6366, 5.8707, 5.3054, 8.2934, 13.394, 5.4369], 
  [
    17.592, 9.1302, 13.662, 11.854, 6.8233, 11.886, 4.3483, 12, 6.5987, 3.8166, 3.2522, 15.505, 
    3.1551, 7.2258, 0.71618, 3.5129, 5.3048, 0.56077, 3.6518, 5.3893, 3.1386, 21.767, 4.263, 
    5.1875, 3.0825, 22.638, 13.501, 7.0467, 14.692, 24.147, -1.22, 5.9966, 12.134, 1.8495, 
    6.5426, 4.5623, 4.1164, 3.3928, 10.117, 5.4974, 0.55657, 3.9115, 5.3854, 2.4406, 6.7318, 
    1.0463, 5.1337, 1.844, 8.0043, 1.0179, 6.7504, 1.8396, 4.2885, 4.9981, 1.4233, -1.4211,
    2.4756, 4.6042, 3.9624, 5.4141, 5.1694, -0.74279, 17.929, 12.054, 17.054, 4.8852, 5.7442, 
    7.7754, 1.0173, 20.992, 6.6799, 4.0259, 1.2784, 3.3411, -2.6807, 0.29678, 3.8845, 5.7014, 
    6.7526, 2.0576, 0.47953, 0.20421, 0.67861, 7.5435, 5.3436, 4.2415, 6.7981, 0.92695, 0.152, 
    2.8214, 1.8451, 4.2959, 7.2029, 1.9869, 0.14454, 9.0551, 0.61705
  ]
 ]

# def graphs
def graph_cost(colomn1,colomn2):
    #DATA 
    theta = [0,0]
    epoch200 = predict(theta,colomn1,colomn2,200,0.01)
    epoch2000 = predict(theta,column1,column2,2000,0.01)
    epoch20000 = predict(theta,column1,column2,20000,0.01)
    alpha1 = predict(theta,colomn1,colomn2,2000,0.009)
    alpha2 = predict(theta,colomn1,colomn2,2000,0.015)
    alpha3 = predict(theta,column1,colomn2,2000,0.02)

    #SETUP GRAPHS
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(10, 7))
    ax0, ax1, ax2, ax3, ax4, ax5 = axes.flatten()
    #COMPARING DIFFERENT EPOCH
    # 200
    n200=len(epoch200[1])
    x200=n200*[0]
    y200=n200*[0]
    for i in range(n200):
        x200[i]=i
        y200[i]=epoch200[1][i]
    ax0.plot(x200,y200,label="Epoch 200",color="blue")
    ax0.set_xlabel("epoch")
    ax0.set_ylabel("Cost")
    ax0.set_title("Cost graph (epoch = 200, alpha = 0.01)",y=-0.30,fontsize=7)
    ax0.legend()
    ax0.grid()
    # 2000
    n2000=len(epoch2000[1])
    x2000=n2000*[0]
    y2000=n2000*[0]
    for i in range(n2000):
        x2000[i]=i
        y2000[i]=epoch2000[1][i]
    ax1.plot(x2000,y2000,label="Epoch 2000",color="green")
    ax1.set_xlabel("epoch")
    ax1.set_ylabel("Cost")
    ax1.set_title("Cost graph (epoch = 2000, alpha = 0.01)",y=-0.30,fontsize=7)
    ax1.legend()
    ax1.grid()
    # 20000
    n20000=len(epoch20000[1])
    x20000=n20000*[0]
    y20000=n20000*[0]
    for i in range(n20000):
        x20000[i]=i
        y20000[i]=epoch20000[1][i]
    ax2.plot(x20000,y20000,label="Epoch 20000",color="red")
    ax2.set_xlabel("epoch")
    ax2.set_ylabel("Cost")
    ax2.set_title("Cost graph (epoch = 20000, alpha = 0.01)",y=-0.3,fontsize=7)
    ax2.legend()
    ax2.grid()

    #DIFFERENT ALPHA FOR 2000 EPOCH
    n1=len(alpha1[1])
    x1=n1*[0]
    y1=n1*[0]
    for i in range(n1):
        x1[i]=i
        y1[i]=alpha1[1][i]
    ax3.plot(x1,y1,label="Epoch 2000",color="green")
    ax3.set_xlabel("epoch")
    ax3.set_ylabel("Cost")
    ax3.set_title("Cost graph (epoch = 2000, alpha = 0.009)",y=-0.3,fontsize=7)
    ax3.legend()
    ax3.grid() 
    
    n2=len(alpha2[1])
    x2=n2*[0]
    y2=n2*[0]
    for i in range(n2):
        x2[i]=i
        y2[i]=alpha2[1][i]
    ax4.plot(x2,y2,label="Epoch 2000",color ="green")
    ax4.set_xlabel("epoch")
    ax4.set_ylabel("Cost")
    ax4.set_title("Cost graph (epoch = 2000, alpha = 0.015)",y=-0.3,fontsize=7)
    ax4.legend()
    ax4.grid()

    n3=len(alpha3[1])
    x3=n3*[0]
    y3=n3*[0]
    for i in range(n3):
        x3[i]=i
        y3[i]=alpha3[1][i]
    ax5.plot(x3,y3,label="Epoch 2000",color="green")
    ax5.set_xlabel("epoch")
    ax5.set_ylabel("Cost")
    ax5.set_title("Cost graph (epoch = 2000, alpha = 0.02)",y=-0.3,fontsize=7)
    ax5.legend()
    ax5.grid() 

    plt.suptitle('Evolution of cost according to different epochs\n or different alphas', size='x-large')

    fig.tight_layout()
    plt.show()

###Main Program###
data = test_dataset()
column1 = data[0]
column2 = data[1]
print("Classic: ",linReg_classic(column1,column2))
print("With cov: ",linReg_cov(column1,column2))
print("With gradient: ",linReg_GD(column1,column2,2000,0.01))
#Increase epoch:# 
print("With epoch at 3000: ",linReg_GD(column1,column2,3000,0.01))
print("With epoch at 30000: ",linReg_GD(column1,column2,30000,0.01))
#Decrease epoch: 
print("With epoch at 1000: ",linReg_GD(column1,column2,1000,0.01))
print("With epoch at 100: ",linReg_GD(column1,column2,100,0.01))
#Modification of alpha: 
print("With alpha = 0.001: ",linReg_GD(column1,column2,1000,0.001))
print("With alpha = 0.0001: ",linReg_GD(column1,column2,100,0.0001))
graph_cost(column1,column2)
