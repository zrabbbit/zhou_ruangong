import re

# 输入一个文件路径
code_path = input()

# 输入等级
level = input()

# 打开文件并转换成字符串
fo = open(code_path, "r")
str1 = fo.read()
print(str1)

# 用多个分隔符分割每个单词
str12 = re.split(r"[;,?\n{}() <>:\t]", str1)
print(str12)
str2 = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default',
        'do', 'double', 'else', 'enum', 'extern', 'float', 'for', 'goto',
        'if', 'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof',
        'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void',
        'volatile', 'while']
keywords_sum = 0
for x in str12:
    if x in str2:
        keywords_sum += 1
        print(x)
print("total num:", keywords_sum)
