from datetime import datetime


t = (3,30,2019,9,25)

print(datetime.strptime(str(t), "(%I, %M, %Y, %m, %d)").strftime("%m/%d/%Y %I:%M"))
