# -*- coding: utf-8 -*-
"""
Created on Fri May 12 14:20:49 2023

@author: 蒋明涛
"""

class Student:
    def __init__(self, sno, name='', english=0, math=0):
        self.sno = sno
        self.name = name
        self.__english = english if 0 <= english <= 100 else 0
        self.__math = math if 0 <= math <= 100 else 0

    @property
    def english(self):
        return self.__english

    @english.setter
    def english(self, english):
        self.__english = english if 0 <= english <= 100 else 0

    @property
    def math(self):
        return self.__math

    @math.setter
    def math(self, math):
        self.__math = math if 0 <= math <= 100 else 0

# 得到成绩的平均分
    def get_average(self):
        return (self.english + self.math) / 2
    
# 格式化输出student的属性
    def __str__(self):
        return str.format('{0:>4d}{1:\u3000>5s}{2:>7d}{3:>7d}', self.sno, self.name, self.english, self.math)

# 格式化输出"'学号', '姓名', '英语', '数学'"字符串
    @staticmethod
    def get_header():
        return '{0:>s}{1:\u3000>5s}{2:\u3000>5s}{3:\u3000>4s}'.format('学号', '姓名', '英语', '数学')


#定义方法，使按学号依次排序
    def __gt__(self, other):
        return self.sno > other.sno

    def __eq__(self, other):
        return self.sno == other

    def __ge__(self, other):
        return self.sno >= other.sno


# 测试代码:
    
# if __name__ == "__main__":
#     s = [Student(1, '王大海', 100, 35), Student(2, '小李', 57, 82), Student(3, '赵四', 81, 44)]
#     a = sorted(s)
#     print(Student.get_header())
#     for e in a:
#         print(e)

#     s1 = Student(11, 'Li', 80, 88 )
#     print('{0}的平均成绩为{1}'.format(s1.name,s1.get_average()))
#     print(s[0] <= s[1])