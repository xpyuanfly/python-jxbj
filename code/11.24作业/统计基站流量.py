''''
统计基站流量
以下是某个基站的日志记录（很小的一个片段而已）
1363157985066 	13726230503	00-FD-07-A4-72-B8:CMCC	120.196.100.82	i02.c.aliimg.com		24	27	2481	24681	200
1363154400022 	13826544101	5C-0E-8B-C7-F1-E0:CMCC	120.197.40.4			4	0	264	0	200
1363157991076 	13926435656	20-10-7A-28-CC-0A:CMCC	120.196.100.99			2	4	132	1512	200
1363154400022 	13826544101	5C-0E-8B-8B-B1-50:CMCC	120.197.40.4			4	0	240	0	200
1363157991076 	13926435656	94-71-AC-CD-E6-18:CMCC-EASY	120.196.100.99	iface.qiyi.com	视频网站	15	12	1527	2106	200
1363157985068 	13726230508	00-FD-07-A4-72-B8:CMCC	120.196.100.82	i02.c.aliimg.com		24	27	2482	24680	200
'''


class bean():
    def __init__(self, telno, upload, download):
        self.telno = telno
        self.upload = int(upload)
        self.download = int(download)
        self.totalload = int(upload)+int(download)

    def __add__(self, object):
        self.download += object.download
        self.upload += object.upload
        self.totalload += object.totalload
        return self

    def __lt__(self, object):
        if self.totalload != object.totalload:
            return self.totalload < object.totalload
        else:
            return self.download < object.download

    def __repr__(self):
        return "{},{},{},{}".format(self.telno, self.upload, self.download, self.totalload)


if __name__ == "__main__":
    string = '1363157985066 	13726230503	00-FD-07-A4-72-B8:CMCC	120.196.100.82	i02.c.aliimg.com		24	27	2481	24681	200\n\
1363154400022 	13826544101	5C-0E-8B-C7-F1-E0:CMCC	120.197.40.4			4	0	264	0	200\n\
1363157991076 	13926435656	20-10-7A-28-CC-0A:CMCC	120.196.100.99			2	4	132	1512	200\n\
1363154400022 	13826544101	5C-0E-8B-8B-B1-50:CMCC	120.197.40.4			4	0	240	0	200\n\
1363157991076 	13926435656	94-71-AC-CD-E6-18:CMCC-EASY	120.196.100.99	iface.qiyi.com	视频网站	15	12	1527	2106	200\n\
1363157985068 	13726230508	00-FD-07-A4-72-B8:CMCC	120.196.100.82	i02.c.aliimg.com		24	27	2482	24680	200'
    ls_row = string.split("\n")
    bean_dic = {}
    for row in ls_row:
        ls = row.split("\t")
        telno = ls[1]
        upload = ls[8]
        download = ls[9]
        if telno in bean_dic:
            bean_dic[telno] += bean(telno, upload, download)
        else:
            bean_dic[telno] = bean(telno, upload, download)
    print("result:")
    for bean in bean_dic.values():
        print(bean)
    
    sorted_ls = sorted(bean_dic.items(), key=lambda x: x[1], reverse=True)
    print("sorted result:")
    for key,value in sorted_ls:
        print(value)
