# -*- coding: utf-8 -*-
"""
Created on Fri May 12 14:20:49 2023

@author: 蒋明涛
"""

from student import Student


# 创建'班级'类
class BanJi:
# 类的实例的初始化
    def __init__(self, name):
        self.name = name
        self.students = []
        self.load_data()

#定义方法
        
# 加载数据文件
    def load_data(self):
        with open('data.txt', encoding = 'utf-8') as f:
            for line in f:
                d = line.split()
                self.students.append(Student(int(d[0]), d[1], int(d[2]), int(d[3])))

# 浏览学生成绩
    def show_student(self):
        print(Student.get_header())
        for s in self.students:
            print(s)
            
# 添加学生成绩
    def add_student(self, student):
        if student in self.students:
            return '学生已存在！'
        else:
            self.students.append(student)
            return '添加成功。'
        
# 浏览学生成绩
    def __index_student(self, sno):
        s = Student(sno)
        try:
            i = self.students.index(s)
        except ValueError:
            i = None
        return i
    
# 浏览学生成绩
    def find_student(self, sno):
        i = self.__index_student(sno)
        if i is None:
            return None
        else:
            return self.students[i]
        
# 浏览学生成绩
    def delete_student(self, sno):
        i = self.__index_student(sno)
        if i is None:
            r = '没有学号为{0:d}的学生！'.format(sno)
        else:
            del self.students[i]
            r = '删除成功。'
        return r
    
# 修改学生信息
    def update_student(self, sno):
        s = self.find_student(sno)
        if s is None:
            return '没有学号为{0:d}的学生！'.format(sno)
        else:
            print(s)
            print('请输入新的值，直接回车不修改')
            name_str = input('姓名：')
            english_str = input('英语：')
            math_str = input('数学：')
            s.name = name_str if len(name_str) > 0 else s.name
            s.english = int(english_str) if len(english_str) > 0 else s.english
            s.math = int(math_str) if len(math_str) > 0 else s.math
            return '修改成功。'

# 保存数据
    def save_data(self):
        with open('data.txt', 'w', encoding = ' utf-8') as f:
            for s in self.students:
                r = str.format('{0:d} {1:s} {2:d} {3:d}\n', s.sno, s.name, s.english, s.math)
                f.write(r)

# 按平均成绩由高到低排序
    def sort_by_sorce(self, reverse = True):
        self.students.sort(key=lambda x: x.english + x.math, reverse = reverse)
    

# 测试代码:

# if __name__ == '__main__':
#     b = BanJi('xj')
#     b.show_student()
#     a = b.find_student(19)
#     print(a)

#     sno = int(input('学号: '))
#     name = input('姓名：')
#     english = int(input('英语：'))
#     math = int(input('数学：'))

#     student=Student(sno, name, english, math)
#     r=b.add_student(student)
#     print(r)
#     b.add_student()
#     b.show_student()
#     s = b.find_student(10)
#     print()
#     print(s)
#     b.delete_student(10)
#     print()
#     b.show_student()
#     print(b.delete_student(4))
#     b.show_student()
#     b.update_student(2)
#     b.show_student()
#     b.sort_by_english(reverse=True)
#     b.show_student()
#     b.save_data()
