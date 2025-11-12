# Examples of Highly Testable Python Functions

Here are several examples of well-designed, testable Python functions along with explanations of what makes them good for testing:

## Example 1: Pure Function - String Processing

```python
def reverse_words(text):
    """Reverses the order of words in a string."""
    words = text.split()
    return " ".join(reversed(words))
```

**Why it's easy to test:**
- Has a clear input and output
- No side effects or state mutation
- Deterministic (same input always produces same output)
- Single responsibility

## Example 2: Pure Function - Mathematical Operation

```python
def calculate_bmi(weight_kg, height_m):
    """Calculate Body Mass Index given weight in kg and height in meters."""
    if height_m <= 0:
        raise ValueError("Height must be positive")
    return weight_kg / (height_m ** 2)
```

**Why it's easy to test:**
- Clear inputs and output
- Handles edge cases explicitly
- Predictable error behavior
- No external dependencies

## Example 3: Business Logic with Clear Contract

```python
def apply_discount(price, discount_percentage):
    """Apply a discount percentage to a price.
    
    Args:
        price: Original price (float)
        discount_percentage: Percentage discount between 0 and 100
        
    Returns:
        Discounted price
    
    Raises:
        ValueError: If discount is not between 0 and 100
    """
    if not 0 <= discount_percentage <= 100:
        raise ValueError("Discount percentage must be between 0 and 100")
    
    discount_factor = discount_percentage / 100
    return price * (1 - discount_factor)
```

**Why it's easy to test:**
- Clear documentation of behavior
- Input validation with specific error messages
- Handles edge cases
- Follows a simple algorithm that can be verified

## Example 4: Class Method with Dependency Injection

```python
class OrderProcessor:
    def __init__(self, payment_gateway, email_service):
        self.payment_gateway = payment_gateway
        self.email_service = email_service
    
    def process_order(self, order):
        """Process payment for an order and send confirmation email."""
        if not order.is_valid():
            return False
        
        payment_successful = self.payment_gateway.charge(
            order.customer_id, 
            order.total_amount
        )
        
        if payment_successful:
            self.email_service.send_confirmation(
                order.customer_email,
                f"Your order #{order.id} has been processed."
            )
            return True
        
        return False
```

**Why it's easy to test:**
- Dependencies are injected via constructor
- External services can be easily mocked
- Single responsibility (processing an order)
- No direct interaction with external systems

## Example 5: Factory Function with Configurable Behavior

```python
def create_greeting(name, greeting_template="{name}, welcome!"):
    """Creates a personalized greeting message.
    
    Args:
        name: Person's name
        greeting_template: Template string with {name} placeholder
    
    Returns:
        Formatted greeting string
    """
    return greeting_template.replace("{name}", name)
```

**Why it's easy to test:**
- Default arguments can be overridden in tests
- Configurable behavior
- Simple string manipulation that's easy to verify

## Example 6: Stateless Data Transformation

```python
def format_phone_number(number):
    """Format a 10-digit phone number to (XXX) XXX-XXXX format.
    
    Args:
        number: String or int containing exactly 10 digits
        
    Returns:
        Formatted phone number string
        
    Raises:
        ValueError: If input doesn't contain exactly 10 digits
    """
    # Convert to string and remove any non-digit characters
    digits = ''.join(filter(str.isdigit, str(number)))
    
    if len(digits) != 10:
        raise ValueError("Phone number must contain exactly 10 digits")
    
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
```

**Why it's easy to test:**
- Handles input normalization
- Explicit validation with descriptive errors
- Output format is consistent and verifiable
- No external dependencies

## Example 7: State Machine with Predictable Transitions

```python
class TrafficLight:
    STATES = ["RED", "YELLOW", "GREEN"]
    
    def __init__(self):
        self.current_state_index = 0
    
    @property
    def current_state(self):
        return self.STATES[self.current_state_index]
    
    def change_state(self):
        """Move to the next state in the traffic light cycle."""
        self.current_state_index = (self.current_state_index + 1) % len(self.STATES)
        return self.current_state
```

**Why it's easy to test:**
- Encapsulated state with clear transitions
- Deterministic behavior
- Can easily verify each state transition
- Simple initialization

## Example 8: Function with Callbacks

```python
def process_items(items, process_func, on_success=None, on_error=None):
    """Process a list of items with the given function.
    
    Args:
        items: List of items to process
        process_func: Function to apply to each item
        on_success: Optional callback for successful processing
        on_error: Optional callback for error handling
        
    Returns:
        Dictionary with successful and failed items
    """
    results = {"success": [], "errors": []}
    
    for item in items:
        try:
            result = process_func(item)
            results["success"].append(result)
            if on_success:
                on_success(item, result)
        except Exception as e:
            results["errors"].append((item, str(e)))
            if on_error:
                on_error(item, e)
    
    return results
```

**Why it's easy to test:**
- Callbacks can be mocked to verify they're called correctly
- Returns structured results that can be verified
- Handles errors gracefully
- Flexible behavior through function composition

These examples showcase key principles of testable code:
- Clear inputs and outputs
- Dependency injection
- Single responsibility
- No side effects
- Error handling
- Limited scope
- Separation of concerns

Testing these functions would be straightforward with unittest or pytest, making them excellent examples for teaching testable code