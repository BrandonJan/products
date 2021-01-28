products = []
while True:
    name = input("請輸入商品名稱:")
    if name == "q":
	    break
    price = input("請輸入商品價格:")
    p = []   #789行 = name = [name, price]
    p.append(name)
    p.append(price)
    products.append(p)  #更簡單的作法: products.append([name, price])
    pass
for p in products:
    print(p[0],"的價格為",p[1])