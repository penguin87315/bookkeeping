import os
import time

def read_file(filename):
	products = []
	with open(filename, 'r') as f:
			for line in f:
				if '商品, 價格' in line:
					continue
				name, price = line.strip().split(',')
				products.append([name, int(price)])
	return products


def user_input(products):
	while True:
		name = input('請輸入商品名稱:')
		if name == ' ':
			break
		price = input('請輸入商品價格:')
		price = int(price)
		products.append([name, price])
		decision = input('還要輸入下一筆嗎？(y/n)：')
		if decision == 'n':
			break
	print(products)
	return products

def count_money(products):
	price_sum = 0
	for p in products:
		price_sum += p[1]
	print('本月花費：', price_sum)

def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('商品, 價格\n')
		for p in products: 
			f.write(p[0] + ',' + str(p[1]) + '\n')


def main():
	today = input('請輸入今天日期：')
	filename = today + '.csv'
	if os.path.isfile(filename):
		if today + '.csv' == filename:
			print('檔案打開中...')
			products = read_file(filename)
	else:
		print('新的一天，重新開始建立')

	products = user_input(products)
	count_money(products)
	write_file(filename, products)

#程式進入點
main()