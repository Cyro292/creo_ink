from django.core.validators import RegexValidator

custom_username_validators = [RegexValidator(
    regex="^[\w_.]*$",
    message="Only use ASCI letters"
)]

username_validators = [RegexValidator(
    regex="^[\w_.#]*$",
    message="Only use ASCI letters"
)]
