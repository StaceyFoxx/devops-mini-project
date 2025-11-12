import unittest
from easy_examples import reverse_words, calculate_bmi, apply_discount, create_greeting, format_phone_number


class TestEasyExampleFunctions(unittest.TestCase):
    """Test cases for all the testable function examples."""

    # Tests for Example 1: reverse_words
    def test_reverse_words_normal_case(self):
        self.assertEqual(reverse_words("hello world"), "world hello")

    def test_reverse_words_empty_string(self):
        self.assertEqual(reverse_words(""), "")

    def test_reverse_words_single_word(self):
        self.assertEqual(reverse_words("hello"), "hello")

    def test_reverse_words_multiple_spaces(self):
        self.assertEqual(reverse_words("hello  world  python"), "python world hello")

    def test_reverse_words_type_error(self):
        with self.assertRaises(AttributeError):
            reverse_words(666)

    # Tests for Example 2: calculate_bmi
    def test_calculate_bmi_normal(self):
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.86, places=2)

    def test_calculate_bmi_zero_height(self):
        with self.assertRaises(ValueError):
            calculate_bmi(70, 0)

    def test_calculate_bmi_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_bmi(70, -1.75)

    # Tests for Example 3: apply_discount
    def test_apply_discount_no_discount(self):
        self.assertEqual(apply_discount(100, 0), 100)

    def test_apply_discount_full_discount(self):
        self.assertEqual(apply_discount(100, 100), 0)

    def test_apply_discount_half_discount(self):
        self.assertEqual(apply_discount(100, 50), 50)

    def test_apply_discount_negative_discount(self):
        with self.assertRaises(ValueError):
            apply_discount(100, -10)

    def test_apply_discount_over_100_percent(self):
        with self.assertRaises(ValueError):
            apply_discount(100, 110)

    # Tests for Example 4: create_greeting

    def test_create_greeting_default_template(self):
        self.assertEqual(create_greeting("John"), "John, welcome!")

    def test_create_greeting_custom_template(self):
        template = "Hello, {name}! How are you today?"
        self.assertEqual(
            create_greeting("John", template),
            "Hello, John! How are you today?"
        )

    def test_create_greeting_empty_name(self):
        self.assertEqual(create_greeting(""), ", welcome!")

    # Tests for Example 5: format_phone_number
    def test_format_phone_number_normal(self):
        self.assertEqual(format_phone_number("1234567890"), "(123) 456-7890")

    def test_format_phone_number_with_non_digits(self):
        self.assertEqual(format_phone_number("(123) 456-7890"), "(123) 456-7890")

    def test_format_phone_number_with_too_few_digits(self):
        with self.assertRaises(ValueError):
            format_phone_number("123456789")

    def test_format_phone_number_with_too_many_digits(self):
        with self.assertRaises(ValueError):
            format_phone_number("12345678901")

    def test_format_phone_number_numeric_input(self):
        self.assertEqual(format_phone_number(1234567890), "(123) 456-7890")


if __name__ == "__main__":
    unittest.main()
