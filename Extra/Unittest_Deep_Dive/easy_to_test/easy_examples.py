# Example 1: Pure Function - String Processing
def reverse_words(text):
    """Reverses the order of words in a string."""
    words = text.split()
    return " ".join(reversed(words))


# Example 2: Pure Function - Mathematical Operation
def calculate_bmi(weight_kg, height_m):
    """Calculate Body Mass Index given weight in kg and height in meters."""
    if height_m <= 0:
        raise ValueError("Height must be positive")
    return weight_kg / (height_m ** 2)


# Example 3: Business Logic with Clear Contract
def apply_discount(price, discount_percentage):
    """Apply a discount percentage to a price."""
    if not 0 <= discount_percentage <= 100:
        raise ValueError("Discount percentage must be between 0 and 100")

    discount_factor = discount_percentage / 100
    return price * (1 - discount_factor)


# Example 4:  Function with Configurable Behavior
def create_greeting(name, greeting_template="{name}, welcome!"):
    """Creates a personalized greeting message."""
    return greeting_template.replace("{name}", name)


# Example 5: Data Transformation
def format_phone_number(number):
    """Format a 10-digit phone number to (XXX) XXX-XXXX format."""
    # Convert to string and remove any non-digit characters
    digits = ''.join(filter(str.isdigit, str(number)))

    if len(digits) != 10:
        raise ValueError("Phone number must contain exactly 10 digits")

    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
