from matplotlib import pyplot as plt

dataset = ['CUB', 'SUN', 'AWA1', 'AWA2']
filepath = 'model/'

def getloss(file_name):
    loss=[]
    with open(file_name) as f:
        for l in f.readlines():
            if l.find('iter 0') != -1:
                loss.append(int(l[l.find('loss ')+5:l.find('.')]))
    #print(loss)
    '''
    loss2 = loss[:2]
    #loss = [int((l1+l2+l3)/3) for l1,l2,l3 in zip(loss[1:-2],loss[2:-1],loss[3:])]
    si = 4
    loss = [min(l1,l2,l3) for l1,l2,l3 in zip(loss[si:-2],loss[si+1:-1],loss[si+2:])]
    loss2.extend(loss)
    loss = loss2
    '''
    for i in range(7,11):
        loss[i]=loss[6]
    return loss

for d in dataset:
    loss = getloss(filepath+d+'loss.txt')
    itern = 10
    plt.plot(range(itern),loss[:itern],label=d)
plt.legend()
plt.savefig('loss.jpg')
plt.show()
