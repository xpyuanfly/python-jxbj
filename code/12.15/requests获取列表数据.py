import requests  # 导入requests包
url = 'http://www.zzrcbank.cn/dibulanmu/gywh/'
headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }
res = requests.get(url,headers=headers) # Get方式获取网页数据
res.encoding='gbk'
print(res.text)
