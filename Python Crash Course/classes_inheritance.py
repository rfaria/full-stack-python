class MyClass:
  x = 5

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print('Hello, my name is', self.name, 'and I\'m', self.age)

class Human(Person):
    pass

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major


def main():
    # p1 = MyClass()
    # print(p1.x)

    person1 = Person('John Doe', 42)
    print(person1.name)
    print(person1.age)

    del person1.age
    try:
        print(person1.name)
        print(person1.age)
    except:
        print('Something went wrong.')

    name = input('Enter your name:')
    age = int(input('Enter your age: '))
    
    person2 = Person(name, age)

    print(person2.name)
    print(person2.age)

    person2.greet()

    student2 = Student(person2.name, person2.age, 'Math')

    print(student2.name)
    print(student2.age)
    print(student2.major)

    student2.greet()

    human1 = Human('John', 22)

    human1.greet()

if __name__ == '__main__':
    main()