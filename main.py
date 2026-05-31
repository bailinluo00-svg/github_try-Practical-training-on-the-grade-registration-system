### 学生类
class Student:
    def __init__(self, name, chinese, math , english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math} | 英语：{self.english} | 总分：{self.chinese + self.math + self.english}"
    
    # 修改学生成绩
    def update_score(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english
    
  # 教务管理系统类
class EduManagement:
    system_version = '1.0.0'
    system_name = '教务管理系统'
    system_author = 'Foxsol'
    
    def __init__(self):
        self.student_list = [] # 列表，记录在校学生的成绩信息
        
    # 添加学生成绩
    def add_student(self):
        name = input("请输入学生姓名：")
        
        # 判断学生姓名是否存在，如果存在，则添加失败（不能重复添加）
        for s in self.student_list:
            if s.name == name:
                print("该学生已存在，添加失败")
                return  # 返回，不执行后续代码
        
        chinese = int(input("请输入语文成绩："))
        math = int(input("请输入数学成绩："))
        english = int(input("请输入英语成绩："))
        
        # 判断分数是否再0~100之间
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name, chinese, math, english)
            self.student_list.append(stu)
            print('学生信息添加成功')
        else:
            print("各科成绩必须得在0~100之间")
            return  # 返回，不执行后续代码

    # 修改学生成绩
    def update_student(self):
        name = input("请输入要修改成绩的学生姓名：")
        # 根据学生姓名找到该学生的信息
        for s in self.student_list:
            if s.name == name:
                print(f'当前成绩：{s}')
                chinese = int(input("请输入修改后的语文成绩："))
                math = int(input("请输入修改后的数学成绩："))
                english = int(input("请输入修改后的英语成绩："))
                
                # 判断分数是否再0~100之间
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese, math, english)
                    print('修改成功')
                    print(f'修改后的成绩：{s}')
                    return
                else:
                    print("各科成绩必须得在0~100之间")
                    return
                
        print("该学生不存在，修改失败")
        
    # 删除学生成绩
    def delete_student(self):
        name = input("请输入要删除成绩的学生姓名：")
        # 根据学生姓名找到该学生的信息
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print('学生信息删除成功')
                return
        print("该学生不存在，删除失败")
        
    # 查询指定学生成绩
    def query_student(self):
        name = input("请输入要查询成绩的学生姓名：")
        # 根据学生姓名找到该学生的信息
        for s in self.student_list:
            if s.name == name:
                print(f"学生信息：{s}")
                return
        print("该学生不存在，查询失败")
  
    # 查询所有学生成绩
    def list_student(self):
        for s in self.student_list:
            print(s)
    
    # 运行系统
    def run(self):
        print(f"欢迎使用{self.system_name}，版本{self.system_version}，作者{self.system_author}")
        
        # 菜单制作
        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print('# 1.添加学生  2.修改学生成绩  3.删除学生成绩  4.查询指定学生  5.查询所有学生  6.退出系统 #')
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print()
            
            choice = input('请选择需要执行的操作，输入1~6：')
            match choice:
                case '1':
                    self.add_student()
                case '2':
                    self.update_student()
                case '3':
                    self.delete_student()
                case '4':
                    self.query_student()
                case '5':
                    self.list_student()
                case '6':
                    print("谢谢使用，系统退出")
                    break
                case _: # 输入其他情况
                    print("输入错误，请输入1~6之间的数字")

if __name__ == '__main__':
    edu_managerment = EduManagement()
    edu_managerment.run()

   


    