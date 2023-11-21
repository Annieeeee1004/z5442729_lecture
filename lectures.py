#yfinance.download(tic,start,end)
x = 'abc'
upper(x) #upper is not a build-in function
#1.
a = str.upper(x)
print(a)
#2.
y = 'abc'.upper()
print(y)

b = str.lower(a)
print(b)
x = "ABC".lower()
print(x)


c = 'sudAdhYSBJdin'.upper()
print(c)

'_'.join(('welcome', 'to', 'stack', 'overflow'))

string = "Good Morning"
new_string = string.replace("Good", "Great")

print(new_string)

str='milk chicken food'
print(str.split()) #()中是断开的地方,也可以是数字代表在第几位断开
str1='123456'
print(str1.split("2",3))

#1.width
#center the word 'Hi' in a line of 40 Characters
"Hi".center(40,'-')

#2.,filllchar
a = True
b = 5
print(f'The value of a is {b} and the result is {a}')
print('the value of a is {} and the result is {},'.format(b,a))

asx_value = 7111.4
date = '2021-01-25'
units = 1
currency = 'AUD'
print(f'the closing value of {units} units of the All Ordinaries on {date} was {asx_value} {currency}.')

dic0 = {'a':1, 'b':2, 'c':3}
dic1 = dic0.update({'a':0, 'd':4})
print(dic0[0])

