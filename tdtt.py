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
