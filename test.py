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

Process=[{'pid': 3, 'at': 0, 'bt': 0}, {'pid': 6, 'at': 2, 'bt': 0}, {'pid': 1, 'at': 4, 'bt': 0}, {'pid': 2, 'at': 5, 'bt': 0}, {'pid': 4, 'at': 6, 'bt': 0}, {'pid': 5, 'at': 9, 'bt': 0}]
Gant=[3, 3, 3, 6, 6, 6, 6, 1, 1, 1, 1, 2, 2, 2, 2, 4, 4, 4, 4, 5, 5, 5, 5, 6, 1, 1, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
print(findResponseTime(Process,Gant,4))