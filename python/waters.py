import random

a3={'volume':3,'water':0,'name':'3升水杯'}
a5={'volume':5,'water':0,'name':'5升水杯'}
a8={'volume':8,'water':8,'name':'8升水杯'}

holds=[a3,a5,a8]
print(holds)
status=[{(8,8),(0,5),(0,3)},{(0,8),(5,5),(3,3)}]

def pour(a,b):#a往b倒水
    bremain=b['volume']-b['water']
    if bremain<a['water']:
        a['water']-=bremain
        b['water']=b['volume']
    else:
        b['water']+=a['water']*(a['water']>=0)
        a['water']=0

def checkstatus(holds,status):
    statu=[]
    for hold in holds:
        statu.append((hold['water'],hold['volume']))
    statu=set(statu)
    if statu in status:
        pass
    else:
        status.append(statu)
    return status


while True:
    a0=random.choice(holds)
    acopy=a0.copy()
    holds.remove(a0)
    b0=random.choice(holds)
    bcopy=b0.copy()
    holds.remove(b0)
    pour(a0,b0)
    before=len(status)
    status=checkstatus(holds+[a0,b0],status)
    after=len(status)
    if before==after:
        holds.append(acopy)
        holds.append(bcopy)
    else:
        holds=holds+[a0,b0]
        print(acopy['name']+'往'+bcopy['name']+'倒'+str((acopy['water']-a0['water'])*(acopy['water']>=0))+'升水')
        print(holds)
        for hold in holds:
            if hold['water']==4:
                exit()
    
