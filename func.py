

def add(x=1, y=1):
    #print(x + y)
    return x + y  #為了把function 的結果存下來

result = add()
print(result)


# function : 清單平均值
def average(numbers):
    # return = sum(numbers) / len(numbers) #總數除以清單長度 = 平均
    avg = sum(numbers) / len(numbers) #總數除以清單長度 = 平均
    return avg


# print(average([1,2,3]))
#a = average([1,2,3])
#print(a)

print(average([1,2,3]))
print(average([180,34,92]))


def wash(dry=False, water=8):
    print('加水', water, '分滿')
    print('加洗衣精')
    print('旋轉')
    if dry:
        print('烘衣')

wash(True)
wash(False)
#wash()
wash(water=100)

#def say_hi():#
#    print('hi!')

#say_hi()

#def add(x=0, y=0):  # 預設0
#    print(x+y)


#add(5,8)
#add(10,10)
#add()
#add(y=100, x=1)

