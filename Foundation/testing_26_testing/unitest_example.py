from unittest import TestCase, main
from unittest import mock
from .test_example import red_or_blue, is_even, is_within_range, average_exam_score, get_file_content, calculate_total

# way to check what filepath to use
# print(__name__)

class TestRedOrBlueFunction(TestCase):

    def test_odd_numbers(self):
        expected = 'Red'
        result = red_or_blue(3)
        self.assertEqual(result, expected)

    def test_even_greater_than_twenty(self):
        expected = 'Blue'
        result = red_or_blue(26)
        self.assertEqual(result, expected)



class TestAverageExamScoreFunction(TestCase):

    def test_calculate_average(self):
        my_input = [
            {'name': 'Jane', 'mark': 7},
            {'name': 'Nitesh', 'mark': 6},
            {'name': 'Aisha', 'mark': 8},
            {'name': 'Zac', 'mark': 8},
        ]
        expected = 7.25
        result = average_exam_score(my_input)
        self.assertEqual(expected, result)

    def test_calculate_average_error_raised(self):
        my_input = [
            {'name': 'Jane', 'mark': 15},
            {'name': 'Nitesh', 'mark': 6},
            {'name': 'Aisha', },
            {'name': 'Zac', 'mark': '8'},
        ]
        with self.assertRaises(ValueError):
            average_exam_score(my_input)


class TestGetFileContentFunction(TestCase):

    @mock.patch('builtins.open', new_callable=mock.mock_open, read_data='1. Hello\n2. Hi\n3. Good Morning\n')
    def test_mock_file_read_function(self, mock_open):
        result = get_file_content('some_file')
        self.assertEqual( 4, result )


    #  folder names cannot start with numbers when targeting a function
    @mock.patch('Foundation.testing_26_testing.test_example.get_item_price', return_value=10)
    def test_calculate_total_with_mocked_price(self, mock_get_price):
        result = calculate_total("anything", 3)
        self.assertEqual(30, result )          # 10 * 3 = 30



if __name__ == '__main__':
    main()


#     test datatype - ie check it is a list, that the list is not empty
#  check that the list contians dictionaries, that two entries per dict
# name and mark keys
# does it raise an error if string provided


#  test ranges - marks should be within 1 and 10
#     and that it is not negative
#  check that it is integer , not a float

#  test default value set to 5 if no mark provided

# test functionality - calculate the correct average










