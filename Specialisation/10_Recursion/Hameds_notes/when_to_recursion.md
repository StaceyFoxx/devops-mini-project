# When To Recursion?
#### Note from Hamed - this is not as easy as just giving you a list. It will take some time and experience for you to get your head around WHEN to recursion. But I do promise it will come to you eventually!


### Keep on eye out for these sort of problems which lend more to recursive solutions:

1. The problem can be broken into smaller, similar sub-problems:
    * For example, calculating factorial (n!) or finding Fibonacci numbers. These naturally follow a divide-and-conquer
      pattern (Note that we haven't yet covered this, but its easy to google).

2. The problem has a natural "stop condition":
    * For example, summing numbers until 0 or reversing a string until it’s empty.

3. Tree-like (or graph-like) structures need to be explored:
    * For example, searching in hierarchical data like file directories or binary trees. Recursion is cleaner for these
      cases.

4. You want simpler, more readable code for specific tasks:
    * Recursion can often make the logic clearer compared to a loop, especially for problems with unknown or dynamic
      depth (e.g., navigating a maze).

### However, avoid recursion if:

1. The problem is easily handled with a loop (e.g., counting numbers in a range).
2. There’s a risk of hitting recursion depth limits (too many levels).