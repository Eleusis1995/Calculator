# test_interface.py
import sys

import pytest
#print(sys.path)
sys.path.append('..')
import unittest
from unittest.mock import patch, Mock
from classes.calculatorclass import calculator
from user_interface import addtition, divition, multiplication, substraction


class TestInterface(unittest.TestCase):

    @patch('builtins.input', return_value = "15,10")
    def test_sum_interface(self, mock_input):
        """
        test to verify the interface addition function
        """
        # Probamos la función con el mock de Calculator
        resultado = addtition(calculator())
        # Verificamos que la función realizó la suma correctamente
        self.assertEqual(resultado, 'The addition is 25')

    @patch('builtins.input', return_value = "15,10")
    def test_sub_interface(self, mock_input):
        """
        test to verify the interface addition function
        """
        # Probamos la función con el mock de Calculator
        resultado = substraction(calculator())
        # Verificamos que la función realizó la suma correctamente
        self.assertEqual(resultado, 'The substraction is 5')

    @patch('builtins.input', return_value = "15,10")
    def test_mul_interface(self, mock_input):
        """
        test to verify the interface addition function
        """
        # Probamos la función con el mock de Calculator
        resultado = multiplication(calculator())
        # Verificamos que la función realizó la suma correctamente
        self.assertEqual(resultado, 'The multiplication is 150')

    @patch('builtins.input', return_value = "15,10")
    def test_div_interface(self, mock_input):
        """
        test to verify the interface addition function
        """
        # Probamos la función con el mock de Calculator
        resultado = divition(calculator())
        # Verificamos que la función realizó la suma correctamente
        self.assertEqual(resultado, 'The divition is 1.5')

    
