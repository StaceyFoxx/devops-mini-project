# Examples of Testable vs Non-Testable Python Functions

## Testable Functions

Testable functions typically:
- Have clear inputs and outputs
- Don't rely on external state
- Have deterministic behavior
- Have a single responsibility

### Example 1: Pure Function
```python
def add_numbers(a, b):
    return a + b
```
This is highly testable because:
- It always returns the same output for the same input
- No side effects
- No external dependencies

### Example 2: Data Transformation
```python
def format_name(first, last):
    return f"{last.upper()}, {first.capitalize()}"
```
Easily testable with various inputs and edge cases.

### Example 3: Domain Logic with Dependencies Passed In
```python
def calculate_discount(price, discount_rate, discount_calculator):
    return discount_calculator(price, discount_rate)
```
Testable because dependencies are injectable.

## Non-Testable Functions

Non-testable functions typically:
- Have side effects
- Rely on external state
- Use non-injectable dependencies
- Mix concerns

### Example 1: Using Global State
```python
total = 0
def add_to_total(value):
    global total
    total += value
    return total
```
Hard to test because it depends on and modifies global state.

### Example 2: Direct External Dependencies
```python
def fetch_user_data():
    response = requests.get("https://api.example.com/users")
    return response.json()
```
Difficult to test because it directly calls an external API.

### Example 3: Mixed Responsibilities
```python
def process_user_login(username, password):
    user = database.find_user(username)
    if user and user.password == password:
        log_file = open("access.log", "a")
        log_file.write(f"{username} logged in at {datetime.now()}\n")
        log_file.close()
        session["user_id"] = user.id
        return True
    return False
```
Difficult to test because it:
- Directly accesses a database
- Writes to a file
- Modifies session state
- Mixes authentication, logging, and session management
