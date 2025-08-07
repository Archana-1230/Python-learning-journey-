MCQs – Tuple, Set, Dictionary

Tuple MCQs:
1. What is the output of:

a = (1, 2, 3)
a[0] = 5

a. 5
b. Error ✅
c. (5,2,3)
d. None

> Tuples are immutable; cannot assign a new value.


2. What will t.count(2) return for t = (1, 2, 2, 3)?
a. 1
b. 2 ✅
c. 3
d. Error


3. What does t.index(3) return for t = (1, 2, 3, 4)?
a. 0
b. 2
c. 3 ✅
d. Error



4. Which of the following creates a tuple with a single item?
a. t = (1)
b. t = (1,) ✅   
c. t = 1  
d.t = [1]`

Set MCQs:

5. What is the result of set("hello")?
a. {'h', 'e', 'l', 'o'} ✅
b. ['h', 'e', 'l', 'o']
c. ('h', 'e', 'l', 'o')
d. Error


6. What is printed?

s = {1, 2, 3}
s.add(2)
print(s)

a. {1, 2, 2, 3}
b. {1, 2, 3} ✅
c. Error
d. None

> add() has no effect if the item already exists.

7. What is the output of:

a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)

a. {1, 2, 3, 4, 5}
b. {3} ✅
c. {}
d. Error


Dictionary MCQs:

8. What is the output of:

d = {"a":1, "b":2}
print(d.get("c"))

a. Error
b. 0
c. None ✅
d. “c”


9. What does this do?

d = {"x": 1}
d["y"] = 2
print(d)

a. {"x": 1}
b. {"x": 1, "y": 2} ✅
c. Error
d. {"y": 2}


10. What is the result of:

d = {"a": 1, "b": 2}
d.update({"b": 3, "c": 4})
print(d)

a. {"a": 1, "b": 2, "c": 4}
b. {"a": 1, "b": 3, "c": 4} ✅
c. {"b": 3, "c": 4}
d. Error