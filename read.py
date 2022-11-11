
data = [] #要塞資料的清單
count = 0 #每一千筆印一次

with open('reviews.txt', 'r') as f:
	for line in f: #因為每次都讀取一行
		data.append(line) #每一行都塞進去
		count += 1 
		if count % 1000 == 0:
			print(len(data))
print(len(data))   #可知道有幾筆資料	

print(data[0])
print('--------------------------')
print(data[1])
