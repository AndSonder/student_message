"""
    业务逻辑处理
"""

class StudentManagerController:
    """
        学生管理控制器,负责业务逻辑处理.
    """

    # 类变量,表示初始编号.
    __init_id = 1000

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        """
            学生列表
        :return: 存储学生对象的列表
        """
        return self.__stu_list

    def add_student(self, stu_info):
        """
            添加一个新学生
        :param stu_info: 没有编号的学生信息
        """
        stu_info.id = self.__generate_id()

        self.__stu_list.append(stu_info)

    def __generate_id(self):
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    def remove_student(self, id):
        """
            根据编号移除学生信息
        :param id: 编号
        :return:
        """
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
                return True  # 表示移除成功
        return False  # 表示移除失败

    def update_student(self, stu_info):
        """
            根据stu_info.id修改其他信息
        :param stu_info: 学生对象
        :return: 是否修改成功
        """
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.atk = stu_info.atk
                item.score = stu_info.score
                return True
        return False

    def order_by_score(self):
        """
            根据成绩，对self.__stu_list进行升序排列
        """
        for r in range(len(self.__stu_list) - 1):
            for c in range(r + 1, len(self.__stu_list)):
                if self.__stu_list[r].score > self.__stu_list[c].score:
                    self.__stu_list[r], self.__stu_list[c] = self.__stu_list[c], self.__stu_list[r]
