# Coding Challenge

> Time taken: 90 minutes
> Language: Python
> Source code: [rand13.py](https://github.com/huynet/challenge/blob/master/rand13.py)

## Question

rand11() returns a random integer from 1 to 11 (inclusive) with equal probability. Use this function to write a function rand13() that returns a random integer from 1 to 13 (inclusive) with equal probability. Assume rand11() is a "black box".

Sample Output: 
rand13() returns 2 
rand13() returns 13 
rand13() returns 8 

## Thinking
**Initial Attempts**
- 11 and 13 -> prime numbers -> something with 143 (smallest common multiple)
- 13 x 13 Matrix with structure like a snake game like this

| Snake  | Loop/Circle |
| ------------- | ------------- |
| ![](https://i.imgur.com/NwDkGYD.jpg=250x)  | ![](https://i.imgur.com/y6ISop6.png=250x) |

## Designing

|  1 |2   |3   |4   |5   |6   |7   | 8  | 9  |10   |11   |
|---|---|---|---|---|---|---|---|---|---|---|
| 12  |13   |1   |2   |3   |4   |5   |6   |7   |8   |9   |
| 10  |11   |12   |13   |1   |2   |3   |4   |5   |6   |7   |
|8   |9   |10   |11  |12   |13   |1   |2   |3   |4   |5   |
|6   |7   |8   |9   |10   |11   |12   |13   |1   |2   |3   |
|4   |5   |6   |7   |8   |9   |10   |11   |12   |13  |1   |
|2   |3   |4   |5   |6   |7   |8   |9   |10   |11   |12   |
|13   |1   |1   |3   |4   |5   |6   |7   |8   |9   |10   |
|11   |12   |13   |1   |2   |3   |4   |5   |6   |7   |8   |
|9   |10   |11   |12   |13   |1   |2   |3   |4   |5   |6   |
|7   |8   |9|10   |11   |12   |13   |0   |0   |0   |0   |

- We will loop through the 11x11 matrix and insert equal amount of elements consecutively. 
- We set the rest to zero
- Then, we call ``rand11()`` to get random elements to the row and column index
- If ``(matrix[row][cow]) == 0`` -> we randomize row and col again until ``result != 0``. Specifically:
``` 
result = 0
while (result == 0):
    row = rand11() - 1
    col = rand11() - 1
    result = matrix[row][col]

return result

```        

## Implementation time
- Best case: 1 attempt (as most cases are)
- Worst case: infinity, we draw 0 every single time (in this case, the odd is ``4/121 ``)

## Interesting
``1001 = 7 x 11 x 13``

If we could use ```rand11()``` to create a number between ```0001``` and ```1001```, and then ```return number % 13```, that could be ```rand13()```. Unfortunately, I can't find a way to do this.

I implemented a DYI version, [randAny.py](https://github.com/huynet/challenge/blob/master/randAny.py), when you plug in the ```lower``` and ```upper``` to find a random number between 1 and ```upper```, in this case, ```rand(11, 13)```



