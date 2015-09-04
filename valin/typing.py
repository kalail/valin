from collections import namedtuple


def create_typedtuple(name, fields):
    try:
        # assert type safety
        name = str(name)
        fields = dict(fields)

        for field, _type in fields.items():

            if not isinstance(field, str):
                raise TypeError('fields must be of type {}'.format(str))

            if not isinstance(_type, type):
                raise TypeError('field type `{}` is not a supported type'.format(_type))

        _tuple = namedtuple(name, fields.keys())

    except Exception as e:
        raise TypeError(e)

    def constructor(**kwargs):
        obj = _tuple(**kwargs)  # raises TypeError

        # fields must have the specified types
        for field, _type in fields.items():
            value = getattr(obj, field)
            if not isinstance(value, _type):
                raise TypeError('field \'{}\' expects type {}, got {}'.format(field, _type, type(value)))

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
