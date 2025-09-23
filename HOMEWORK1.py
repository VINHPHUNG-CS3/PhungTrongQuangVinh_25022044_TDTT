#Bài 1
n = int(input())
print(n*2)

#Bài 2
a = float(input())
b = float(input())
print(f'{a*b - 3.14*(a/2)**2 :.2f}')

#Bài 3
c = input()
if c.isupper():
    print(c.lower())
else: print(c.upper())

#Bài 4
c = input()
if ord(c) >= 65 and ord(c) <= 90:
    print('{c} là kí tự alphabet')
elif ord(c) >= 97 and ord(c) <= 122:
    print('{c} là kí tự alphabet') 
else: print('{c} không phải là kí tự alphabet')

#Bài 5
A = input()
if ord(A) > 65 and ord(A) <= 90:
    A = A.lower()
    print(chr( ord(A) - 1 ))
else: print('Kí tự không hợp lệ')

#Bài 6
a, b, c = map(int, input().split())
if a + b > c and a + c > b and b + c > a :
    p = ( a + b + c )/2
    s = (p*(p-a)*(p-b)*(p-c))**(1/2)
    print(f'{s:.1f}')
else: print('Không phải 3 cạnh của tam giác')

#Bài 7
s = input()
if len(s) >= 20:
    print(s[4], s[8])
else: 
    print('nhập chuỗi có độ dài >=20:')

#Bài 8
def ep(x):
    if x <= 50:
        n = 1984*x
        return n + n*0.08
    elif 51 <= x <= 100:
        n = 50*1984 + (x - 50)*2050
        return n + 0.08*n
    elif 101 <= x <= 200:
        n = 50*1984 + 50*2050 + (x - 100)*2380
        return n + 0.08*n
    elif 201 <= x <= 300:
        n = 50*1984 + 50*2050 + 50*2380 + (x - 150)*2998
        return n + 0.08*n
    elif 301 <= x <= 400:
        n = 50*1984 + 50*2050 + 50*2380 + 50*2998 + (x - 200)*3350
        return n + 0.08*n
    elif x >= 401:
        n = 50*1984 + 50*2050 + 50*2380 + 50*2998 + 50*3350 + (x-250)*3460
        return n + 0.08*n
    
a = input('Ten chu ho:')
b = int(input('Chi so thang trươc:'))
c = int(input('Chi so thang nay:'))
print('Ho va ten:', a)
print('Tien phai tra la:', int(ep(c - b)))

#Một số bài tập khác

#1
a = int(input())
if a % 2 ==0:
    print('La so chan')
else: print('La so le')

#2
n = int(input())
if n % 10 == 5:
    print('True')
else: print('False')

#3
n = int(input())
if n % 3 == 0 and n % 5 ==0:
    print('True')
else: print('False')

#4
t = int(input('Nhập năm sinh:'))
n = int(input('Nhập năm hiện tại:'))
if n - t >= 18:
    print('Đủ tuổi để đi bầu cử')
elif n - t < 0:
    print('Dữ liệu không hợp lệ')
else: print('Không đủ tuổi')

#5
a = float(input())
b = float(input())
if a == b:
    print('Hai số bằng nhau')
elif a < b:
    print(b)
else: print(a)

#6
char = input()
if 65 <= ord(char) <= 90:
    print('Là chữ cái')
elif 97 <= ord(char) <= 122:
    print('Là chữu cái')
elif 48 <= ord(char) <= 57:
    print('Là chữ số')
else: print('Không là chữ cái, cũng không là số')

#7
res = float(input())
if 8 <= res <=10:
    print('Giỏi')
elif 6.5 <= res < 8:
    print('Khá')
elif 5 <= res < 6.5:
    print('Trung Bình')
elif 0 <= res < 5:
    print('Yếu')
else:
    print('Điểm không hợp lệ')

#8
n = int(input())
if n % 400 == 0 and n % 100 != 0:
    print('Là năm nhuận')
elif n % 4 == 0 and n% 100 != 0:
    print('Là năm nhuận')
else:
    print('Không là năm nhuận')

#9
s = int(input())
while s < 0 or s >= 10:
    print('Không hợp lệ hãy nhập lại')
    s = int(input())
def kt(s):
    match s:
        case 0:
            return 'Không'
        case 1:
            return 'Một'
        case 2:
            return 'Hai'
        case 3:
            return 'Ba'
        case 4:
            return 'Bốn'
        case 5: 
            return 'Năm'
        case 6:
            return 'Sáu'
        case 7:
            return 'Bảy'
        case 8:
            return 'Tám'
        case 9:
            return 'Chín'
print(kt(s))

#10
res = float(input())
if res >= 4:
    print('Qua môn')
else: print('Học lại')

#11
n = int(input())
h = 2025
if n > h:
    print('Không hợp lệ')
elif h - n >= 18:
    print( h - n)
    print('Đã đủ 18 tuổi')
else: 
    print(h - n)
    print('Không đủ 18 tuổi')