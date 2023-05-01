import re
string = "qwqe12vf4.5tr5"
res1 = re.findall('\d+\.\d*|\d+', string)
res2 = re.findall('\d+|\d+\.\d*', string)
res3 = re.findall('[A-Za-z]+', string)
print(res1)    # ['12', '4.5', '5']
print(res2)    # ['12', '4', '5', '5']
print(res3)    # ['qwqe', 'vf', 'tr']
