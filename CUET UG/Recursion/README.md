# INTRODUCING RECURSION AS A PROGRAMMING TECHNIQUE
<br>
<h1>INTRODUCTION:</h1>
<p>By definition: Recursion by definition means a technique where a function calls itself, either directly from it's own function body, or indirectly when two functions call each other recursively, provided that both the functions do have a base case 
usually while writing programs, most of you have always used iterations to solve a question or a problem statement given to you, but here's something new you can implement instead of iterative approach to solve those same questions or problem statements, and that is Recursion.</p>
<br>
<h2>Crucial step while writing recursive functions:</h2>
<p>A recursive function not just calls itself directly or indirectly, each recursive call made a function needs a certain increment in any of it's parameters, otherwise making recursive calls to the same function without incrementing or updating it's parameters results to infinite recursion error (also called as Stackoverflow error in some languages).</p>
<br>
<h2>But what if increments to the parameters produces the same error?</h2>
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

<h2>Observation:</h2>
<p>Right here in this code example you can see that how I have made it sure to update the arguement of the function
in the statement where I am calling it recursively and also how I have also made it sure to keep a base case where
if a number being passed as an arguement to the function is lesser than or equal to 1 , then the function first prints
it and then terminates the entire execution of this recurring function by that return statement.</p>

