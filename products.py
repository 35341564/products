shop_list = []

with open('products.csv','r',encoding='utf-8')as f:
    for line in f:
        if '商品,價格' in line:
            continue #跳到下一迴圈，不會跳出
        name,price = line.strip().split(',')
        shop_list.append([name,price])
print(shop_list)

while True:
    shop_name = input('請輸入商品名稱: ')
    if shop_name == 'q':
        break
    shop_price = input('請輸入商品價格: ')
    shop_list.append([shop_name,shop_price]) #在大清單加入小清單中的價格與物品
print(shop_list)

for p in shop_list:
    print(p[0],'的價格為:',p[1])

with open('products.csv','w',encoding='utf-8')as f:
    f.write('商品,價格\n')
    for p in shop_list:
        f.write(p[0] + ',' + str(p[1] + '\n'))
