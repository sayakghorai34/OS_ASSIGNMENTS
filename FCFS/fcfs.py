import numpy as np
import csv
#============================================================================================================================================
def findWaitingTime(n, bt, wt, at):
	Running_Time = [0] * n
	Running_Time[0] = 0
	wt[0] = 0
	for i in range(1, n):
		Running_Time[i] = (Running_Time[i - 1] + bt[i - 1])
		wt[i] = Running_Time[i] - at[i]
		if (wt[i] < 0):
			wt[i] = 0
#============================================================================================================================================
def findTurnAroundTime(n, bt, wt, tat):
	for i in range(n):
		tat[i] = bt[i] + wt[i]
#============================================================================================================================================
def findavgTime( n,p, bt, at):
	wt = [0] * n
	tat = [0] * n
	findWaitingTime(n, bt, wt, at)
	findTurnAroundTime(n, bt, wt, tat)
	
	print("\n","--------+----------------------------------------------------+")
	print("\t","| Processes    BT    AT    TAT    WT    RT      RD   |")
	print("\t","|----------------------------------------------------|")
	total_wt = 0
	total_tat = 0
	total_rt=total_wt
	total_rd=0
	csvArr=[['Process','BT','AT','TAT','WT','RT','RD']]
	for i in range(n):
		total_wt +=wt[i]
		total_tat += tat[i]
		rt=wt[i]
		rd=tat[i]/bt[i]
		total_rd+=rd
		print("\t","    P",p[i],"      ", bt[i],"   ", at[i],"   ", tat[i],"   ", wt[i],"    ",rt,"    ","%.2f "%rd )
		print("\t","|....................................................|")
		csvArr.append([p[i],bt[i],at[i],tat[i],wt[i],rt,"%.2f "%rd])
	print("_________|______________________________________________________|")
	print("Total:   |   ",n,"                   ",total_tat,"   ",total_wt,"    ",total_rt,"    ","%.2f"%total_rd)
	print("~~~~~~~~~|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
	print("Average: | ","/",n,"                  ","%.2f"%(total_tat/n)," ","%.2f"%(total_wt/n),"  ","%.2f"%(total_rt/n)," ","%.2f"%(total_rd/n))
	print("~~~~~~~~~+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+\n")
# Write in CSV »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
	csvArr.append(["  "])
	csvArr.append(["Avg TAT ","Avg WT ","Avg RT ","Avg RD"])
	csvArr.append(["%.2f"%(total_tat/n),"%.2f"%(total_wt/n),"%.2f"%(total_rt/n),"%.2f"%(total_rd/n)])
	arr=np.asarray(csvArr)
	with open('output_fcfs.csv','w') as file:
		mwr=csv.writer(file,delimiter=',')
		mwr.writerows(csvArr)
	print("Results are saved in output.csv file~~~~~~~~~~~~")

#=============================================================================================================================================
if __name__ =="__main__":
	array=np.loadtxt("sourcefile.csv",skiprows=1,delimiter=',')
	Process=[]
	AT=[]
	BT=[]
	array = sorted(array, key=lambda x:x[1])
	print(array)
	for i in range(len(array)):
		Process.append(int(array[i][0]))
		AT.append(int(array[i][1]))
		BT.append(int(array[i][2]))
	n=len(Process)
	findavgTime( n,Process, BT, AT)

    
