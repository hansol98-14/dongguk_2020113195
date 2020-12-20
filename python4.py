# 2020113195 유한솔
# 예제4 가위바위보 게임

import random

game = ['가위', '바위', '보']
chk = input('가위, 바위, 보 중 골라주세요')
com = game[random.randint(0,2)]

print(chk)
print(com)

vs = game.index(chk) - game.index(com)
if vs == 1 or vs == -2:
    print('이겼어요!')
elif vs == -1 or vs == 2:
    print('졌어요ㅜ.ㅜ')
elif vs == 0:
    print('비겼어요~')