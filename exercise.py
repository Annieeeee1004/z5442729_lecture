#Strings
tic = "QAN.AX"
print (tic)
str1 = 'One single quote one each side'
str2 = "double quote"
str3 = '''triple single quote''' #allows multiple lines, like text
str4 = """ triple double quote"""
# x = "<-- double quote but single quote -->' #确保首尾符号相同


# Multiple lines
str1 = '''This string can spend
more than one line'''
print (str1)
str2 = """ this string also can spend
more than one line"""
print (str2)


#Best way to compare floats,using isclose function
import math
f = 0.2 + 0.2 + 0.2
print(math.isclose(f,0.6))

#Booleans: A type for T/F
1==2
1==1

1==2 #true or false --> true


#Check the type of an object
i = 1
type(i)
f = 0.1
type(f)

#1.Adding two integers together
print(1+2)
#2.Adding two strings together
print('1'+'2')
#不同的class不可以plus，但可以multiply
'x'*2

f_suburbs = {"Randwick", "Kensington", "Frenchs Forest", "Flemington"}
f_suburbs.remove("Frenchs Forest")
f_suburbs.remove("Flemington")
print(f_suburbs)
f1 = {'Fairlight','Fairfield East','Frenchs Forest','Freshwater','Flemington','Five Dock','Freemans Reach','Fairfield','Fairfield West','Fiddletown','Forestville','Forest Lodge','Forest Glen','Fairfield Heights'}
f_suburbs = f1
print(f_suburbs)
'Fairfield','Fairfield East','Fairfield Heights','Fairfield West','Fairlight','Fiddletown','Five Dock',' Flemington','Forest Glen','Forestville','Freemans Reach','Frenchs Forest','Freshwater' in f_suburbs

lst_a = ['a']
lst_b = ['b', lst_a]
lst_c = ['b', ['a']]
lst_b[1].append("c")
print(lst_b[1]),(lst_a)

