
class ValidationError(Exception):
    pass


def create_validator(validators):
    validators = dict(validators)
    print type(validators)
    print validators['id'](1)

    if not all(map(callable, validators.values())):
        raise TypeError('all validators must be callables')

    def validator(obj):
        for v in validators.values():
            print v(obj)
        try:
            return [validation for validation, validator in validators.items() if not validator(obj)]
        except Exception as e:
            raise ValidationError(e)

    return validator


def is_valid_url():
    pass


def validator():
    pass


@validator
class Validator:
    media_url = [
        is_valid_url,
    ]

    object = [
        field_present_if('media_url', lambda o: o.provider != 'disqus'),
    ]


Validator()
