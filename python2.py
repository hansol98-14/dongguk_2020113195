# 2020113195 유한솔
# 예제2 가위바위보 랭킹 시스템

import random as rd
import operator

play_num=int(input('몇명이 가위바위보를 하나요? :'))
player_list=[]
for i in range(1,play_num+1):
    player_list.append(input('{}번째 플레이어의 이름을 입력하시오.'.format(i)))
print('현재 리그에 속한 플레이어 명단 : {} '.format(player_list))

def main_versece(player):
    a = {}
    pointer=[]
    for i in range(len(player)):
        for j in range(i+1,len(player)):
            ver=[]
            print('이번 경기는 {}와 {}의 싸움입니다'.format(player[i],player[j]))
            ver.append(player[i])
            ver.append(player[j])
            winer=ver.pop(rd.randrange(0,2))
            ver=ver[0]
            print('승자는 [{}](포인트+3)이고 패자는 [{}](포인트-3)입니다\n'.format(winer,ver))
            key = winer
            key_loser=ver
            value = 3
            if (key in a) :
                a[key]+=value
                if (key_loser in a):
                    if (a[key_loser]-value)<=0:pass
                    else:a[key_loser]-=value
                else:a[key_loser]=0
            else:a[key] = value
    return a

def ranking(ver_result):
    return (sorted(ver_result.items(), key=operator.itemgetter(1),reverse=True))

print(ranking(main_versece(player_list)))