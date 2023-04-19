import re

from password_strength import PasswordPolicy
from marshmallow import ValidationError

policy = PasswordPolicy.from_names(
    uppercase=1,  # need min. 1 uppercase letters
    numbers=1,  # need min. 1 digits
    special=1,  # need min. 1 special characters
    nonletters=1,  # need min. 1 non-letter characters (digits, specials, anything)
)


class Validation:
    @staticmethod
    def validate_card_number(number):
        if 16 < len(str(number)) > 19:
            raise ValidationError(
                "Invalid card number"
            )

    @staticmethod
    def validate_author(author):
        try:
            first_name, last_name = author.split()
        except ValueError:
            raise ValidationError(
                "Full name should consists of first and last name at least"
            )

        if len(first_name) < 2 or len(last_name) < 2:
            raise ValueError("Author should be at least 2 characters")

    @staticmethod
    def validate_password(value):
        errors = policy.test(value)
        if errors:
            raise ValidationError(f"Not a valid password")

    @staticmethod
    def validate_cvv(cvv):
        if len(str(cvv)) == 3 or len(str(cvv)) == 4:
            return cvv

        raise ValidationError("Invalid Card Verification Value Number")

    @staticmethod
    def phone_number_validation(value):
        pattern = "^\+[\+\d]?(\d{2,3}[-\.\s]??\d{2,3}[-\.\s]??\d{5}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d)"
        if re.match(pattern, value):
            return value

        raise ValidationError(
            "Phone number is not in the correct format. Please review it for any typos or mismatches."
        )

    @staticmethod
    def validate_email(email):
        pattern = "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"

        if re.match(pattern, email):
            return email

        raise ValidationError("Invalid Email")
