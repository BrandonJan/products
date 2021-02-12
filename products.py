import os #operating system
def read_file(filename):
    products = []
    with open (filename, "r", encoding = 'utf-8') as f:#讀取檔案
            for line in f:
                if "商品,價格" in line:
                    continue
                name, price = line.strip().split(",") 
                products.append([name, price])
    return products    
#輸入清單
def input_file(products):
    while True:
        name = input("請輸入商品名稱:")
        if name == "q":
            break
        price = input("請輸入商品價格:")
        p = []   #以下三行 = name = [name, price]
        p.append(name)
        p.append(price)
        products.append(p)  #更簡單的作法: products.append([name, price])
        pass
    return products        
#印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0],"的價格為",p[1])
#寫入檔案
def write_file(filename, products):
    with open (filename, "w", encoding = 'utf-8') as f:
        f.write("商品,價格\n")
        for p in products:
            f.write(p[0] + "," + p[1] + "\n")
def main():
    filename = "products.csv"
    if os.path.isfile(filename):#檢查products.py這個檔案存取點附近有沒有這個products.csv檔案(相對路徑)
        products = read_file(filename)
    else:
        print("還未創建檔案喔")
    products = input_file(products)
    print_products(products)
    write_file("products.csv", products)

main()