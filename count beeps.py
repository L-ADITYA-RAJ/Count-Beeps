n=int(input()) #Getting Input as Integer but in Binary form
def btd(n): #Function to convert Binary to decimal
    d,i = 0,0
    while(n != 0):
        r = n % 10
        d = d + r * pow(2, i)
        n = n//10
        i += 1
    return d
x=len(str(n)) #Finding length of n for using it in loops
n=str(n) #Converting it as String to do (STRING)Conversion
l=[] #Empty list
y=0 #
for i in range(0,x,1):
    v=n[i:]+n[:i] #string conversion/rotation
    v=int(v) #converted string to integer binary
    v=btd(v) #converted integer binary to integer decimal
    l.append(v)
for i in l:
    if i%2==0:
        y=y+1
print(y)