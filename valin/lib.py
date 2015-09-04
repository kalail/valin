from collections import namedtuple

from .validation import create_validator


def create_typedtuple(name, fields):
    name = str(name)
    fields = dict(fields)

    for field_1, _type in fields.items():

        if not isinstance(field_1, str):
            raise TypeError('fields must be of type {}'.format(str))

        if not isinstance(_type, type):
            raise TypeError('field type `{}` is not a supported type'.format(_type))

    _tuple = namedtuple(name, fields.keys())
    print fields

    _validators = {}
    for field_2, _type in fields.items():
        def validator(_obj):
            return isinstance(getattr(_obj, field_2), _type)
        _validators[field_2] = validator

    print _validators['layout']('asd')

    validator = create_validator(_validators)

    def constructor(**kwargs):
        obj = _tuple(**kwargs)  # raises TypeError
        print obj

        errors = validator(obj)

        if errors:
            raise TypeError('field type errors: ' + ', '.join('\'{}\' expected {} got {}'.format(_field, fields[_field], type(getattr(obj, _field))) for _field in errors))

        # object is valid
        return obj

    # Modify constructor name and return
    constructor.func_name = name
    return constructor


def typedtuple(cls):
    return create_typedtuple(cls.__name__, {
            field: getattr(cls, field)
            for field in dir(cls)
            if not field.startswith('_')
    })
