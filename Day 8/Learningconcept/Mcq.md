Functions MCQs

Q1. What will this code print?

def greet(name="Guest"):
    return f"Hello, {name}!"
print(greet())

a) Hello, Guest! ✅
b) Hello, name!
c) Error
d) None


Q2. Which is correct about Python functions?
a) They must return a value
b) They can return multiple values ✅
c) They must have parameters
d) They cannot be nested


Q3. What is the output?

def test(a, b=2, c=3):
    return a + b + c
print(test(5, c=10))

a) 20 ✅
b) 10
c) Error
d) 15


Q4. What is the type of **kwargs inside a function?
a) list
b) tuple
c) dict ✅
d) set



Q5. Which is NOT a valid function definition?
a) def f(a, b=5): pass
b) def f(a=5, b): pass ✅
c) def f(*args): pass
d) def f(**kwargs): pass


Q6. Output?

def fun():
    x = 5
    return x
print(fun())

a) 5 ✅
b) None
c) Error
d) Undefined


Q7. Which function call is correct for the following definition?

def calc(a, b=10, c=5):
    return a + b + c

a) calc(5, 3, 2) ✅
b) calc(b=3, 2) ❌ (invalid syntax)
c) calc(5, c=2) ✅
d) calc() ❌ (missing a required argument)


Q8. Output?

add = lambda x, y=2: x + y
print(add(5))

a) 5
b) 7 ✅
c) Error
d) None


Q9. What does this code print?

def outer():
    def inner():
        return "Inner"
    return inner()
print(outer())

a) Inner ✅
b) outer
c) Error
d) None


Q10. Which built-in function can be used to apply another function to each element of a sequence?
a) map() ✅
b) filter()
c) reduce()
d) apply()
