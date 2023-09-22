import csv
with open('C:/Users/peyman/pythonProject17/sense.csv','r') as f:
    p=[]
    t=[]
    power=[]
    time=[]
    reader=csv.reader(f)
    for row in reader:
        t.append(row[0])
        p.append(row[1])
    for p in p[1:]:
        power.append(p)
    for t in t[1:]:
        time.append(t)
    for i in range(len(power)):
        if float(power[i])>=0.35 and float(power[i])<=0.85:
            print(f'Time : {time[i]} s and Power : {power[i]} result :  This power is dangerous!!!!!!!!!')
        else:
            print(f'Time : {time[i]} s and Power : {power[i]} result : Power is good')



