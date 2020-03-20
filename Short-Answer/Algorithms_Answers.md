#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) This will only be run run n times until the condition is met.

b) O(log n). The while loop is run for every value of N. everytime two loops are multiplied it is at least log(n).

c) The number of bunny ears scales linear to # of buns. This will only be run n times.
O(n)

## Exercise II

I would set egg_is_broken to a boolean. I would make a function that took in all the floors (list). The base case for this funtion would return floor value where == to egg_is_broken is True.

Starting from the highest value (higest floor) I would recursively use function(n - 1)

Then subtract one from the value of floors. This would give the lowest possible floor that eggs can survive, while also minimizing the eggs lost to discover it.
