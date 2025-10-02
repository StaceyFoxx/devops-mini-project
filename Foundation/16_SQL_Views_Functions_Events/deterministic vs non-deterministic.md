### Deterministic functions

A function is deterministic if it always returns the same result given the same input.

#### Example:
```
ABS(-10);   -- Always returns 10
ROUND(3.14159, 2);  -- Always returns 3.14
```

Predictable, no matter when/where it runs.

### Non-deterministic functions

A function is non-deterministic if the result can change even with the same input.

#### Example:
```
NOW();     -- Changes depending on current time
RAND();    -- Returns a different random number each time
```

Not predictable — depends on external factors (time, randomness, etc.).

### Why do we need to specify?

When you create stored functions, you need to declare whether they are DETERMINISTIC or NOT DETERMINISTIC.

This helps MySQL know if it can safely cache results or use them in indexes/replication.