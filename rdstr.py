import random

# 随机n个字符的字符串，n可设定
base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'

candler: int = 12

str_list = [random.choice(base_str) for i in range(candler)]

print(''.join(str(s) for s in str_list))
