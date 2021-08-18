import os
import datetime


today = datetime.date.today()
today = str(today)
filename = today + '.csv'

#在專案中建立「系統」
#檢查檔案是否存在，並讀取
products = []
if os.path.isfile(filename):
	print('檔案打開中...')
	with open(filename, 'r') as f:
		for line in f:
			if '商品, 價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, int(price)])
else:
	print('檔案不在，請重新檢查！')

today = datetime.date.today()
today = str(today)
filename = today + '.csv'

#讓使用者輸入，並且看到今日購買清單
while True:
	name = input('請輸入商品名稱:')
	if name == ' ':
		break
	price = input('請輸入商品價格:')
	price = int(price)
	products.append([name, price])
print(products)

#計算金額
price_sum = 0
for p in products:
	price_sum += p[1]
print('本月花費：', price_sum)

#寫入檔案
with open(filename, 'w', encoding = 'utf-8') as f:
	f.write('商品, 價格\n')
	for p in products: 
		f.write(p[0] + ',' + str(p[1]) + '\n')

