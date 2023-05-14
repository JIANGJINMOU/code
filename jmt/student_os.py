# -*- coding: utf-8 -*-
"""
Created on Fri May 12 14:22:32 2023

@author: 蒋明涛
"""

import os
from student import Student
from banji import BanJi
import colorama
import matplotlib.pyplot as plt
from scipy import stats

# 开启windows控制台可设置颜色这一功能
colorama.init(autoreset=True)  

# 菜单选项
menu = """
\033[0;34m**************************
                                         
\033[1;31m学生成绩管理系统
                       
\033[2;31m1. 按学号浏览学生成绩
\033[4;32m2. 按学号查找学生
\033[5;33m3. 按平均成绩由高到低排序
\033[5;33m4. Q-Q图(检验样本数据概率)
\033[7;34m5. 添加学生信息
\033[0;35m6. 删除学生信息
\033[1;36m7. 修改学生信息
\033[1;36m8. 绘制成绩直方图
\033[1;31m9. 保存
\033[1;34m0. 直接退出
    
\033[0;44m**************************\033[0;44m
"""

tip = "输入（0~9）选择操作："

choice = ''
b = BanJi('信计2201')

os.system('cls')
print(menu)

while True:
    choice = input(tip)
    os.system('cls')
    print(menu)
    
# 直接退出    
    if choice == '0':
        b.save_data()
        print('数据已保存。')
        break
 
# 按学号浏览学生成绩
    elif choice == '1':
        b.students.sort()
        b.show_student()
        
# 按学号查找学生       
    elif choice == '2':
        sno = int(input('请输入要查找的学生的学号：'))
        s = b.find_student(sno)
        
        if s is None:
            print('无此学号的学生！')
        else:
            print(s)
            
# 按平均成绩由高到低排序         
    elif choice == '3':
        b.sort_by_sorce()
        b.show_student()
        
# Q-Q图(检验样本数据概率)    
    elif choice == '4':
        s = [64, 33, 63, 60, 61, 75, 71, 26, 79, 61,64, 67, 78, 60, 71, 72, 56, 70, 64, 57,82, 42, 43, 75, 94, 49, 63, 57, 56, 43,52, 43, 64, 65, 60, 64, 37, 62, 44, 78, 48]
        k = [74, 86, 57, 63, 61, 71, 50, 76, 86, 55, 70, 61,79, 77, 62, 70, 54, 76, 75, 47, 62, 58, 51, 50, 74, 57, 52, 63, 60, 79, 61, 61, 49, 64, 76, 60, 87, 35, 76, 72]
        print("输入1绘制数学成绩Q-Q图")
        print("输入2绘制英语成绩Q-Q图")
        h = int(input("请输入:"))
        if h == 1:
            l = s
            # 默认检测正态分布，参数dist='norm'
            stats.probplot(l, plot = plt)  
            plt.title("Q-Q Plot")
            plt.show()
        elif h == 2:
            l = k
            stats.probplot(l, plot = plt)
            plt.title("Q-Q Plot")
            plt.show()
        else:
            print('输入错误!')

# 添加学生信息    
    elif choice == '5':
        print('请输入学生信息')
        sno = int(input('学号: '))
        name = input('姓名：')
        english = int(input('英语：'))
        math = int(input('数学：'))
        student = Student(sno, name, english, math)
        r = b.add_student(student)
        print(r)
        
# 删除学生信息  
    elif choice == '6':
        sno = int(input('请输入要删除的学生的学号：'))
        r = b.delete_student(sno)
        print(r)
        
# 修改学生信息    
    elif choice == '7':
        sno = int(input('请输入要修改的学生的学号：'))
        r = b.update_student(sno)
        print(r)
        
# 绘制成绩直方图  
    elif choice == '8':
       s = [64, 33, 63, 60, 61, 75, 71, 26, 79, 61,64, 67, 78, 60, 71, 72, 56, 70, 64, 57,82, 42, 43, 75, 94, 49, 63, 57, 56, 43,52, 43, 64, 65, 60, 64, 37, 62, 44, 78, 48]
       k = [74, 86, 57, 63, 61, 71, 50, 76, 86, 55, 70, 61,79, 77, 62, 70, 54, 76, 75, 47, 62, 58, 51, 50, 74, 57, 52, 63, 60, 79, 61, 61, 49, 64, 76, 60, 87, 35, 76, 72]
       bins = [i for i in range(0, 101, 10)]
       print("输入1绘制数学成绩直方图")
       print("输入2绘制英语成绩直方图")
       h = int(input("请输入:"))
       if h == 1:
           #hist函数会根据所给的bins列表区间按照区间去统计个数
           plt.hist(k, bins=bins)
           plt.xticks(ticks=bins)
           plt.xlabel('成绩分组', fontproperties="SimSun")
           plt.ylabel('人数', fontproperties="SimSun")
           plt.grid()
           plt.show()
       elif h == 2:
           plt.hist(s, bins=bins)
           plt.xticks(ticks=bins)
           plt.xlabel('成绩分组', fontproperties="SimSun")
           plt.ylabel('人数', fontproperties="SimSun")
           plt.grid()
           plt.show()
       else:
           print('输入错误!')
      

# 保存数据
    elif choice == '9':
        b.save_data()
        print('保存成功！')
        
    else:
        print('输入错误!')
    # 让Python脚本暂停执行
    os.system('pause')

