#W1A1
a = 7
b = 5
c = a + b
print(c)

#Giải thích từng dòng:
#a = 7

#Gán giá trị 7 cho biến a.

#b = 5

#Gán giá trị 5 cho biến b.

#c = a + b

#Tính tổng của a và b, tức là 7 + 5 = 12.

#Gán kết quả này cho biến c.

#print(c)

#In ra giá trị của biến c, tức là 12.

#✅ Kết quả khi chạy code:
#Kết quả in ra màn hình sẽ là:

#Sao chép mã
#12
#🖥️ Thử chạy code thực tế:
#👉 Đúng như dự đoán, đoạn code đã in ra 12.
#Lý do: vì a = 7, b = 5, nên c = 7 + 5 = 12, sau đó print(c) in ra kết quả này. '''


#W1A2
city = "Hà Nội" 
year = "2025"     
print("Thàn phố", city , "-Năm", year)
ngay = 16
thang = 9
nam = 2025
print (ngay, thang, nam, sep = "/")
# Giải thích từng dòng:
#city = "Hà Nội"

#Tạo một biến tên là city và gán giá trị chuỗi "Hà Nội" cho nó.

#year = "2025"

#Tạo biến year và gán giá trị chuỗi "2025" cho nó.

#print("Thàn phố", city , "-Năm", year)

#Lệnh print sẽ in ra các giá trị được ngăn cách bởi dấu cách mặc định.

#Ở đây in ra: "Thàn phố Hà Nội -Năm 2025".

#Lưu ý: Trong code của bạn viết "Thàn phố" (thiếu chữ h → đúng ra là "Thành phố").

#ngay = 16

#Gán số nguyên 16 cho biến ngay.

#thang = 9

#Gán số nguyên 9 cho biến thang.

#nam = 2025

#Gán số nguyên 2025 cho biến nam.

#print (ngay, thang, nam, sep = "/")

#In ra ba giá trị ngay, thang, nam.

#Nhờ tham số sep="/" nên các giá trị sẽ được ngăn cách bằng dấu / thay vì khoảng trắng mặc định.

#Kết quả: 16/9/2025.

#✅ Kết quả mong đợi khi chạy code:
#css
#Sao chép mã
#Thàn phố Hà Nội -Năm 2025
#16/9/2025
#🖥️ Thực thi code để kiểm chứng:
#👉 Kết quả chạy thực tế trùng khớp với phân tích:

#css
#Sao chép mã
#Thàn phố Hà Nội -Năm 2025
#16/9/2025
#✔️ Dòng đầu in ra thông tin thành phố và năm.
#✔️ Dòng sau in ra ngày/tháng/năm theo định dạng dd/mm/yyyy. '''

#W1A3 TH1
n = 4 
t = 0
for i in range (1, n+1):
    t += i
print(t)
#Giải thích từng dòng:
#n = 4

#Gán số nguyên 4 cho biến n. Đây là giới hạn trên để tính tổng.

#t = 0

#Tạo biến t và gán giá trị ban đầu là 0. Biến này dùng để lưu tổng các số.

#for i in range (1, n+1):

#Vòng lặp for sẽ chạy với i từ 1 đến n (bao gồm cả n, vì range(1, n+1) sẽ tạo dãy [1, 2, 3, 4]).

#t += i

#Mỗi lần lặp, cộng giá trị i vào t.

#Quá trình:

#Lặp 1: i = 1 → t = 0 + 1 = 1

#Lặp 2: i = 2 → t = 1 + 2 = 3

#Lặp 3: i = 3 → t = 3 + 3 = 6

#Lặp 4: i = 4 → t = 6 + 4 = 10

#print(t)

#In ra giá trị cuối cùng của t.

#✅ Kết quả mong đợi:
#Sao chép mã
#10
#🖥️ Thực thi code để kiểm chứng:
#👉 Kết quả chạy thực tế là 10, đúng như phân tích.

#📌 Giải thích ngắn gọn: Đoạn code trên tính tổng các số nguyên từ 1 đến n (ở đây n = 4), tức là 
#1
#+
#2
#+
#3
#+
#4
#=
#10
#1+2+3+4=10 ''' 

