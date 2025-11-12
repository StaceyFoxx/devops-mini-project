## Example 2: Direct System Interactions

```python
def save_user_data(user_data):
    with open("users.txt", "a") as file:
        file.write(f"{user_data['name']},{user_data['email']}\n")
    print(f"User {user_data['name']} saved successfully!")
    return True
```

**Why it's hard to test:**
- Directly interacts with the file system
- Has a side effect (printing to console)
- Tests would create actual files on the system
- No way to easily mock the file operations

## Example 3: Time-Dependent Behavior

```python
def is_weekend():
    day = datetime.datetime.now().weekday()
    return day >= 5  # 5 = Saturday, 6 = Sunday
```

**Why it's hard to test:**
- Result depends on when the test is run
- Impossible to test all scenarios (would need to wait for weekend)
- No way to inject or control the current date/time

## Example 4: External API Calls

```python
def get_weather(city):
    url = f"https://api.weather.com/forecast?city={city}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["temperature"]
    else:
        return "Could not fetch weather data"
```

**Why it's hard to test:**
- Makes actual HTTP requests to external service
- Depends on network connectivity
- Depends on external API availability and response format
- May have rate limiting or costs associated with calls

## Example 5: Random Behavior

```python
def generate_random_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(12))
    return password
```

**Why it's hard to test:**
- Output is non-deterministic
- Cannot verify exact expected output
- Can only test password length or character set inclusion

## Example 6: Singleton or Static Methods (Will teach this in Specialisation later)

```python
class DatabaseManager:
    _instance = None
    
    @staticmethod
    def get_instance():
        if DatabaseManager._instance is None:
            DatabaseManager._instance = DatabaseManager()
        return DatabaseManager._instance
    
    def query(self, sql):
        # Execute SQL against a real database
        conn = sqlite3.connect("production.db")
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        conn.close()
        return result
```

**Why it's hard to test:**
- Singleton pattern makes it difficult to replace with test doubles
- Direct database connection
- No way to inject test dependencies

## Example 7: Multiple Responsibilities

```python
def process_order(order_id):
    # Get order from database
    db = sqlite3.connect("shop.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM orders WHERE id = ?", (order_id,))
    order = cursor.fetchone()
    
    # Validate order
    if not order or order[3] != "PENDING":
        return False
    
    # Process payment
    payment_api = PaymentGateway("api_key_12345")
    success = payment_api.charge(order[2])  # amount
    
    # Update order status
    if success:
        cursor.execute("UPDATE orders SET status = 'PAID' WHERE id = ?", (order_id,))
        db.commit()
        
        # Send email
        smtp = smtplib.SMTP("smtp.example.com")
        smtp.send_message(f"Order {order_id} has been processed")
        smtp.quit()
        
    db.close()
    return success
```

**Why it's hard to test:**
- Mixes database operations, payment processing, and email sending
- Has hardcoded dependencies
- Multiple side effects
- No separation of concerns

These examples highlight common patterns that make functions difficult to test. When teaching testing, you can use these as "before" examples, then show how to refactor them to make them testable.