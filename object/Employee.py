from abc import ABCMeta, abstractmethod


class Employee(object,metaclass=ABCMeta):
    def __init__(self,name):
        self._name=name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):
    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    def __init__(self,name,work_hour=0):
        super().__init__(name)
        self._work_hour=work_hour

    @property
    def work_hour(self):
        return self._work_hour

    @work_hour.setter
    def work_hour(self,work_hour):
        self._work_hour=work_hour if work_hour>0 else 0

    def get_salary(self):
        return 150*self._work_hour

class Salesman(Employee):
    def __init__(self,name,sales=0):
        super().__init__(name)
        self._sales=sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales=sales if sales>0 else 0

    def get_salary(self):
        return 1200+self._sales*0.05


def main():
    emps=[Manager('刘备'),Programmer('诸葛亮'),Manager("曹操"),Salesman('吕布')]
    for emp in emps:
        if isinstance(emp,Programmer):
            emp.work_hour=int(input('请输入%s本月工作时间'%emp.name))
        elif isinstance(emp,Salesman):
            emp._sales = int(input('请输入%s本月销售额' % emp.name))

        print('%s本月工资为：¥%s元'%(emp.name,emp.get_salary()))


if __name__ == '__main__':
    main()