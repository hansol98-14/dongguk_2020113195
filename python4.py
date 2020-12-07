# 2020113195 유한솔
# 예제4 메모리공간을 동적으로 사용해 데이터 관리하기

갯수 = int(input("입력할 정수 갯수를 적으세요 > "))
sum = 0

for i in range(갯수):
    j = int(input(str(i)+"번 정수 > "))
    sum += j

avg = sum/int(갯수)

print("합계 = ",sum)
print("평균 = ",avg)

del sum, avg, 갯수