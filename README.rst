Model your data like this::

    import valin

    class Provider(object):
        def __init__(self, name):
            self.name = name

    @valin.Model
    class Ad(object):
        id = int
        layout = str
        provider = Provider


    ad = Ad(layout='thumbnail')                                     # Fails due to missing keys!
    ad = Ad(id='asdf', layout='thumbnail', provider='john')         # Fails due to mismatched types!
    ad = Ad(id=1, layout='thumbnail', provider=Provider('john'))    # Works!

    ad  # type verified lightweight namedtuple
