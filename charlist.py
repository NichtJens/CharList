
class CharList(list):

    def __init__(self, s):
        list.__init__(self, s)

    @property
    def list(self):
        return list(self)

    @property
    def string(self):
        return "".join(self)

    def __setitem__(self, key, value):
        # handles single items and 
        # slices with step: obj[3:7:2], incl. obj[3:7:]
        # NB: regular slices (i.e., without step) are handled in __setslice__
        if isinstance(key, int) and len(value) != 1:
            cls = type(self).__name__
            raise ValueError("attempt to assign sequence of size {} to {} item of size 1".format(len(value), cls))
        super(CharList, self).__setitem__(key, value)

    def __str__(self):
        return self.string

    def __repr__(self):
        cls = type(self).__name__
        return "{}(\'{}\')".format(cls, self.string)


