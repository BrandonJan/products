import os #operating system
products = []
if os.path.isfile("products.csv"):#檢查products.py這個檔案存取點附近有沒有這個products.csv檔案(相對路徑)
    with open ("C:\\Users\\Brandon\\Desktop\\products\\products.csv", "r", encoding = 'utf-8') as f:#讀取檔案
	    for line in f:
		    if "商品,價格" in line:
			    continue
		    name, price = line.strip().split(",") 
		    products.append([name, price])
		    print(products)
else:
	print("還未創建檔案喔")

#輸入清單
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
#印出所有購買紀錄
for p in products:
    print(p[0],"的價格為",p[1])
#寫入檔案
with open ("C:\\Users\\Brandon\\Desktop\\products\\products.csv", "w", encoding = 'utf-8') as f:
    f.write("商品,價格\n")
    for p in products:
        f.write(p[0] + "," + p[1] + "\n")