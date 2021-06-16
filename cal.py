
cal = [True]*54

def calify(leapYear):
	wei=0
	i=28
	moi=0

	if leapYear:
	 monthDays =  ( 31,   31,  29,  31,  30,  31,  30,  31,  31,  30,  31,  30,  31,   31)
	else:
	 monthDays =  ( 31,   31,  28,  31,  30,  31,  30,  31,  31,  30,  31,  30,  31,   31)
	monthNames = ("De", "Ja","Fe","Mr","Ap","My","Jn","Jl","Au","Se","Oc","Nv","De", "Ja")

	print("   wk:  Mo   Tu   We   Th   Fr   Sa   Su ")
	while True:
	  week = monthNames[moi]+" "
	  week += "{:2d}: ".format(wei)
	  wei+=1
	  cleanWeek = True
	  for _ in range(7):
	    week += "{:2d}".format(i)
	    #week += "__"
	    if i<7:
	      cleanWeek=False
	      cal[wei-1]=False
	      week+="#  "
	    elif i==7:
              week+="~  "
	    else:
	      week+="   "
	    i+=1
	    if (i>monthDays[moi]):
	      i=1
	      moi+=1

	  if cleanWeek:
	    week+="#"

	  print(week)

	  if (moi==13):
	    break

print("leapyear:")
calify(True)
print("non leapyear:")
calify(False)


monthind = 0
monthNames = (
    "January",
    "Frebrurury",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)
was = False
for i in range(53):
 if cal[i]:
   if not was:
     print("{:2d}: ## {}".format(i,monthNames[monthind]))
     monthind+=1
     was = True
   else:
     print("{:2d}: ##".format(i))
 else:
   print("{:2d}: ".format(i))
   was = False

