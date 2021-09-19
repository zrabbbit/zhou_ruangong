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
switch_case_num = -1
case_list = list()
for x in str12:
    if x in str2:
        keywords_sum += 1
        print(x)
    if x == 'switch':
        switch_case_num += 1
        case_list.append(0)
    if x == 'case':
        scn = switch_case_num
        t = case_list[switch_case_num]
        t += 1
        case_list[switch_case_num] = t

print("total num:", keywords_sum)
print("switch num:", switch_case_num+1)
print("case num:", end=' ')
i = 0
while i <= switch_case_num:
    # 输出每个switch中的case个数
    print(case_list[i], end=' ')
    i += 1
