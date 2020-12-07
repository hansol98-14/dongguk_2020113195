# 2020113195 유한솔
# 예제5 메모리공간을 동적으로 사용해 데이터 관리하기

def lcd_disp(size, num_str):
    _map = [
        '1011010111',
        '1000111111',
        '1111100111',
        '0011111011',
        '1010001010',
        '1101111111',
        '1011011010'
    ]

    def _horizon(key):
        prt = [' ', '-']
        for x in num_str:
            print (' {} '.format(prt[int(_map[key][int(x)])] * size), end=' ')
        print('')

    def _vertical(key1, key2):
        prt = [' ', '|']        
        for i in range(size):
            for x in num_str: 
                print ('{}{}{}'.format(prt[int(_map[key1][int(x)])]
                                       ,' ' * size
                                       ,prt[int(_map[key2][int(x)])]),
                       end=' ')
            print('')

    _horizon(0)      #   -
    _vertical(1, 2)  # |   |
    _horizon(3)      #   -
    _vertical(4, 5)  # |   |
    _horizon(6)      #   -

lcd_disp(2, '12345')
lcd_disp(3, '67891')