#w1A3 TH2
n = 4 
t = 0
for i in range (1, n+1):
    t += i
    print(t) 

# Giải thích từng dòng:
#n = 4

#Gán giá trị 4 cho biến n. Đây là số cuối cùng trong dãy mà ta sẽ cộng dồn.


#t = 0

#Khởi tạo biến t bằng 0. Đây sẽ là biến lưu tổng lũy tiến.

#for i in range (1, n+1):

#Vòng lặp chạy với i lần lượt từ 1 đến 4 (vì range(1, n+1) tạo ra [1, 2, 3, 4]).

#t += i

#Mỗi vòng lặp, cộng i vào t (tức là t = t + i).

#print(t)

#In giá trị của t ngay trong từng vòng lặp, nên ta sẽ thấy kết quả từng bước cộng dồn.

#📊 Quá trình tính toán:
#Lặp 1: i = 1 → t = 0 + 1 = 1 → in ra 1

#Lặp 2: i = 2 → t = 1 + 2 = 3 → in ra 3

#Lặp 3: i = 3 → t = 3 + 3 = 6 → in ra 6

#Lặp 4: i = 4 → t = 6 + 4 = 10 → in ra 10

#✅ Kết quả mong đợi khi chạy code:
#Sao chép mã
#1
#3
#6
#10
#🖥️ Thực thi code để kiểm chứng:
#It seems like I can’t do more advanced data analysis right now. Please try again later.

#Tuy nhiên, theo phân tích chi tiết ở trên thì khi chạy đoạn code bạn đưa ra, kết quả in ra màn hình sẽ là:

#Sao chép mã
#1
#3
#6
#10
#📌 Lý do: mỗi lần lặp vòng for, biến t được cộng dồn thêm giá trị i và được in ngay sau đó. Vì thế bạn nhìn thấy các bước cộng dồn lần lượt:

#Sau vòng 1: 1

#Sau vòng 2: 3

#Sau vòng 3: 6

#Sau vòng 4: 10 '''

#W1A4
numbers = [1, 2, 3, 4]
for x in numbers:
    if x % 2 == 0:
        print(x, 'là số chẵn')
    else:
        print(x, 'là số lẻ')

# Giải thích từng dòng:
#numbers = [1, 2, 3, 4]

#Tạo một danh sách (list) chứa các số nguyên [1, 2, 3, 4].

#for x in numbers:

#Vòng lặp for sẽ duyệt lần lượt từng phần tử trong danh sách numbers.

#Như vậy x sẽ lần lượt nhận giá trị 1, 2, 3, 4.

#if x % 2 == 0:

#Toán tử % là chia lấy dư.

#Nếu x % 2 == 0 tức là x chia hết cho 2 → số chẵn.

#print(x, 'là số chẵn')

#Nếu điều kiện đúng thì in ra số đó kèm chuỗi "là số chẵn".

#else:

#Nếu không chia hết cho 2 thì rơi vào nhánh này (nghĩa là số lẻ).

#print(x, 'là số lẻ')

#In ra số đó kèm chuỗi "là số lẻ".

#📊 Quá trình chạy:
#Với x = 1: 1 % 2 = 1 ≠ 0 → in: 1 là số lẻ

#Với x = 2: 2 % 2 = 0 → in: 2 là số chẵn

#Với x = 3: 3 % 2 = 1 ≠ 0 → in: 3 là số lẻ

#Với x = 4: 4 % 2 = 0 → in: 4 là số chẵn

#✅ Kết quả in ra:
#Sao chép mã
#1 là số lẻ
#2 là số chẵn
#3 là số lẻ
#4 là số chẵn


#W1A5
animals = ['cat', 'dog', 'cat', 'bird']
count = 0
for a in animals:
    count += 1
print('Số phần tử trong danh sách là:', count)

#Giải thích từng dòng:

#Đây chỉ là chú thích (comment) để ghi chú, không ảnh hưởng đến chương trình.

#animals = ['cat', 'dog', 'cat', 'bird']

#Tạo một danh sách (list) tên animals gồm 4 phần tử: 'cat', 'dog', 'cat', 'bird'.

#Lưu ý: 'cat' xuất hiện 2 lần.

