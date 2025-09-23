#W2A1
print('Hello World!')

#W2A2
name = input()
print ("Chao ban", name)

#W2A3
# Phep toan + cong - tru * nhan / chia thuong // chia nguyen % chia du
a, b = map(int, input().split())  # Nhap 2 so nguyen tren cung mot dong
print (f'{a} + {b} = {a + b}')
print (f' {a} - {b} = {a - b}')
print (f'{a} * {b} = {a*b}')
print (f' {a} / {b} = {a / b:.2f}')
print (f'{a} // {b} = {a // b}')
print (f'{a} % {b} = {a % b}')


#W2A4
a1, b1, c1, a2, b2, a3 = map(int, input().split())
tb = ((a1 + b1 + c1) + (a2 + b2)*2 + a3*3)/10
print (f'{tb:.2f}')

#W2A5
a, b = map(int, input().split())
print (a**b)

#W2A6
char = input()
print( ord(char)) #In ra ma coode unicode cua ki tu
hoa = ord (char) - 32  #'a' = 97, 'A' = 65
print(chr(hoa)) # chuyen tu ma unicode sang ki tu 

#W2A7
A=((13**2)*3) + 5
B=13**2*3 + 5
print(A, B)

#W2A8
C = float(input())
F = 9/5 * C + 32
print(f'{9/5 * C +32 :.2f}')


#W2A9
x = float(input())
print(f'{ x + 10 + 0.3*x + 0.1*x :.2f}', "USD")


#W2A10
a, b, c = input().split()
print('Hello', c ,',', b,'and', a, sep=' ')

#W2A11
h = int(input())
m = int(input())
print(h*60*60 + m*60)

#W2A12
n = int(input())
print(n*n*6)

#W2A13
a, b = map(int, input().split())
T = a*b 
print ( T % 10 )

#W2A14
a=1
b=3
print(a, b)
a = a + b 
b = a - b 
a = a - b 
print(a, b)

#W2A15
n = int(input())
print( 6*n*(n-1) + 1 )

#W2A16
print( 'Spring', 'Summer', 'Autumn', 'Winter', sep='\n')

#W2A17
print(' ','*')
print('','***')
print('*****')

#W2A18 
print('### ##    ###  ###')
print(' #  #  #   #    #')
print(' #  #   #  #    #')
print(' #  #  #   #    #')
print(' #  ##     #    #')

#W2A19
print('Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', sep='\n')

#W2A20
print('January','Feburary','March','April','May','June','July','August','September','October','November','December', sep = '\n')

#W2A21
n=11
for i in range(0,n):
    print('Hello, world')