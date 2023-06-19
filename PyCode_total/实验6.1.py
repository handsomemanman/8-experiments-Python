class People:
    def __init__(self, name, gender, age):
        self._name = name  # 一个下划线表示保护成员
        self._gender = gender
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_gender(self):
        return self._gender

    def set_gender(self, gender):
        self._gender = gender

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age


class Teacher(People):  # 括号里面写入类名 表示继承该类
    def __init__(self, name, gender, age, teacher_id, college_name):
        super().__init__(name, gender, age)  # 初始化父类变量
        self._teacher_id = teacher_id
        self._college_name = college_name
        self._count = 0

    def get_teacher_id(self):
        return self._teacher_id

    def set_teacher_id(self, teacher_id):
        self._teacher_id = teacher_id

    def get_college_name(self):
        return self._college_name

    def set_college_name(self, college_name):
        self._college_name = college_name

    def get_count(self):
        return self._count

    def set_count(self, count):
        self._count = count

    def print_info(self):
        print("姓名:", self._name)
        print("年级:", self._gender)
        print("年龄:", self._age)
        print("工号:", self.teacher_id)
        print("学院:", self._college_name)
        print("数量统计:", self._count)


class Student(People):
    def __init__(self, name, gender, age, student_id, class_name):
        super().__init__(name, gender, age)
        self._student_id = student_id
        self._class_name = class_name
        self._count = 0

    def get_student_id(self):
        return self._student_id

    def set_student_id(self, student_id):
        self._student_id = student_id

    def get_class_name(self):
        return self._class_name

    def set_class_name(self, class_name):
        self._class_name = class_name

    def get_count(self):
        return self._count

    def set_count(self, count):
        self._count = count

    def printInfo(self):
        print("姓名:", self._name)
        print("年级:", self._gender)
        print("年龄:", self._age)
        print("学号:", self._student_id)
        print("班级:", self._class_name)
        print("数量统计:", self._count)
