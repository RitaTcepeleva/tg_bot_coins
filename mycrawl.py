from bs4 import BeautifulSoup
import requests
import random

'''web_req = requests.get('https://www.coingecko.com/en/yield-farming/')
content = BeautifulSoup(web_req.text, 'html.parser')
assets = content.select('tbody  tr')

the_one = 'uniswap'   #asset which we look for
flength = len(the_one)
available = False
final_string = ''
for asset in assets:
    for i in range(len(asset.text)):
        chunk = asset.text[i:i+flength].lower()
        if chunk == the_one:
            available = True

    columns = asset.contents
    number = int(columns[1].text)
    name = str(columns[3].text)
    price = str(columns[11].text)
    for column in columns:
        cont = []
        if type(column) == 'bs4.element.Tag':
            cont.append(column.text)
    final_string += '{0}. {1} TVL {2}\n'.format(number,name,price)'''

def topfarms():
    web_req = requests.get('https://www.coingecko.com/en/yield-farming/')
    content = BeautifulSoup(web_req.text, 'html.parser')
    assets = content.select('tbody  tr')

    final_string = ''
    for asset in assets:
        if int(asset.contents[1].text) < 11:
            columns = asset.contents
            number = str(columns[1].text).strip()
            name = str(columns[3].text).strip()
            price = str(columns[11].text).strip()
            pool = str(columns[5].text).strip()
            prom = str(columns[13].text).strip()
            ret = prom.split("\n")[0]
            final_string += '\n{0}. Pool: {1}\n' \
                            'Asset: {2}\n' \
                            'Total Value Locked: {3}\n' \
                            'Returns: {4}\n'.format(number, pool, name, price, ret)

    return final_string

def degen():
    web_req = requests.get('https://www.coingecko.com/en/yield-farming/')
    content = BeautifulSoup(web_req.text, 'html.parser')
    assets = content.select('tbody  tr')
    final_string = ''
    for asset in assets:
        columns = asset.contents
        if str(columns[13].text) != '\n':
            prom = str(columns[13].text).strip()
            ret = float(prom.split("%")[0])
            if ret > 1000.0:
                number = str(columns[1].text).strip()
                name = str(columns[3].text).strip()
                price = str(columns[11].text).strip()
                pool = str(columns[5].text).strip()
                final_string += '\n{0}. Pool: {1}\n' \
                                'Asset: {2}\n' \
                                'Total Value Locked: {3}\n' \
                                'Returns: {4}% Yearly\n'.format(number, pool, name, price, str(ret))

    return final_string

def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in nums:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quicksort(s_nums) + e_nums + quicksort(m_nums)


def reorder_farm():
    web_req = requests.get('https://www.coingecko.com/en/yield-farming/')
    content = BeautifulSoup(web_req.content, 'html.parser')
    assets = content.select('tbody tr')
    ret_arr = []
    for asset in assets:
        columns = asset.contents
        if str(columns[13].text) != '\n':
            prom = str(columns[13].text).strip()
            ret = float(prom.split("%")[0])
            ret_arr.append(ret)
    data = quicksort(ret_arr)
    final_string = ''
    n = len(data) - 1
    while n > len(data) - 11:
        for asset in assets:
            columns = asset.contents
            if str(columns[13].text) != '\n':
                prom = str(columns[13].text).strip()
                ret = float(prom.split("%")[0])
            if ret == data[n]:
                number = str(columns[1].text).strip()
                name = str(columns[3].text).strip()
                price = str(columns[11].text).strip()
                pool = str(columns[5].text).strip()
                final_string += '\n{0}. Pool: {1}\n' \
                                'Asset: {2}\n' \
                                'Total Value Locked: {3}\n' \
                                'Returns: {4}% Yearly\n'.format(number, pool, name, price, ret)
                n -= 1

    return final_string


#print(reorder_farm())
