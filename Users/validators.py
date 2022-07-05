from django.core.exceptions import ValidationError


def validate_latitude(value):
    if value < -90.0 or value > 90.0:
        raise ValidationError('latitude must be in the range [-90, 90]')


def validate_longitude(value):
    if value < -180.0 or value > 180.0:
        raise ValidationError('longitude must be in the range [-180, 180]')


def validate_phone(value):
    if len(value) < 11:
        raise ValidationError('Iranian cell phone number contains 11 digits (including 0)')
    elif value[:2] != '09':
        raise ValidationError('Iranian cell phone number starts with 09 (09XX XXX XX XX)')
