
products = []

while True: 
	name = input('請輸入商品名稱: ')
	if name == 'q':  
		break
	price = input('請輸入商品價格: ')
	p = []
	# p.append(name)
	# p.append(price)
	p = [name, price]  # 這可以取代上面兩行
	products.append(p)

print(products)  # 印出有多少商品

print(products[0][0])
print(products[0][1])


