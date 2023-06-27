#Given Question where we have 3 type of resource
Available=[3,3,2]
Processes=[
    {'pid':'P1','Allocated':[0,1,0],'MaxRequirement':[7,5,3],'Need':[]},
    {'pid':'P2','Allocated':[2,0,0],'MaxRequirement':[3,2,2],'Need':[]},
    {'pid':'P3','Allocated':[3,0,2],'MaxRequirement':[9,0,2],'Need':[]},
    {'pid':'P4','Allocated':[2,1,1],'MaxRequirement':[2,2,2],'Need':[]},
    {'pid':'P5','Allocated':[0,0,2],'MaxRequirement':[4,3,3],'Need':[]}
    ]

#Have to Calculate
SafeSequence=[]
#Calculate_Need
for x in Processes:
    for i in range(3):
        x['Need'].append(x['MaxRequirement'][i]-x['Allocated'][i])
    # print(x['Need'])

#Get Safe Sequence
while(len(SafeSequence)<5):
    for x in Processes:
        flag=True
        for i in range(3):
            # print(x['Need'][i],Available[i])
            if(x['Need'][i]>Available[i]):
                flag=False
                break
        if flag:
            SafeSequence.append(x['pid'])
            for j in range(3):
                Available[j]+=x['MaxRequirement'][j]
            Processes.remove(x)
            break

print('Total Resources Available: ',Available)
print(SafeSequence)

