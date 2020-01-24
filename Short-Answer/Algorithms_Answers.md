#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This is a case of Linear Time (O(n)) because we have to look at every item in the array.


b) This is a case of Quadratic Time (O(n2)) do to the nested while loop within the for loop. A linear operation within another linear operation.


c) In this case, we are directly accessing the value of a variable. Using one step makes it Constant Time (O(1)).

## Exercise II

First we need to a function that takes in N and F as arguments.

Then we need to create a base case where there are no more floors or no more eggs.

we could set a mid point for the floors.

if the egg breaks we go down half the floors and try again, if it doesnt break we go up

if the eggs breaks we repeat, if not, we move up half the floors between where it last broke and where it didnt break and try again. repeat untill lowest breaking floor is found.

the complexity of this solution would be O(log n) at best if we find out which side of the floors array to check on and repeat recursively.




