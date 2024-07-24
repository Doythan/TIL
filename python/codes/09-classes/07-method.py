class MyClass:
    def instance_method(self):
        return 'instance method', self

    @classmethod
    def class_method(cls):
        return 'class method', cls

    @staticmethod
    def static_method():
        return 'static method'


instance = MyClass()
# 클래스가 할 수 있는 것
print(MyClass.instance_method(instance)) # 기능적으로는 되지만 안된다고 생각해라 ! 
print(MyClass.class_method())
print(MyClass.static_method())



# 인스턴스가 할 수 있는 것
print(instance.instance_method())
print(instance.class_method()) # 기능적으로는 되지만 안된다.
print(instance.static_method()) # 기능적으로는 되지만 안된다. 협업, 유지보수 불가능 