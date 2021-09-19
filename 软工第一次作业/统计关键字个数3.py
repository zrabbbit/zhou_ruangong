import re


def total_count(str1):
    # 实现对 32 个关键字的总数统计和对 switch 的个数统计和每个 switch 所包含的 case 数统计
    # 以非字母的字符作为分隔符切分字符串
    file_str_list = re.split(r'[^a-zA-Z]+', str1)
    str2 = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default',
            'do', 'double', 'else', 'enum', 'extern', 'float', 'for', 'goto',
            'if', 'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof',
            'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void',
            'volatile', 'while']
    total_num = 0
    switch_num = -1
    case_num = list()
    for x in file_str_list:
        if x in str2:
            total_num += 1
        if x == 'switch':
            switch_num += 1
            case_num.append(0)
        if x == 'case':
            t = case_num.pop()
            t += 1
            case_num.append(t)
    print("total num:", total_num)
    print("switch num:", switch_num + 1)
    print("case num:", end=' ')
    i = 0
    while i <= switch_num:
        print(case_num[i], end=' ')
        i += 1


def if_elseif_else_count(str1):
    # 实现 if-else 组的个数统计和 if-elseif-else 组的个数统计
    if_elseif_else_num = 0
    if_else_num = 0
    if_list = list()  # 1:if  2:else if
    i = 0
    while i < len(str1):
        if str1[i] == 'i':
            if i + 1 < len(str1) and str1[i + 1] == 'f':
                if_list.append(1)
                i += 2
            else:
                i += 1
        elif str1[i] == 'e':
            if i + 6 < len(str1) and str1[i:i + 7] == 'else if':
                if_list.append(2)
                i += 7
            elif i + 3 < len(str1) and str1[i:i + 4] == 'else':
                if if_list[-1] != 1:
                    if_elseif_else_num += 1
                else:
                    if_else_num += 1
                while if_list[-1] != 1:
                    if_list.pop()
                if_list.pop()
                i += 4
            else:
                i += 1
        else:
            i += 1
    print("if-else num:", if_else_num)
    print("if-elseif-else num:", if_elseif_else_num)


# 输入一个c/c++文件路径和等级
code_path, level = map(str, input().split())
# 打开文件并去除注释和字符串
rule = "(/\\*\\*/)|(/\\*[\\s\\S]*?\\*/)|(//[\\s\\S]*?\n)|(\"[\\s\\S]*?\")"
fo = open(code_path, "r")
file_str: str = fo.read()
file_str = re.sub(rule, "", file_str)
total_count(file_str)
print()
if_elseif_else_count(file_str)
