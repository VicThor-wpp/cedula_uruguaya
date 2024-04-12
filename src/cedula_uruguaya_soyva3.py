import random
import re

class CedulaUruguaya:
    """A holistic class for managing the numerological fate of Uruguayans—namely, their ID numbers. 
    Like the universe itself, this class adds a sprinkle of order to the chaos of numbers."""

    @staticmethod
    def get_validation_digit(ci):
        """Dances with the digits of a Uruguayan ID to find that one cosmic number that holds the balance.
        
        Everything in the universe follows a pattern, ID numbers included. This method does a little
        jig with the digits, summing their modular products, to uncover the digit that completes the
        numerical harmony of the ID.

        Args:
            ci (int): The ID number without its last verification digit.

        Returns:
            int: The verification digit, a numeric balancer of the cosmic equation.
            Example: For ci = 3298763 -> returns 4
        """
        a = 0
        ci_str = str(ci).zfill(7)  # The universe prefers 7-digit numbers.
        for i in range(7):
            a += (int("2987634"[i]) * int(ci_str[i])) % 10
        return 0 if a % 10 == 0 else 10 - a % 10

    @staticmethod
    def clean_ci(ci):
        """Purifies the ID from any earthly impurities like dots and dashes.
        
        In this chaotic universe, an ID might be hidden behind symbols and signs. This method strips them away,
        revealing the true numeric essence of the ID.

        Args:
            ci (str/int): The ID in its earthly form, possibly tainted.

        Returns:
            int: The ID in its pure, numeric form.
            Example: For ci = '3.298.763-4' -> returns 32987634
        """
        return int(str(ci).replace("-", "").replace('.', ''))

    @staticmethod
    def validate_ci(ci):
        """Validates the ID in an act of cosmic confirmation of its authenticity.
        
        Just as the universe seeks balance, this method checks if the final digit of an ID coincides
        with the cosmic digit calculated. It's like confirming if the stars are aligned for that ID.

        Args:
            ci (str/int): The complete ID, seeking validation.

        Returns:
            bool: True if the ID echoes universal order, False otherwise.
            Example: For ci = '3.298.763-4' -> returns True
        """
        ci_str = str(CedulaUruguaya.clean_ci(ci))
        digit = int(ci_str[-1])
        ci_without_digit = int(ci_str[:-1])
        return digit == CedulaUruguaya.get_validation_digit(ci_without_digit)

    @staticmethod
    def format_ci(ci):
        """Formats the ID number into a visually friendly format, like X.XXX.XXX-X.
        
        Sometimes, even numbers need a little help to look their best in social situations.
        
        Args:
            ci (int/str): The ID number to be formatted.

        Returns:
            str: The ID, dressed up in its best format.
            Example: For ci = 32987634 -> returns '3.298.763-4'
        """
        ci_str = str(CedulaUruguaya.clean_ci(ci))
        return f"{ci_str[:-1][:-6]}.{ci_str[:-1][-6:-3]}.{ci_str[:-1][-3:]}-{ci_str[-1]}"

    @staticmethod
    def random_ci_in_range(start=1000000, end=2000000):
        """Generates a random ID within a specific numeric range—fate, with a hint of direction.
        
        Args:
            start (int): The lower bound of the range.
            end (int): The upper bound of the range.

        Returns:
            int: A randomly generated, yet cosmically validated ID.
            Example: For start = 1000000, end = 2000000 -> might return 12345678
        """
        ci = random.randint(start, end)
        return int(f"{ci}{CedulaUruguaya.get_validation_digit(ci)}")

    @staticmethod
    def international_format(ci):
        """Converts the ID to an international format that includes the country code, like 'UY-X.XXX.XXX-X'.
        
        For when your ID needs to travel internationally.
        
        Args:
            ci (int/str): The ID to be converted.

        Returns:
            str: The ID, ready for its international adventures.
            Example: For ci = 32987634 -> returns 'UY-3.298.763-4'
        """
        return "UY-" + CedulaUruguaya.format_ci(ci)

    @staticmethod
    def bulk_validate_ci(ci_list):
        """Validates a list of IDs in one fell swoop. Ideal for when you have many IDs and little time.
        
        Args:
            ci_list (list): A list of IDs to be validated.

        Returns:
            dict: A dictionary with IDs as keys and validation results as values.
            Example: For ci_list = ['3.298.763-4', '1.234.567-8'] -> returns {'32987634': True, '12345678': False}
        """
        return {ci: CedulaUruguaya.validate_ci(ci) for ci in ci_list}

    @staticmethod
    def extract_ci_from_text(text):
        """Extracts ID numbers from text using regular expressions, useful for processing documents.
        
        Args:
            text (str): The text containing potential ID numbers.

        Returns:
            list: A list of extracted and cleaned ID numbers, if they are valid.
            Example: For text = 'Mi CI es 3.298.763-4 y la tuya es 1.234.567-8' -> returns [32987634]
        """
        matches = re.findall(r"\b\d{1,3}\.?\d{3}\.?\d{3}[-\d]\d\b", text)
        return [CedulaUruguaya.clean_ci(match) for match in matches if CedulaUruguaya.validate_ci(match)]
