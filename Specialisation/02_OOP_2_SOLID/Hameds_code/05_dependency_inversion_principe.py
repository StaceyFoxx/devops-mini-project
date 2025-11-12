"""
DEPENDENCY INVERSION PRINCIPLE
(Not to be confused with DEPENDENCY INJECTION PRINCIPLE
which is slightly different by we're going to assume both to be same for now)

High-level modules should not depend on low-level modules.
Both should depend on abstractions (e.g. interfaces).
"""


# BAD EXAMPLE FIRST

# Low-level Module
class CreditCardPaymentProcessor:
    def process_credit_card_payment(self, amount):
        # Logic for processing credit card payment
        print(f"Processing credit card payment of ${amount}")

class DebitCardPaymentProcessor:
    def process_debit_card_payment(self, amount):
        # Logic for processing credit card payment
        print(f"Processing debit card payment of ${amount}")

class PaypalPaymentProcessor:
    def process_paypal_payment(self, amount):
        # Logic for processing credit card payment
        print(f"Processing Paypal payment of ${amount}")

# High-level Module
class Order:
    def __init__(self, credit_processor: CreditCardPaymentProcessor, debit_processor: DebitCardPaymentProcessor, paypal_processor:PaypalPaymentProcessor):
        self.credit_processor = credit_processor
        self.debit_processor = debit_processor
        self.paypal_processor = paypal_processor

    def checkout(self, amount, checkout_type):
        # Direct dependency on low-level module
        if checkout_type == "credit":
            self.credit_processor.process_credit_card_payment(amount)
        elif checkout_type == "debit":
            self.debit_processor.process_debit_card_payment(amount)
        elif checkout_type == "paypal":
            self.paypal_processor.process_paypal_payment(amount)



"""
### WHY IS IT BAD?
In this bad example, the Order class has a direct dependency on the low-level module 
CreditCardPaymentProcessor. This violates the Dependency Inversion Principle because 
the high-level module is directly dependent on a low-level module, and there's no use 
of an abstraction. If there are changes in the payment processing logic or if you want 
to introduce a different payment method, it would require modifications to the Order class.
"""

#############################################################################################
#############################################################################################
# GOOD EXAMPLE NOW
#############################################################################################
#############################################################################################


from abc import ABC, abstractmethod


# Abstraction (Interface)
class PaymentProcessor(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


# Low-level Module
class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # Logic for processing credit card payment
        print(f"Processing credit card payment of ${amount}")

class DebitCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # Logic for processing credit card payment
        print(f"Processing debit card payment of ${amount}")


# High-level Module
class Order:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor

    def checkout(self, amount):
        # Use the abstraction
        self.payment_processor.process_payment(amount)


"""
### WHY IS IT GOOD?
In this example, Order is the high-level module, and it depends on the abstraction 
PaymentProcessor. The CreditCardPaymentProcessor is a low-level module that implements 
the PaymentProcessor interface. This adheres to the Dependency Inversion Principle as 
the high-level module depends on an abstraction, and not directly on a low-level module.
"""
