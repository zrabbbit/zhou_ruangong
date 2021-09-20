import unittest

from 统计关键字个数5 import total_count
from 统计关键字个数5 import switch_count
from 统计关键字个数5 import if_elseif_else_count


class TotalCountTest(unittest.TestCase):
    # 用于测试 total_count 函数
    def test_file_str(self):
        fo = open("D:\\Code\\example.cpp", "r")
        total_num = total_count(fo)
        fo.close()
        self.assertEqual(total_num, 20)  # add assertion here


class SwitchCountTest(unittest.TestCase):
    # 用于测试 switch_count 函数
    def test_file_str(self):
        fo = open("D:\\Code\\example.cpp", "r")
        switch_num = switch_count(fo)
        fo.close()
        self.assertEqual(switch_num + 1, 1)


class IfElseifCountTest(unittest.TestCase):
    # 用于测试 if_elseif_else 函数
    def test_file_str(self):
        fo = open("D:\\Code\\example.cpp", "r")
        if_else_num = if_elseif_else_count(fo)
        fo.close()
        self.assertEqual(if_else_num, 1)


if __name__ == '__main__':
    unittest.main()
