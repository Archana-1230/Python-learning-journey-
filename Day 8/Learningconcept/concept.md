Python Functions 
Function:
A function is a reusable block of code designed to perform a specific task.

Syntax:

def function_name(parameters):
    # function body
    return value

Types of Functions

1. Built-in functions → len(), max(), sorted(), etc.


2. User-defined functions → Functions you create using def.


3. Lambda (Anonymous) functions → Short, one-line functions using lambda.



Function Parameters

Parameter Type	Description	Example

Positional	Passed in order	def add(a,b)
Default	Value if not passed	def add(a,b=10)
Keyword	Named arguments	add(b=4, a=2)
Arbitrary *args	Unlimited positional args (tuple)	def add(*nums)
Arbitrary **kwargs	Unlimited keyword args (dict)	def info(**data)


Return Statement

A function can return single or multiple values.

Multiple values are returned as a tuple.


Variable Scope

Local → Inside the function

Global → Declared outside, accessed using global keyword


Advanced Concepts

Recursion → Function calling itself

Higher-order functions → Function taking other functions as arguments

map(), filter(), reduce() → Functional programming utilities
