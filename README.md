# Count-Beeps
Binary representation of a number ‘n’ are written on a circle which is divided into ‘m’ segments. Here the number of bits required to represent ‘n’ is ‘m’. A needle is fixed on the top of this circle and the circle rotates in clockwise direction for every ten seconds till a complete rotation is made that is the number of rotations is equal to ‘m-1’. Let the segment pointed by needle be ‘p’. A beep sound is made when the decimal equivalent of the binary digits is even when read from the next segment to the right of ‘p’ to the segment ‘p’. Given the binary digits written on the segment from the segment next to ‘p’ to ‘p’, write a C program to find the number of times beep sound will be made. For example, if the initial configuration of binary string given is ‘1001101’ then the binary strings obtained by rotation are 1001101 1100110 0110011 1011001 1101100 0110110 0011011 The binary strings 1100110, 1101100 and 0110110 are even when decimal equivalent is taken. Hence beep sound will be made three times. Boundary Conditions Length of the binary string &lt; 25 Input Format First line contains the binary representation of the number ‘n’ Output Format Print the number of times beep sound will be made
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
