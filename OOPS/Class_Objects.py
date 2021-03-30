class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')


P = Person()
# Output: 10
print(P.age)
# Output: <function Person.greet>
print(P.greet)
# Output: 'This is my second class'
print(P.__doc__)
