
i = input("Please enter the number of trades: ")

j=0
long=0
short=0
while j<int(i):
    ab=input("Enter long/short ")

    if(ab.lower()=="long"):
        long+=1
    elif(ab.lower()=="short"):
        short+=1
    j+=1
print("Long->"+str(long))
print("Short->"+str(short))



