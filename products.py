shop_list = []
while True:
    shop_name = input('請輸入商品名稱: ')
    if shop_name == 'q':
        break
    shop_price = input('請輸入商品價格: ')
    shop_list.append([shop_name,shop_price]) #在大清單加入小清單中的價格與物品
print(shop_list)