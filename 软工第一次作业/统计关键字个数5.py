import re

str2 = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default',
        'do', 'double', 'else', 'enum', 'extern', 'float', 'for', 'goto',
        'if', 'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof',
        'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void',
        'volatile', 'while'
        ]
rule = "(/\\*\\*/)|(/\\*[\\s\\S]*?\\*/)|(//[\\s\\S]*?\n)|(\"[\\s\\S]*?\")"


def total_count(file):
    # 实现对 32 个关键字的总数统计
    # 打开文件并去除注释和字符串
    file_str: str = file.read()
    file_str = re.sub(rule, "", file_str)
    # 以非字母的字符作为分隔符切分字符串
    file_str_list = re.split(r'[^a-zA-Z]+', file_str)
    total_sum = 0
    for x in file_str_list:
        if x in str2:
            total_sum += 1
    return total_sum


def switch_count(file):
    # 实现 switch 组的个数统计
    file_str: str = file.read()
    file_str = re.sub(rule, "", file_str)
    file_str_list = re.split(r'[^a-zA-Z]+', file_str)
    switch_sum = -1
    case_list = list()
    for x in file_str_list:
        if x == 'switch':
            switch_sum += 1
            case_list.append(0)
        if x == 'case':
            t = case_list.pop()
            t += 1
            case_list.append(t)
    print("switch num:", switch_sum + 1)
    print("case num:", end=' ')
    i = 0
    while i <= switch_sum:
        print(case_list[i], end=' ')
        i += 1
    return switch_sum


def if_elseif_else_count(file):
    # 实现 if-else 组的个数统计和 if-elseif-else 组的个数统计
    file_str: str = file.read()
    file_str = re.sub(rule, "", file_str)
    if_elseif_else_num = 0
    if_else_num = 0
    if_list = list()  # 1:if  2:else if
    i = 0
    while i < len(file_str):
        if file_str[i] == 'i':
            if i + 1 < len(file_str) and file_str[i + 1] == 'f':
                if_list.append(1)
                i += 2
            else:
                i += 1
        elif file_str[i] == 'e':
            if i + 6 < len(file_str) and file_str[i:i + 7] == 'else if':
                if_list.append(2)
                i += 7
            elif i + 3 < len(file_str) and file_str[i:i + 4] == 'else':
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
        elif file_str[i] == '{':
            if_list.append('{')
            i += 1
        elif file_str[i] == '}':
            while if_list[-1] != '{':
                if_list.pop()
            if_list.pop()
            i += 1
        else:
            i += 1
    print("if-else num:", if_else_num)
    print("if-elseif-else num:", if_elseif_else_num)
    return if_else_num


# 输入一个c/c++文件路径和等级
code_path, level = map(str, input().split())
if code_path.endswith(".c") or code_path.endswith(".cpp"):
    fo = open(code_path, "r")
    total_num = total_count(fo)
    print("total num:", total_num)
    fo = open(code_path, "r")
    switch_count(fo)
    fo = open(code_path, "r")
    print()
    if_elseif_else_count(fo)
    fo.close()
else:
    print("Error：输入的文件格式不对")
