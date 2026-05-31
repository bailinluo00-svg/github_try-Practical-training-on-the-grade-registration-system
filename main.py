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
    
    def init(self):
        self.student_list = [] # 列表，记录在校学生的成绩信息
        
    # 添加学生成绩
    def add_student(self, student):
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

    
    # 查询指定学生成绩
    
    # 查询所有学生成绩
    
    pass




# if __name__ == "__main__":
#     s1 = Student("张三", 90, 85, 95)
#     print(s1)

#     s1.update_score(95, 90, 98)
#     print(s1)
    


    