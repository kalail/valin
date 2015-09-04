import valin


class Provider(object):
        def __init__(self, name):
            self.name = name


@valin.typedtuple
class Ad(object):
    id = int
    layout = str
    provider = Provider


# validator = valin.create_validator({
#     'id must be a positive number': lambda ad: ad.id >= 1,
#     'layout must be at least 3 characters': lambda ad: len(ad.layout) >= 3,
# })


a = Ad(id=None, layout='as', provider='john')
Ad(id=1, layout='asd', provider=Provider('john'))
bad_ad = Ad(id=-1, layout='as', provider=Provider('john'))

# print validator(bad_ad)
