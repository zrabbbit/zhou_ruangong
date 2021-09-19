import unittest

from 统计关键字个数4 import total_count
from 统计关键字个数4 import switch_count
from 统计关键字个数4 import if_elseif_else_count


class TotalCountTest(unittest.TestCase):
    # 用于测试 total_count 函数
    def test_file_str(self):
        fo = open("D:\\Code\\样例.c", "r")
        total_num = total_count(fo)
        fo.close()
        self.assertEqual(total_num, 35)  # add assertion here


class SwitchCountTest(unittest.TestCase):
    # 用于测试 switch_count 函数
    def test_file_str(self):
        fo = open("D:\\Code\\样例.c", "r")
        switch_num = switch_count(fo)
        fo.close()
        self.assertEqual(switch_num, 1)


class IfElseifCountTest(unittest.TestCase):
    # 用于测试 if_elseif_else 函数
    def test_file_str(self):
        fo = open("D:\\Code\\样例.c", "r")
        if_else_num = if_elseif_else_count(fo)
        fo.close()
        self.assertEqual(if_else_num, 2)


if __name__ == '__main__':
    unittest.main()
