# 2020113195 유한솔
# 예제3 (어벤져스)타노스의 핑거스냅

import random

List = [1, 2, 3, 4, 5, 6, 7]
ite = 0
if len(List)//2 == len(List)/2: ite = len(List)/2
else: ite = len(List)//2 + random.randint(0, 1)

for a in range(int(ite)):
    List.pop(random.randint(0, len(List)-1))
    
print(List)