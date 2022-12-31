Q.1. When is the else part of a try-except block executed?

In an if-else block, the else part is executed when the condition in the if-statement is False. But with a try-except block, the else part executes only if no exception is raised in the try part.

Q.2. If a list is nums=[0,1,2,3,4], what is nums[-1]?

This code does not throw an exception. nums[-1] is 4 because it begins traversing from right

Q.3. What is the PYTHONPATH variable?

PYTHONPATH is the variable that tells the interpreter where to locate the module files imported into a program. Hence, it must include the Python source library directory and the directories containing Python source code. You can manually set PYTHONPATH, but usually, the Python installer will preset it.

Q.4. Explain join() and split() in Python.

join() lets us join characters from a string together by a character we specify.

>>> ','.join('12345')
‘1,2,3,4,5’

split() lets us split a string around the character we specify.

>>> '1,2,3,4,5'.split(',')
[‘1’, ‘2’, ‘3’, ‘4’, ‘5’]

Q.5. Explain the output of the following piece of code-

x=[‘ab’,’cd’]
print(len(map(list,x)))
This actually gives us an error- a TypeError. This is because map() has no len() attribute in their dir().

Important for Interview – Package of top 5 Python Projects with source code

Q.6. Explain a few methods to implement Functionally Oriented Programming in Python.

Sometimes, when we want to iterate over a list, a few methods come in handy.

a. filter()

Filter lets us filter in some values based on conditional logic.

>>> list(filter(lambda x:x>5,range(8)))
[6, 7]

b. map()

Map applies a function to every element in an iterable.

>>> list(map(lambda x:x**2,range(8)))
[0, 1, 4, 9, 16, 25, 36, 49]
c. reduce()

Reduce repeatedly reduces a sequence pair-wise until we reach a single value.

>>> from functools import reduce
>>> reduce(lambda x,y:x-y,[1,2,3,4,5])
-13

Q.7. So what is the output of the following piece of code?

x=[‘ab’,’cd’]
print(len(list(map(list,x))))
This outputs 2 because the length of this list is 2. list(map(list,x)) is [[‘a’, ‘b’], [‘c’, ‘d’]], and the length of this is 2.

Q.8. Is del the same as remove()? What are they?

del and remove() are methods on lists/ ways to eliminate elements.

>>> list=[3,4,5,6,7]
>>> del list[3]
>>> list
[3, 4, 5, 7]

>>> list.remove(5)
>>> list
[3, 4, 7]

While del lets us delete an element at a certain index, remove() lets us remove an element by its value.

Q.9. How do you open a file for writing?

Let’s create a text file on our Desktop and call it tabs.txt. To open it to be able to write to it, use the following line of code-

>>> file=open('tabs.txt','w')
This opens the file in writing mode. You should close it once you’re done.

>>> file.close()
Q.10. Explain the output of the following piece of code-

>>> tuple=(123,'John')
>>> tuple*=2
>>> tuple
(123, ‘John’, 123, ‘John’)

In this code, we multiply the tuple by 2. This duplicates its contents, hence, giving us (123, ‘John’, 123, ‘John’). We can also do this to strings:

>>> 'ba'+'na'*2
‘banana’

Q.11. Differentiate between the append() and extend() methods of a list.

The methods append() and extend() work on lists. While append() adds an element to the end of the list, extend adds another list to the end of a list.

Let’s take two lists.

>>> list1,list2=[1,2,3],[5,6,7,8]
This is how append() works:

>>> list1.append(4)
>>> list1
[1, 2, 3, 4]

And this is how extend() works:

>>> list1.extend(list2)
>>> list1
[1, 2, 3, 4, 5, 6, 7, 8]

You must check the detailed description for Lists in Python

Q.12. What are the different file-processing modes with Python?

We have the following modes-

read-only – ‘r’
write-only – ‘w’
read-write – ‘rw’
append – ‘a’
We can open a text file with the option ‘t’. So to open a text file to read it, we can use the mode ‘rt’. Similarly, for binary files, we use ‘b’.

Q.13. What does the map() function do?

map() executes the function we pass to it as the first argument; it does so on all elements of the iterable in the second argument. Let’s take an example, shall we?

>>> for i in map(lambda i:i**3, (2,3,7)):
print(i)
8
27
343

This gives us the cubes of the values 2, 3, and 7.

Q.14. Explain try, raise, and finally.

These are the keywords we use with exception-handling. We put risky code under a try block, use the raise statement to explicitly raise an error, and use the finally block to put code that we want to execute anyway.

Q.15. What happens if we do not handle an error in the except block?

