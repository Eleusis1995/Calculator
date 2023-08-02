import pytest
from ..calculatorclass import calculator
class TestCalculatorClass:
    """Class to test the different functionalities of calculator"""
    def setup_method(self):
        """
        General variables and setups
        """
        self.local_calculator = calculator()

    def test_sum_two_positive_nums(self):
        """
        Test basic_operation_sum method with two numbers
        """
        result = self.local_calculator.basic_operation_sum(14,20)
        assert result == 34

    def test_sum_positive_list_nums(self):
        """
        Test basic_operation_sum method with a list of numbers
        """
        nums = [2,5,23,9,1,2]
        result = self.local_calculator.basic_operation_sum(*nums)
        expected = sum(nums)
        assert result == expected

    def test_sub_positive_result(self):
        """
        """
        result = self.local_calculator.basic_operation_sub(30,15)
        assert result == 15

    @pytest.mark.test_mul
    @pytest.mark.parametrize("Num1, Num2, Expected_result", 
                            [(10, 10, 100), 
                            (20, -3, -60),
                            ([10,20,30],[10,20,30], 36000000)])
    def test_mul(self, Num1, Num2, Expected_result):
        """
        """
        if isinstance(Num1, list) and isinstance(Num2, list):
            result = self.local_calculator.basic_operation_mul(*Num1,*Num2)
        else:
            result = self.local_calculator.basic_operation_mul(Num1,Num2)
        assert result == Expected_result

    @pytest.mark.divition
    @pytest.mark.parametrize("Num1, Num2, Expected_result", 
                            [(5, 2, 2.5), 
                            (2, -5, -0.4)])
    def test_correct_div(self, Num1, Num2, Expected_result):
        """
        """
        result = self.local_calculator.basic_operation_dev(Num1,Num2)
        assert result == Expected_result

    @pytest.mark.divition
    def test_error_div(self):
        """
        """
        Expected_result = "NOT possitble devide by 0"
        with pytest.raises(ZeroDivisionError) as expec:
            self.local_calculator.basic_operation_dev(6,0)
        assert str(expec.value) == Expected_result


