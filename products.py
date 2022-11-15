
products = []

while True: 
	name = input('請輸入商品名稱: ')
	if name == 'q':  
		break
	price = int(input('請輸入商品價格: '))
	p = []
	# p.append(name)
	# p.append(price)
	#p = [name, price]  # 這可以取代上面兩行
	#products.append(p)
	products.append([name, price])

print(products)  # 印出有多少商品

for p in products:
	#print(p)
    print(p[0], '的價格是', p[1], '元')

#print(products[0][0])
#print(products[0][1])
# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

with open('products.csv', 'w', encoding = 'utf-8') as f:  # 提示要用共通的utf-8 編碼
	f.write('商品, 價格\n') # 寫入欄位名稱
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')



