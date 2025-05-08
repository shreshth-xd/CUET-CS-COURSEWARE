# INTRODUCING RECURSION AS A PROGRAMMING TECHNIQUE
<br>
<ul>
<li><h1>INTRODUCTION:</h1></li>
<p>By definition: Recursion by definition means a technique where a function calls itself, either directly from it's own function body, or indirectly when two functions call each other recursively, provided that both the functions do have a base case.</p>
<br>
<li><h2>Crucial step while writing recursive functions:</h2></li>
<p>A recursive function not just calls itself directly or indirectly, each recursive call made a function needs a certain increment in any of it's parameters, otherwise making recursive calls to the same function without incrementing or updating it's parameters results to infinite recursion error (also called as Stackoverflow error in some languages).</p>
<br>
<li><h2>But what if it incrementation produces the same error?</h2></li>
<p>Now that's where the concept of "Base case" and "Recursive case" comes in, In order to make sure that a recursive function, be it a directly or indirectly recursive one, doesn't repeats itself infinitely, we make sure to program a conditional block in the function body of this recursive function which terminates the recurring execution of this function after executing the statements that we have written in the base case (if any), and such a conditional block or such a condition is called as "Base case". Now the part of the function body which recalls this function with increments in one or more than one parameters of it is called as the recursive case.</p>
<br>
<p>Have a look at the code example given below:</p>
<h3>Code:</h3>

```python
def DivBy2(x):
    if x<=1:
        print(x)
        return
    else:
        print(x)
        return DivBy2(x//2)
    
print(DivBy2(8))
```
<br>
<h3>Output:</h3>

```python
8
4
2
1
```

<li><h2>Observation:</h2></li>
<p>Right here in this code example you can see that how I have made it sure to update the arguement of the function
in the statement where I am calling it recursively and also how I have also made it sure to keep a base case where
if a number being passed as an arguement to the function is lesser than or equal to 1 , then the function first prints
it and then terminates the entire execution of this recurring function by that return statement.</p>
<br>
<p>So in our code example:</p>
<p>The base case is:</p>

```python
if x<=1:
    print(x)
    return
```
<p>The recursive case is:</p>

```python
return DivBy2(x//2)
```

<li><h2>Direct and indirect recursion:</h2></li>
<p>There are two ways of using recursion in a program, Direct recursion and indirect recursion.</p>
<br>
<li><h3>Direct recursion:</h3></li>
<p>Direct recursion is widely used while writing recursive functions and using recursion in a program, where a function calls itself
from it's own function body, and again, while making sure that each recursive call updates the arguement to be used in the function
and is reachable to the base case of that recursive function.</p>
<br>
<li><h3>Indirect recursion:</h3></li>
<p>When two or more than two functions call each other from each other's function bodies, then it's called as indirect recursion,
provided that this chained recursive flow gets to stop at some point of this recurring execution with the help of the base cases of
all these recursive functions.</p>
<span>For example:</span>

```python
def odd(x):
    if x%2==0:
        return
    else:
        return even(x+1)

def even(x):
    if x%2!=0:
        return
    else:
        return odd(x+1)

odd(1)
    
```
<p>If you look at this code example, you can say, that this chain of recursion is never going to terminate itself,
as the function odd(x) takes the number 1 which is odd and then passes it to the function even(x) which in turn again
increments it and passes it to the function odd(x) and this cycle continues, and this cycle of infinite recursion produces
an exception which gets displayed as: </p>

```python
RecursionError: maximum recursion depth exceeded in comparison
```

<p>In order to make the an infinite flow of recursion stop at a certain point, we have add a base case reachable by this recursion.</p>
<p>For example:</p>

```python
def odd(x):
    if x>=10:
        print(x)
        return
    if x%2==0:
        return
    else:
        return even(x+1)

def even(x):
    if x>=10:
        print(x)
        return
    if x%2!=0:
        return
    else:
        return odd(x+1)

odd(1)
```
<li>
<h2>Infinite recursion and it's result:</h2></li>
<p>We have already seen how missing a base case in a recursive function can induce a infinite flow of recursion, and how a base case 
must be reachable by the function otherwise, if a function fails to reach any base case of it, then still it will result in infinite
recursion and hence a runtime exception.</p>
<br>

<li><h3>Ok so, Why doeesn't the interpreter throws this exception at once? Why does it throws it after executing it for some time?</h3></li>
<p>To understand this, we have to realise that all the function calls are stored and managed in a stack type data structure known
as call stack, here when the call stacks gets pushed with too many recursive calls (since there is no upper limit to as how many 
elements can be pushed to a stack implemented through list in Python) it crashes the program after returning the runtime exception</p>

```python
RecursionError: maximum recursion depth exceeded in comparison
```
<p>From the Operating system's point of view, it is preferrable to crash a program or crash a program which encounters stack overflow
error than to affect performance of other well running programs in the background.</p>
<br>

<li><h2>Some recursive codes:</h2></li>
<ol type="1">
<li><h3>Calculating factorial</h3></li>
<span>Code:</span>

```python
def factorial(x):
    if x<=0:
        return "Doesn't exists"
    elif x==1:
        return 1
    else:
        return x*factorial(x-1)

print(factorial(5))
```
<span>Output:</span>

```python
120
```
<br>
<li><h3>Fibonacci sequence</h3></li>
<span>Code:</span>

```python
def fibonacci(x,a=0,b=1):
    if a+b==x:
        print(a+b)
        return

    if a==0 and b==1:
        print(a)
        print(b)

    c=a+b
    print(c)
    a=b
    b=c
    fibonacci(x,a,b)

fibonacci(2)
```
<span>Output:</span>

```python
0
1
1
2
```
<br>
<li><h3>nth Fibonacci</h3></li>
<span>Code:</span>

```python
def nfib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return nfib(n-1) + nfib(n-2)
```
</ol>
</ul>