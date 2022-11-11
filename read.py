
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



new = []
#data 清單裡面每一筆每一筆叫出來, 每一個d 都是單獨留言
#d 是字串, data 是清單
for d in data: 
	if len(d) < 100:
		new.append(d) #如果長度小於一百, 將其裝入清單
print('一共有: ', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])


# 開始抓有good 的留言
#good = []
#for d in data: 
#	if 'good' in d:
#		good.append(d) #如果good 有在留言內, 就塞進清單

#'a' in 'abc' -> True
#'1' in 'abc' -> False

# 下面是快寫法
# for d in data 
good = [1 for d in data if 'good' in d]
print(good)

print('一共有: ', len(good), '筆留言提到good')
print(good[0])

# 'bad' in d 是個運算式 只有true & false 
bad = ['bad' in d for d in data]
print(bad)

#bad = []
#for d in data:
#	bad.append('bad' in d)