#count = 0

#Khởi tạo biến count bằng 0, dùng để đếm số phần tử trong danh sách.

#for a in animals:

#Vòng lặp for sẽ duyệt lần lượt từng phần tử trong danh sách animals.

#Biến a sẽ lần lượt nhận 'cat', 'dog', 'cat', 'bird'.

#count += 1

#Mỗi lần lặp, cộng thêm 1 vào count.

#Như vậy, sau 4 vòng lặp thì count sẽ tăng từ 0 → 4.

#print('Số phần tử trong danh sách là:', count)

#In ra thông báo kèm theo giá trị cuối cùng của count.

#📊 Quá trình chạy:
#Bắt đầu: count = 0

#Lặp 1: gặp 'cat' → count = 1

#Lặp 2: gặp 'dog' → count = 2

#Lặp 3: gặp 'cat' → count = 3

#Lặp 4: gặp 'bird' → count = 4

#✅ Kết quả in ra:
#Sao chép mã
#Số phần tử trong danh sách là: 4
#👉 Như vậy, đoạn code trên đếm số phần tử trong danh sách animals (không phân biệt trùng hay không). '''

#W1A6 đề bải ??

#W1A7 Đã sửa lỗi của đề bài (thiếu int or float)
num = int(input('Nhập số:'))
if num % 2 ==0:
    print('Số chẵn')
else:
    print('Số lẻ')

#W1A8
for i in range(3):
    print('AI đang học lần', i + 1)
print('Huấn luyện xong')

#Giải thích từng dòng:
#for i in range(3):

#Vòng lặp for chạy với i lần lượt nhận các giá trị 0, 1, 2 (vì range(3) tạo ra dãy [0, 1, 2]).

#print('AI đang học lần', i + 1)

#Trong mỗi vòng lặp, chương trình in ra chuỗi "AI đang học lần" và giá trị i + 1.

#Vì i bắt đầu từ 0 nên ta cộng thêm 1 để in lần học từ 1 → 3 thay vì 0 → 2.

#print('Huấn luyện xong')

#Sau khi kết thúc vòng lặp, in ra thông báo "Huấn luyện xong".

#📊 Quá trình chạy:
#Vòng 1: i = 0 → in: AI đang học lần 1

#Vòng 2: i = 1 → in: AI đang học lần 2

#Vòng 3: i = 2 → in: AI đang học lần 3

#Kết thúc vòng lặp → in thêm: Huấn luyện xong

#✅ Kết quả in ra:
#r
#Sao chép mã
#AI đang học lần 1
#AI đang học lần 2
#AI đang học lần 3
#Huấn luyện xong
#👉 Như vậy, đoạn code này mô phỏng quá trình AI được huấn luyện 3 lần, sau đó in ra thông báo hoàn thành. '''

#W1A9
for x in ['cat', 'dog', 'fish']:
    print('Dự đoán con vật:', x)

#Giải thích:
# for x in ['cat', 'dog', 'fish']:

#Vòng lặp for sẽ duyệt qua từng phần tử trong danh sách ['cat', 'dog', 'fish'].

#Như vậy, biến x lần lượt nhận giá trị 'cat', 'dog', 'fish'.

#print('Dự đoán con vật:', x)

#Mỗi lần lặp, chương trình in ra chuỗi "Dự đoán con vật:" kèm theo giá trị hiện tại của x.

#📊 Quá trình chạy:
#Lặp 1: x = 'cat' → in: Dự đoán con vật: cat

#Lặp 2: x = 'dog' → in: Dự đoán con vật: dog

#Lặp 3: x = 'fish' → in: Dự đoán con vật: fish

#✅ Kết quả in ra (3 dòng):
#mathematica
#Sao chép mã
#Dự đoán con vật: cat
#Dự đoán con vật: dog
#Dự đoán con vật: fish
#👉 Vậy đoạn code in ra 3 dòng, mỗi dòng ứng với một phần tử trong danh sách. '''

#W1A10 (Đã sửa lỗi cú pháp)
print('===AI Prediction System===')
print('1 Senntiment Analysis')
print('2 Weather forecast')
print('3 Exit')
print('Please choose an option:')