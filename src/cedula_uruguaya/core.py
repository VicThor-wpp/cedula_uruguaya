import random
import re
from typing import Dict, List, Union

# Constants
WEIGHTS = [2, 9, 8, 7, 6, 3, 4]


def get_validation_digit(ci: int) -> int:
    """
    Calculates the validation digit for a given Uruguayan ID number.

    Args:
        ci (int): The ID number without the verification digit.
                  It must be an integer. If the ID has fewer than 7 digits,
                  it is treated as if it were padded with leading zeros.

    Returns:
        int: The calculated validation digit (0-9).
    """
    ci_str = str(ci)

    # Pad with zeros to ensure 7 digits for the calculation (though usually up to 7)
    # The algorithm requires aligning with the weights.
    # Standard Uruguay CI (old format) had fewer digits, new ones are 8 digits
    # total (7 + digit). If the number provided is the first 7 digits (or fewer),
    # we pad to 7.
    ci_str = ci_str.zfill(7)

    if len(ci_str) > 7:
        # Handle cases where input might be unexpectedly longer, though standard is
        # 7 digits + check. For robustness, we take the last 7 digits if it's too long,
        # or raise error? Given "robustness", let's assume valid 7-digit input logic.
        # If >7, it might be an issue. But let's stick to the standard algorithm which
        # iterates 7 times. If we strictly follow the algorithm:
        ci_str = ci_str[-7:]

    total = 0
    for i in range(7):
        digit = int(ci_str[i])
        weight = WEIGHTS[i]
        total += (digit * weight) % 10

    remainder = total % 10
    return 0 if remainder == 0 else 10 - remainder


def clean_ci(ci: Union[str, int]) -> int:
    """
    Removes non-numeric characters from the ID.

    Args:
        ci (Union[str, int]): The ID number, possibly containing delimiters
                              (dots, hyphens).

    Returns:
        int: The numeric representation of the ID.
    """
    # Remove all non-digit characters
    cleaned = re.sub(r"\D", "", str(ci))
    if not cleaned:
        raise ValueError("Input does not contain any digits.")
    return int(cleaned)


def validate_ci(ci: Union[str, int]) -> bool:
    """
    Validates a complete Uruguayan ID number (including the verification digit).

    Args:
        ci (Union[str, int]): The complete ID number.

    Returns:
        bool: True if the ID is valid, False otherwise.
    """
    try:
        ci_cleaned = str(clean_ci(ci))
    except ValueError:
        return False

    # A valid CI must have at least 2 digits (1 number + 1 check digit)?
    # Technically 1 digit CI + check is possible (very old).
    if len(ci_cleaned) < 2:
        return False

    check_digit = int(ci_cleaned[-1])
    number_part = int(ci_cleaned[:-1])

    expected_digit = get_validation_digit(number_part)
    return check_digit == expected_digit


def format_ci(ci: Union[int, str]) -> str:
    """
    Formats the ID number into the standard format 'X.XXX.XXX-X'.

    Args:
        ci (Union[int, str]): The ID number.

    Returns:
        str: The formatted ID string.
    """
    ci_str = str(clean_ci(ci))

    # Pad to at least 2 digits to have a check digit and a number
    if len(ci_str) < 2:
        return ci_str  # Return as is if too short to format properly

    # The check digit is the last one
    check_digit = ci_str[-1]
    number_part = ci_str[:-1]

    # Format the number part with dots
    # We can use standard string formatting for thousands separator, then
    # replace comma with dot providing we are in a locale where comma is thousands sep
    # or just force it. Python's f"{x:,}" uses comma.

    formatted_number = f"{int(number_part):,}".replace(",", ".")

    return f"{formatted_number}-{check_digit}"


def random_ci_in_range(start: int = 1_000_000, end: int = 2_000_000) -> int:
    """
    Generates a valid random Uruguayan ID number within a specified range.

    Args:
        start (int): The lower bound of the range (inclusive) for the number part.
        end (int): The upper bound of the range (inclusive) for the number part.

    Returns:
        int: A valid ID number including the verification digit.
    """
    number_part = random.randint(start, end)
    digit = get_validation_digit(number_part)
    return int(f"{number_part}{digit}")


def international_format(ci: Union[int, str]) -> str:
    """
    Formats the ID with the international country code prefix 'UY-'.

    Args:
        ci (Union[int, str]): The ID number.

    Returns:
        str: The ID in international format (e.g., 'UY-1.234.567-8').
    """
    return f"UY-{format_ci(ci)}"


def bulk_validate_ci(ci_list: List[Union[str, int]]) -> Dict[Union[str, int], bool]:
    """
    Validates a list of ID numbers.

    Args:
        ci_list (List[Union[str, int]]): A list of ID numbers to validate.

    Returns:
        Dict[Union[str, int], bool]: A dictionary mapping the original input ID
                                     to its validation result.
    """
    return {ci: validate_ci(ci) for ci in ci_list}


def extract_ci_from_text(text: str) -> List[int]:
    """
    Extracts valid ID numbers from a text string.

    Args:
        text (str): The input text.

    Returns:
        List[int]: A list of cleaned, valid ID numbers found in the text.
    """
    # Regex to match patterns that look like CIs
    # Matches:
    # - 1 to 3 digits
    # - Optional dot
    # - 3 digits
    # - Optional dot
    # - 3 digits
    # - Hyphen or digit (to cover "12345678" or "1.234.567-8")
    # This regex is a bit simplistic, let's make it robust for finding sequences.
    # The original regex was: r"\b\d{1,3}\.?\d{3}\.?\d{3}[-\d]\d\b"
    # This expects close to 1 million and up (7 digits + check).

    matches = re.findall(r"\b\d{1,3}(?:\.?\d{3}){2}(?:-|\d)\d\b", text)

    valid_cis = []
    for match in matches:
        try:
            # We clean it first to get the integer
            cleaned = clean_ci(match)
            # Then validate
            if validate_ci(cleaned):
                valid_cis.append(cleaned)
        except ValueError:
            continue

    return valid_cis
