"""
Calculator Module

This module provides basic arithmetic operations.
"""

class Calculator:
    """
    A simple calculator class.

    Methods
    -------
    add(a, b)
        Returns the sum of two numbers.

    subtract(a, b)
        Returns the difference of two numbers.

    multiply(a, b)
        Returns the product of two numbers.

    divide(a, b)
        Returns the quotient of two numbers.
    """

    def add(self, a, b):
        """
        Add two numbers.

        Parameters
        ----------
        a : float
            First number.
        b : float
            Second number.

        Returns
        -------
        float
            Sum of a and b.
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtract two numbers.

        Parameters
        ----------
        a : float
            First number.
        b : float
            Second number.

        Returns
        -------
        float
            Difference of a and b.
        """
        return a - b

    def multiply(self, a, b):
        """
        Multiply two numbers.

        Parameters
        ----------
        a : float
            First number.
        b : float
            Second number.

        Returns
        -------
        float
            Product of a and b.
        """
        return a * b

    def divide(self, a, b):
        """
        Divide two numbers.

        Parameters
        ----------
        a : float
            Numerator.
        b : float
            Denominator.

        Returns
        -------
        float
            Quotient of a and b.

        Raises
        ------
        ValueError
            If b is zero.
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b