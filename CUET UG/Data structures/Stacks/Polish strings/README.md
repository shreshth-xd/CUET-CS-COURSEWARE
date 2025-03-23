# <h1>Introduction to Polish strings</h1>

<p>Polish strings is one of the basic applications of Stack data structure.</p>
<br>
<p>Polish strings are just a notation or a way of writing arithmetic expressions in such a way that it can
be understood by the computers and machines. This concept of Polish strings is named after a polish
mathematician "Jan Lukasiewicz". There are three types of Polish strings or notations, namely:</p> 

<ol>
    <li>Infix notation - The one which is readable and used by humans. For ex. A+B</li>
    <li>Postfix notation - The expressions where the operators come after the operands AB+</li>
    <li>Prefix notation - The expressions where the operators come before the operands +AB</li>
</ol>

# <h2>Ok, so.. but how does this makes it a application of Stack?</h2>
<p>Stacks, as a data structure are a used for a variety of purposes but in case of Polish strings and in 
case of converting the human readable arithmetic expressions to machine readable format, Stacks are used for: </p>
<br>
<ol>
    <li>To convert an infix notation (human readable) to postfix notation.</li>
    <li>To convert an infix notation (human readable) to prefix notation.</li>
    <li>To evaluate a prefix or a postfix notation's numerical value.</li>
</ol>
<p>Although, I do have scripts related to the conversion of infix expressions to postfix and prefix formats 
which are clearly a way to implement stacks to solve this problem statement ,but there is also a direct 
method to estimate the postfix or prefix format of a given expression directly, but since these direct
methods is purely based on simple logic and requires a little bit of retentivity I suggest you guys to use
it in exams and not while you revise Stacks for CUET or Boards.</p>