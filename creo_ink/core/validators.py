from django.core.validators import RegexValidator

custom_username_validators = [RegexValidator(
    regex="^[\w]*$",
    message="Only use ASCI letters"
)]
