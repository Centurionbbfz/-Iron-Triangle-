Python 3.8.3rc1 (tags/v3.8.3rc1:802eb67, Apr 29 2020, 21:39:14) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Python 3.8.3rc1 (tags/v3.8.3rc1:802eb67, Apr 29 2020, 21:39:14) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> #其他数学运算符，比如幂（“**”），除号（取商“//”），取余数（“%”）
>>> 2**5
32
>>> 9**（1/2)
  File "<stdin>", line 1
    9**（1/2)
        ^
SyntaxError: invalid character in identifier
>>> #额，上边的bug是由于符号的英汉问题
>>> 9**(1/2)
3.0
>>> #一个数的1/2次方就是这个数的开二次根号
>>> 20//6
3
>>> 1.25
1.25
>>> 7%(5//2)
1
>>> #字符串：单、双引号中加上文本
>>> #字符串转义：单、双引号中不能有引号，如果有则必须要在串中的引号前加上"\",进行转义。此外，\n还表示换行，\t表示制表符 （即Tab键）
>>> "He \ 's a very naughty boy."
"He \\ 's a very naughty boy."
>>> #What?再来一次
>>> "He\'s a very naughty boy."
"He's a very naughty boy."
>>> #运行成功！这说明转义符前后不能加空格
>>> "Wan\tZisheng is very\nclever.
  File "<stdin>", line 1
    "Wan\tZisheng is very\nclever.
                                 ^
SyntaxError: EOL while scanning string literal
>>> #啊啊啊啊啊啊，我忘加括号了
>>> "Wan\tZisheng is very\nclever."
'Wan\tZisheng is very\nclever.'
>>> print("Wan\tZisheng is very\nclever.")
Wan     Zisheng is very
clever.
>>> #三个单引号中换行的字符串运行后自动合为一行并加上\n
>>> '''Wan Zisheng
... is very clever.'''
'Wan Zisheng\nis very clever.'
>>> #输入与输出
>>> #print（）就是一个函数
>>> print("print("print")")
  File "<stdin>", line 1
    print("print("print")")
                  ^
SyntaxError: invalid syntax
>>> print("print('print')")
print('print')
>>> #一行代码中不能出现两个双引号或两个单引号
>>> #input函数
>>> #input("字符串")
>>> #字符串输入各种类型的数
>>> #输出
>>> input("a")
a"wzs"
'"wzs"'
>>> input("a")
awzs
'wzs'
>>> input("a")
a13503871089
'13503871089'
>>> #字符串连接（就像做加法）
>>> "番茄"+"鸡蛋"
'番茄鸡蛋'
>>> #注意：只能用于字符串，不能用于数字↓
>>> 1+"2"+3+"4"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> #字符串可以与数字相乘，重复字符串
>>> 'spam'*3
'spamspamspam'
>>> '2'*4
'2222'
SyntaxError: invalid syntax
>>> 