If we don’t do this, the program terminates. Then, it sends an execution trace to sys.stderr.

Q.16. Is there a way to remove the last object from a list?

Yes, there is. Try running the following piece of code-

>>> list=[1,2,3,4,5
>>> list.pop(-1)
5

>>> list
[1, 2, 3, 4]

Q.17. How will you convert an integer to a Unicode character?

This is simple. All we need is the chr(x) built-in function. See how.

>>> chr(52)
‘4’

>>> chr(49)
‘1’

>>> chr(67)
‘C’

Don’t forget to check DataFlair’s latest guide on Python Built-in Functions

Q.18. Explain the problem with the following piece of code-

>>> def func(n=[]):
              #playing around
               pass
>>> func([1,2,3])
>>> func()
>>> n
The request for n raises a NameError. This is since n is a variable local to func and we cannot access it elsewhere. It is also true that Python only evaluates default parameter values once; every invocation shares the default value. If one invocation modifies it, that is what another gets. This means you should only ever use primitives, strings, and tuples as default parameters, not mutable objects.

Q.19. What do you see below?

s = a + ‘[‘ + b + ‘:’ + c + ‘]’

This is string concatenation. If a, b, and c are strings themselves, then it works fine and concatenates the strings around the strings ‘[‘, ‘:’, and ‘]’ as mentioned. If even one of these isn’t a string, this raises a TypeError.

Q.20. So does recursion cause any trouble?

Sure does:

Needs more function calls.
Each function call stores a state variable to the program stack- consumes memory, can cause memory overflow.
Calling a function consumes time.
Q.21. What good is recursion?

With recursion, we observe the following:

Need to put in less efforts.
Smaller code than that by loops.
Easier-to-understand code.
Q.22. What does the following code give us?

>>> b=(1)
Not a tuple. This gives us a plain integer.

>>> type(b)
<class ‘int’>

To let it be a tuple, we can declare so explicitly with a comma after 1:

>>> b=(1,)
>>> type(b)
<class ‘tuple’>

Q.23. Why are identifier names with a leading underscore disparaged?

Since Python does not have a concept of private variables, it is a convention to use leading underscores to declare a variable private. This is why we mustn’t do that to variables we do not want to make private.

Q.24. Can you remove the whitespaces from the string “aaa bbb ccc ddd eee”?

I can think of three ways to do this.

Using join-

>>> s='aaa bbb ccc ddd eee'
>>> s1=''.join(s.split())
>>> s1
‘aaabbbcccdddeee’

Using a list comprehension–

>>> s='aaa bbb ccc ddd eee'
>>> s1=str(''.join(([i for i in s if i!=' '])))
>>> s1
‘aaabbbcccdddeee’

Using replace()-

>>> s='aaa bbb ccc ddd eee'
>>> s1 = s.replace(' ','')
>>> s1
‘aaabbbcccdddeee’

Q.25. How do you get the current working directory using Python?

Working on software with Python, you may need to read and write files from various directories. To find out which directory we’re presently working under, we can borrow the getcwd() method from the os module.

>>> import os
>>> os.getcwd()
‘C:\\Users\\Ayushi\\AppData\\Local\\Programs\\Python\\Python37-32’

Top Python Interview Questions and Answers
Q.26. How would you randomize the contents of a list in-place?

For this, we’ll import the function shuffle() from the module random.

>>> from random import shuffle
>>> shuffle(mylist)
>>> mylist
[3, 4, 8, 0, 5, 7, 6, 2, 1]

Q.27. How do you remove the leading whitespace in a string?

Leading whitespace in a string is the whitespace in a string before the first non-whitespace character. To remove it from a string, we use the method lstrip().

>>> ' Ayushi '.lstrip()
‘Ayushi ‘

As you can see, this string had both leading and trailing whitespaces. lstrip() stripped the string of the leading whitespace. If we want to strip the trailing whitespace instead, we use rstrip().

>>> ' Ayushi '.rstrip()
‘ Ayushi’

Q.28. Below, we give you code to remove numbers smaller than 5 from the list nums. However, it does not work as expected. Can you point out the bug for us?

>>> nums=[1,2,5,10,3,100,9,24]
>>> for i in nums:
             if i<5:
                         nums.remove(i)
>>> nums
[2, 5, 10, 100, 9, 24]

This code checks for each element in nums- is it smaller than 5? If it is, it removes that element. In the first iteration, 1 indeed is smaller than 5. So it removes that from this list. But this disturbs the indices. Hence, it checks the element 5, but not the element 2. For this situation, we have three workarounds:

Create an empty array and append to that-

>>> nums=[1,2,5,10,3,100,9,24]
>>> newnums=[]
>>> for i in nums:
       if i>=5:
newnums.append(i)
>>> newnums
[5, 10, 100, 9, 24]

Using a list comprehension-

>>> nums=[1,2,5,10,3,100,9,24]
>>> newnums=[i for i in nums if i>=5]
>>> newnums
[5, 10, 100, 9, 24]

Using the filter() function-

>>> nums=[1,2,5,10,3,100,9,24]
>>> newnums=list(filter(lambda x:x>=5, nums))
>>> newnums
[5, 10, 100, 9, 24]

Q.29. What is the enumerate() function in Python?

enumerate() iterates through a sequence and extracts the index position and its corresponding value too.

Let’s take an example.

>>> for i,v in enumerate(['Python','C++','Scala']):
        print(i,v)
0 Python
1 C++
2 Scala

Q.30. How will you create the following pattern using Python?
*
**
***
****
*****

We will use two for-loops for this.

>>> for i in range(1,6):
       for j in range(1,i+1):
                 print('*',end='')
       print()
Q.31. Where will you use while rather than for?

Although we can do with for all that we can do with while, there are some places where a while loop will make things easier-

python advanced interview questions

For simple repetitive looping
When we don’t need to iterate through a list of items- like database records and characters in a string.
Want to revise the concepts of loops? Here it is – Python Loops

Q.32. Take a look at this piece of code:

>>> A0= dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
>>> A1= range(10)
>>> A2= sorted([i for i in A1 if i in A0])
>>> A3= sorted([A0[s] for s in A0])
>>> A4= [i for i in A1 if i in A3]
>>> A5= {i:i*i for i in A1}
>>> A6= [[i,i*i] for i in A1]
>>> A0,A1,A2,A3,A4,A5,A6
What are the values of variables A0 to A6? Explain.

Here you go:

A0= {‘a’: 1, ‘b’: 2, ‘c’: 3, ‘d’: 4, ‘e’: 5}
A1= range(0, 10)
A2= []
A3= [1, 2, 3, 4, 5]
A4= [1, 2, 3, 4, 5]
A5= {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
A6= [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]

Now to find out what happened. A0 zips ‘a’ with 1, ‘b’ with 2, and so on. This results in tuples, which the call to dict() then turns into a dictionary by using these as keys and values.

A1 gives us a range object with start=0 and stop=10.
A2 checks each item in A1- does it exist in A0 as well? If it does, it adds it to a list. Finally, it sorts this list. Since no items exist in both A0 and A1, this gives us an empty list.
A3 takes each key in A0 and returns its value. This gives us the list [1,2,3,4,5].
A4 checks each item in A1- does it exist in A3 too? If it does, it adds it to a list and returns this list.
A5 takes each item in A1, squares it, and returns a dictionary with the items in A1 as keys and their squares as the corresponding values.
A6 takes each item in A1, then returns sublists containing those items and their squares- one at a time.
Q.33. Does Python have a switch-case statement?

In languages like C++, we have something like this:

switch(name)
{
   case ‘Ayushi’:
       cout<<”Monday”;
       break;
   case ‘Megha’:
       cout<<”Tuesday”;
       break;
   default:
       cout<<”Hi, user”;
}
But in Python, we do not have a switch-case statement. Here, you may write a switch function to use. Else, you may use a set of if-elif-else statements. To implement a function for this, we may use a dictionary.

>>> def switch(choice):
   switcher={
       'Ayushi':'Monday',
       'Megha':'Tuesday',
      print(switcher.get(choice,'Hi, user'))
return

>>> switch('Megha')
Tuesday

>>> switch('Ayushi')
Monday

>>> switch('Ruchi')
Hi, user

Here, the get() method returns the value of the key. When no key matches, the default value (the second argument) is returned.

Q.34. Differentiate between deep and shallow copy.

python basic interview questions

A deep copy copies an object into another. This means that if you make a change to a copy of an object, it won’t affect the original object. In Python, we use the function deepcopy() for this, and we import the module copy. We use it like:

>>> import copy
>>> b=copy.deepcopy(a)
A shallow copy, however, copies one object’s reference to another. So, if we make a change in the copy, it will affect the original object. For this, we have the function copy(). We use it like:

>>> b=copy.copy(a)
Python Developer Interview Questions
Q.35. Can you make a local variable’s name begin with an underscore? (developer)

You can, but you should not. This is because:

Local variables indicate private variables of a class, and so, they confuse the interpreter.
