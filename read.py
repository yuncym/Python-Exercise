
data = [] #要塞資料的清單
count = 0 #每一千筆印一次


with open('reviews.txt', 'r') as f:
	for line in f: #因為每次都讀取一行
		data.append(line) #每一行都塞進去
		count += 1 
		if count % 1000 == 0: 
			print(len(data))  #每讀取一千筆, 印出

print('檔案讀取完畢, 總共有: ', len(data), '筆資料')

# 算平均長度
sum_len = 0
for d in data: 
	sum_len = sum_len + len(d)  #每讀一筆會算長度, 然後再加總
	#print(sum_len)

print('每筆留言平均長度為', sum_len/len(data))
