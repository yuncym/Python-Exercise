# range 是清單產生器
# range 通常會跟for loop 搭配, 主要目的是執行某個"固定次數"

import random

range(5)         # [0, 1, 2, 3, 4]
range(3)         # [0, 1, 2]
range(2, 5)      # [2, 3, 4] 
range(8, 10)     # [8, 9]
range(2, 10, 3)  # [2, 5, 8]  #3 是遞增值
range(3, 8, 2)   # [3, 5, 7]
range(10, 3, -2) # [10, 8, 6, 4]
  


for i in range(3):
	#print(i) #出現0,1,2
	r = random.randint(1,100)
	#print('hi') #出現hi, hi , hi
	print('這是第', 1+i, '次產生隨機數: ', r)
