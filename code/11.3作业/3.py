password = 'ab3427.f'

low = 8
up = 16
'''
1.大写字母：A,B,C...Z;
2.小写字母：a,b,c...z;
3.数字：0,1,2...9;
4.特殊符号：~,!,@,#,$,%,^;

'''
ls = [
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'abcdefghijklmnopqrstuvwxyz',
    '0123456789',
    '~!@#$%^',
    
]


def fhtj(pattern):
    for p in password:
        if p in pattern:
            return True
    return False

# print(fhtj(ls[2]))


def isSecure():
    return low <= len(password) < up and sum(list(map(fhtj, ls))) >= 3


print(isSecure())
