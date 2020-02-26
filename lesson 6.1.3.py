from functools import reduce
def str2float(s):
    digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    integer,decimals = s.split('.')
    decimal_point = len(decimals)
    integer = reduce(lambda x,y:x*10+y,(map(lambda x:digit[x],integer)))
    decimals = reduce(lambda x,y:x*10+y,(map(lambda x:digit[x],decimals)))
    return integer+decimals/pow(10,decimal_point)


def make_str(x):
    dict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6}
    return dict[x]

def make_num(x,y):
    return x*10+y

def cut_float(f):
    return f.split('.')

def str2float(s):
    num = cut_float(s)
    num2_len = len(num[1])
    num1 = reduce(make_num , map(make_str , num[0]))
    num2 = reduce(make_num , map(make_str , num[1]))
    return num1 + num2*pow(0.1,num2_len)

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')