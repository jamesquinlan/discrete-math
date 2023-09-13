# Python Lab

[COS 280 Discrete Mathematics II](https://cs.usm.maine.edu/~james.quinlan/cos280/)<br>
University of Southern Maine<br>
Instructor: [Quinlan](https://cs.usm.maine.edu/~james.quinlan)

### Learning Objectives

* Comments (single line and block)
* Assignments and variables
* Math operations
* Logical and relational operators
* if-then-else
* Loops
* Lists
* Random numbers
* Functions

 

### Comments
Comments are one of the most important parts of any program.
A single line comment is given by the hashtag, `#` symbol. These can be used as prefix or inline.  For Example,

```
# This is a comment
```

Block comments (and doc strings) are denoted with triple quotes.

```
''' This is a comment using string literals with triple quotes '''
```

Comments can span multiple lines:

```
'''
This is first line
This is second line
Here is a third line
'''
```

## Variables and Assignment Statements

Python expressions (e.g., 4+9) may contain **variables** which store values for later use in code.  For example the variable ```x``` can store the integer ```5```.  That is, we assignment the value ```5``` to the variable ```x``` by creating the **statement**  ```x=5```.


```
# Create a variable y and assign a value 5

```


### Variable Names

A variable name (also called an __identifier__) can contain:

* letters
* digits (_Note_: cannot begin with digit)
* underscores

> Python is __case sensitive__ and therefore `total` is different from `Total`.


### Variable Types
Every value has a __type__ (e.g., `int`, `float`).  To view the _value type_, use the `type` function.

```
# Determine the types of the following by using the `type()` function.

'Hello World'
123
3.1415
```

## Arithmetic

The following table summarizes arithmetic operations.

| Operation          | Operator | Example Expression |
|--------------------|----------|--------------------|
| Addition           | +        | 2 + 3              |
| Subtraction        | -        | 9 - 5              |
| Multiplication     | *        | 5 * 6              |
| Exponentiation     | **       | x ** y             |
| Division           | /        | 10 / 2             |
| Floor Division     | //       | 10 // 3            |
| Remainder (modulo) | %        | 9 % 5              |

```py
# Perform the following arithmetic in the cell below using python.
```

1. $3.75 + 19.23842$

2. $(5-3) + 23\frac{4}{7}$

3. Find the remainder when $178$ is divided by $56$

## Even and Odd Integers

You can use modulo operator to determine if an integer is even or odd.  Recall, an **even** integer $n$ can be written as $n = 2k$ for some integer $k$.  An **odd** integer $m$ can be written as $m = 2j+1$ for some integer $j$.  

The mod operator (`%`) can be used to test if even by
```
n % 2 == 0
```
and odd by
```
m % 2 == 1
```
 
```
# Determine if 234 is even or odd.  Print the result.
```

## Decision Making: `if` statement and comparison operators

* Practical construct - Flow control
* Decision structure = Branching

**Boolean expressions** evaluate to TRUE or FALSE.  A **condition** is a Boolean expression. The comparison operators are listed in the table below.

| Operation          | Operator | Example Expression |
|--------------------|----------|--------------------|
| Equal              | ==       | 2 == 3             |
| Less than          | <        | 2 < 3              |
| Greater than       | >        | 9 > 5              |
| Less than or equal | <=       | 5 <= 6             |
| Greater or equal   | >=       | x >= y             |
| Not equal          | !=       | 10 != 2            |


```
# Evaluate the Boolean expressions (record its value)
1 < 2

# Evaluate the Boolean expression (note its value)
3 != 5
```

Conditions often use **comparison operators**, i.e., ```>, <, >=, <=, ==, !=```.  Be aware of the precedence of these operators, the first four have same precedence, but higher than the last two (which have the same precedence).  That is, ```<``` and ```>``` have the same precedence, which is higher than ```==```.  

Also, be aware of syntax errors such as ``` < = ```.  The correct syntax is ```<=```.  


### ```if``` statements (branching structure)

The basic syntax of an ```if``` statement is:

```
if condition:
  code_block
```
Notice the colon (:) and the indentation.  

Assign values for integer values for x and y in order to make the following print 'Yes'

```
x =
y =
if x < y:
  print('Yes')
```

Try again, this time picking values to produce 'Yes' and then change only one value to produce 'No'.
```
x =
y =

if x < y:
  print('Yes')
else:
  print('No')
```

## For Loops

A for loop is a repetition structure to perform a task a known number of times.

The syntax is:
```
for i in range(10):
  # do something
```

```
# Print the numbers 1 to 10 using a for loop
```


## Lists

A list (array or vector) is a fundamental data structure.  Lists are denoted by square brackets.  For example, the list of the first four prime numbers are:
2, 3, 5, 7.  

In python,
```
[2, 3, 5, 7]
```


```
# Make a list of the first 7 positive composite numbers

```

**Tip**: It is often necessary to preallocate your list with ones or zeros.  The following code creates a list of length 10 with zeros in each entry, ```x = [0]*10```.

## Random Numbers

You will need to import the `random` module by typing `import random`.  Then, a random integer can be generate using `randint(start, stop+1)`.  You can alias the library as desired, e.g., `as rnd`.



```
# import the random library

# 1. Generate a random integer between 3 and 13.


# 2. Use a loop to generate a list of 20 random integers between 1 and 100
r = [0]*20   # preallocate list with zeros
```

## Functions
A function takes a value(s) and either returns a value(s), or prints to the screen or writes to a file.  The syntax is:

```
def f(x):
  # do something, calculate y
  return y

# call function like:
f(5)
```


Write two functions, `iseven` and `isodd` that will return true or false depending on whether it is even (or odd).  

Do not use an `if` statement.

```
def iseven(n):
  # write code here

def isodd(n):
  # write code here
```


## Problems

1. Write a function that determines if a positive integer is prime.

1. Write a function that lists all primes less than or equal a given positive integer.

1. Use a loop and the function above to determine whether $2^p - 1$ is prime for each of the primes not exceeding 100.

1. Show that $n^2 + n + 41$ is prime for all integers $n$ with $0 \le n \le 39$, but is not prime when $n = 40$.  Is there a polymomial in $n$ with integer coefficients and degree greater than zero that always takes on a prime value when $n$ is a positive integer?

1. Find 10 different primes each with 100 digits.

1. Find all pseudoprimes to the base 2, that is, composite integers $n$ such that $2^{n-1} \equiv 1 \,(mod\ n)$, where $n$ does not exceed 10000.


## Solutions

```
# 1. Write a function that determines if a positive integer is prime.
def isprime(n):
  # assume n > 0
  if n == 2:
    return True
  if n % 2 == 0:
      return False
  for p in range(3,int(n**0.5)+1,2):
    if (n % p == 0):
      return False
  return True

isprime(143)


# 2. Write a function that lists all primes less than or equal a given positive integer.
def primes(n):
  if n > 1:
    thePrimes = [2]
    for p in range(3,n+1,2):
      if isprime(p):
        thePrimes.append(p)
    return thePrimes
  return []

# Test
primes(100)


# 3. Use a loop and the function above to determine whether $2^p - 1$ is prime for each of the primes not exceeding 100.
primesLT100 = primes(100)
for p in primesLT100:
  print(p,2**p - 1,isprime(2**p - 1))


# 4. Show that $n^2 + n + 41$ is prime for all integers $n$ with $0 \le n \le 39$,
# but is not prime when $n = 40$.  Is there a polymomial in $n$ with integer
# coefficients and degree greater than zero that always takes on a prime value
# when $n$ is a positive integer?

for n in range(41):
  print(n, isprime(n**2 + n + 41))


#5. Find 10 different primes each with 100 digits.
count = 0
bigprimes = [0]*10
for n in range(10**99,10**100):
  if isprime(n):
    bigprimes[count] =  n
    count += 1
    if count == 10:
      break
print(bigprimes)


# 6. Find all pseudoprimes to the base 2, that is, composite integers $n$ such
# that $2^{n-1} \equiv 1 \,(mod\ n)$, where $n$ does not exceed 10000.

n = 2
pseudos = []
while n < 10000:
  if (2**(n-1) % n == 1):
    pseudos.append(n)
  n += 1

print(pseudos)
```


<!-- 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
 FOOTER 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-->
<div style="border-top: 1px solid #ccc;padding:0px 0px 20px 0px;"></div>
<i style="padding-left:0px;">
Last modified  Sun Aug 27 2023 01:20:32 PM EST
<a href="https://cs.usm.maine.edu/~james.quinlan/">Quinlan</a>
</i>  
