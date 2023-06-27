import matplotlib.pyplot as plt

Composition = ["Process", "TAT", "BT", "WT", "AT", "RD"]

#=== SJF Preemptive ============================================================================================================================

def Preemptive_SJF(filename):

    #Open File, read lines, append all datas in process array ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    with open(filename, 'r') as f:
        string = f.readlines()
        N = int(string[0].strip())
        ProcessArr = []
        for i in range(1, N + 1):
            ProcessID, ArrivalTime, BurstTime = map(int, string[i].split())
            ProcessArr.append({'pid': ProcessID, 'at': ArrivalTime, 'bt': BurstTime, 'rd': BurstTime})
    ProcessArr.sort(key=lambda x: x['at'])
    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    time = 0
    isCompleated = 0
    Gant_chart = []
    Start_T = {}
    responses = []

    while isCompleated < N:
        WaitingQueue = [p for p in ProcessArr if p['at'] <= time and p['rd'] > 0]
        if len(WaitingQueue) == 0:
            time += 1
            continue
        ShortestP = min(WaitingQueue, key=lambda x: x['rd'])
        ProcessID = ShortestP['pid']
        if ProcessID not in Start_T:
            Start_T[ProcessID] = time
        ShortestP['rd'] -= 1
        Gant_chart.append(ShortestP['pid'])
        if ShortestP['rd'] == 0:
            isCompleated += 1
            ShortestP['CompletionT'] = time + 1
            ShortestP['tat'] = ShortestP['CompletionT'] - ShortestP['at']
            ShortestP['wt'] = ShortestP['tat'] - ShortestP['bt']
            rt = Start_T[ProcessID] - ShortestP['at']
            responses.append(rt)
        time += 1
    print("Gant_Chart»» ",Gant_chart)
    print("+-----+--------------+------------+--------------+---------------+------------------+----------------+")
    print("| P_ID| Arrival Time | Burst Time | Response Time | Waiting Time | Turn Around Time | Relative Delay |")
    print("+-----+--------------+------------+--------------+---------------+------------------+----------------+")
    Total_TAT = 0
    Total_WT = 0
    Relative_Delay = []
    for p in range(0, len(ProcessArr)):
        single_rd = ProcessArr[p]['tat'] / ProcessArr[p]['bt']
        Relative_Delay.append(single_rd)
    for p in range(0, (len(ProcessArr))):
        print(f"| P{ProcessArr[p]['pid']:2} | {ProcessArr[p]['at']:12} | {ProcessArr[p]['bt']:10} | {responses[p]: 13} | {ProcessArr[p]['wt']:12} | {ProcessArr[p]['tat']:16} | {round(Relative_Delay[p], 2):14} |")
        print("+-----+--------------+------------+--------------+---------------+------------------+----------------+")
        Total_TAT += ProcessArr[p]['tat']
        Total_WT += ProcessArr[p]['wt']

    print(
        f"| {'AVG':3} | {'':12} | {'':10} | {round(sum(responses) / len(ProcessArr),2): 13} | {round(Total_WT/N,2):12} | {round(Total_TAT/N,2):16} | {round(sum(Relative_Delay) / len(ProcessArr), 2):14} |")
    print("+-----+--------------+------------+--------------+---------------+------------------+----------------+")

#=== LJF Preemptive ============================================================================================================================
def ljf_preemptive(filename):

    #Open File, read lines, append all datas in process array ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    with open(filename, 'r') as f:
        string = f.readlines()
        N = int(string[0].strip())
        ProcessArr = []
        for i in range(1, N + 1):
            ProcessID, ArrivalTime, BurstTime = map(int, string[i].split())
            ProcessArr.append({'pid': ProcessID, 'at': ArrivalTime, 'bt': BurstTime, 'rd': BurstTime})
    ProcessArr.sort(key=lambda x: x['at'])
    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    time = 0
    isCompleated = 0
    Gant_chart = []
    Start_T = {}
    responses = []

    while isCompleated < N:
        WaitingQueue = [p for p in ProcessArr if p['at'] <= time and p['rd'] > 0]
        if len(WaitingQueue) == 0:
            time += 1
            continue
        LongestP = max(WaitingQueue, key=lambda x: x['rd'])
        LongestP['rd'] -= 1
        ProcessID = LongestP['pid']
        if ProcessID not in Start_T:
            Start_T[ProcessID] = time
        Gant_chart.append(LongestP['pid'])
        if LongestP['rd'] == 0:
            isCompleated += 1
            LongestP['ct'] = time + 1
            LongestP['tat'] = LongestP['ct'] - LongestP['at']
            LongestP['wt'] = LongestP['tat'] - LongestP['bt']
            rt = Start_T[ProcessID] - LongestP['at']
            responses.append(rt)
        time += 1
#````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
    print("Gant_Chart»» ",Gant_chart)
    print("+-----+--------------+------------+--------------+---------------+------------------+----------------+")
    print("| PID | Arrival Time | Burst Time | Waiting Time | Response Time | Turn Around Time | Relative Delay |")
    print("+-----+--------------+------------+--------------+---------------+------------------+----------------+")
    Total_TAT = 0
    Total_WT = 0
    Relative_Delay = []
    for p in range(0, len(ProcessArr)):
        single_rd = ProcessArr[p]['tat'] / ProcessArr[p]['bt']
        Relative_Delay.append(single_rd)
    for p in range(0, (len(ProcessArr))):
        print(f"| {ProcessArr[p]['pid']:3} | {ProcessArr[p]['at']:12} | {ProcessArr[p]['bt']:10} | {ProcessArr[p]['wt']:12} | {responses[p]: 13} | {ProcessArr[p]['tat']:16} | {round(Relative_Delay[p], 2):14} |")
        print("+-----+--------------+------------+--------------+---------------+------------------+----------------+")
        Total_TAT += ProcessArr[p]['tat']
        Total_WT += ProcessArr[p]['wt']

    print(
        f"| {'AVG':3} | {'':12} | {'':10} | {round(sum(responses) / len(ProcessArr),2): 13} | {round(Total_WT/N,2):12} | {round(Total_TAT/N,2):16} | {round(sum(Relative_Delay) / len(ProcessArr), 2):14} |")
    print("+-----+--------------+------------+--------------+---------------+------------------+----------------+")


program = ["SJF", "LJF"]
print('Choose a program to run')
for i in range(2):
    print(f'{i+1}: {program[i]}')
choice = int(input("> "))

if choice == 1:
    Preemptive_SJF('Input.txt')
else:
    ljf_preemptive('Input.txt')
















