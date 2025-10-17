#1
print("hello world")

#2
def greet():
    print("こんにちは")

greet()

#3
def print_name(name):
    print(f"私の名前は{name}です")

print_name("name")

#4
def get_greet():
    return "おはようございます"

print(get_greet())

#5
def add(a,b):
    return a+b

print(add(int(input()),int(input())))
