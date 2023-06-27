#Execute the process»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
def executeProcess(ProcessArr,pid,duration,Gant_chart):
    x={}
    for i in ProcessArr:
        if i['pid']==pid:
            x=i
    while(x['bt']!=0 and duration!=0):
        Gant_chart.append(x['pid'])
        x['bt']-=1
        duration-=1

#TO calculate TAT
def findTAT(ProcessArr,Gant_chart,pid):
    x={}
    for i in ProcessArr:
        if i['pid']==pid:
            x=i
    TAT=len(Gant_chart)
    for i in range(len(Gant_chart)-1,-1,-1):
        if(Gant_chart[i]!=pid):
            TAT-=1
        else:
            break
    TAT=TAT-x['at']
    return TAT

#To calculate Response Time
def findResponseTime(ProcessArr,Gant_chart,pid):
    x={}
    for i in ProcessArr:
        if i['pid']==pid:
            x=i
    RT=0
    for i in range(len(Gant_chart)):
        if(Gant_chart[i]!=pid):
            RT+=1
        else:
            break
    RT=RT-x['at']
    return RT

#To calculate Waiting Time
def findWaitingTime(ProcessArr,Gant_chart,pid):
    x={}
    for i in ProcessArr:
        if i['pid']==pid:
            x=i
    WT=findTAT(ProcessArr,Gant_chart,pid)-x['bt']
    return WT

#DRIVER CODE===============================================================================

ProcessArr = []
N=0
#Calculate GantChart»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
with open('Input.txt', 'r') as f:
        string = f.readlines()
        N = int(string[0].strip())
        for i in range(1, N + 1):
            ProcessID, ArrivalTime, BurstTime = map(int, string[i].split())
            ProcessArr.append({'pid': ProcessID, 'at': ArrivalTime, 'bt': BurstTime})
ProcessArr.sort(key=lambda x: x['at'])
Gant_chart = []
quantum=int(input("Enter Time Quantum: "))              #Time Quantum is set to 4. It can be changed here
completecount=0
while(completecount<=N):
    for x in ProcessArr:
        if(x['bt']!=0): 
            if(x['at']<=len(Gant_chart)):
                executeProcess(ProcessArr,x['pid'],quantum,Gant_chart)
            # else:
            #     Gant_chart.append('-')
    completecount+=1
ProcessArr = []
N=0
with open('Input.txt', 'r') as f:
        string = f.readlines()
        N = int(string[0].strip())
        for i in range(1, N + 1):
            ProcessID, ArrivalTime, BurstTime = map(int, string[i].split())
            ProcessArr.append({'pid': ProcessID, 'at': ArrivalTime, 'bt': BurstTime})
ProcessArr.sort(key=lambda x: x['at'])
#Printing||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
print("Gant Chart» ",Gant_chart)
print("+-----+--------------+------------+--------------+---------------+------------------+----------------+")
print("| PID | Arrival Time | Burst Time | Waiting Time | Response Time | Turn Around Time | Relative Delay |")
print("+-----+--------------+------------+--------------+---------------+------------------+----------------+")
TotalRD=0
TotalTAT=0
TotalWT=0
TotalRT=0
for x in ProcessArr:
    WT=findWaitingTime(ProcessArr,Gant_chart,x['pid'])
    RT=findResponseTime(ProcessArr,Gant_chart,x['pid'])
    TAT=findTAT(ProcessArr,Gant_chart,x['pid'])
    RD=findTAT(ProcessArr,Gant_chart,x['pid'])/x['bt']
    TotalWT+=WT
    TotalRT+=RT
    TotalTAT+=TAT
    TotalRD+=RD
    print(f"| {x['pid']:3} | {x['at']:12} | {x['bt']:10} | {WT:12} | {RT: 13} | {TAT:16} | {round(RD, 2):14} |")
    print("+-----+--------------+------------+--------------+---------------+------------------+----------------+")
print(f"| {'AVG':3} | {'':12} | {'':10} | {round(TotalRT/N,2): 13} | {round(TotalWT/N,2):12} | {round(TotalTAT/N,2):16} | {round(TotalRD/N, 2):14} |")
print("+-----+--------------+------------+--------------+---------------+------------------+----------------+")