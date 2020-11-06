# Q：【编程】编写一个程序，输入为一个人的身份证号码，判断此人是否成年？
# 很多同学 算年龄的逻辑 没有理清楚
import datetime
dt = datetime.datetime.now()

brith_date = input("请输入身份证号码：")
brith_year = int(brith_date[6:10])
brith_month = int(brith_date[10:12])
brith_day = int(brith_date[12:14])

if dt.month < brith_month:
	age = dt.year - brith_year
elif dt.month == brith_month:
	if dt.day <= brith_day:
		age = dt.year - brith_year
	else:
		age = dt.year - brith_year-1
else:
	age = age = dt.year - brith_year-1

if(age>=18):
	print("已成年！")
else:
	print("未成年！")

# 另外一种思路是：把此人出生年份+18，然后拼接，转成整型，与今天年月日整型比较
import datetime
dt = datetime.datetime.now()
today_int = int(str(dt.year)+str(dt.month)+str(dt.day))
brith_date = input("Enter your id number:")
brith_add18 = int(brith_date[6:10])+18
brith_int = int(str(brith_add18)+str(brith_date[10:14]))
if(brith_int > today_int):
	print("已成年！")
else:
	print("未成年！")

# Q：闰年问题
# 很多同学条件写错了
year = input("请输入年份：")
year = int(year)
if (year%4==0 and year%100!=0) or (year%400==0):
	print("是闰年！")
else:
	print("不是闰年！")
