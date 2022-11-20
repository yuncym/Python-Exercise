def wash(dry=False, water=8):
    print('加水', water, '分滿')
    print('加洗衣精')
    print('旋轉')
    if dry:
        print('烘衣')

wash(True)
wash(False)
wash()
wash(water=100)

def say_hi():
    print('hi!')

#say_hi()

def add(x=0, y=0):  # 預設0
    print(x+y)


add(5,8)
add(10,10)
add()
add(y=100, x=1)

