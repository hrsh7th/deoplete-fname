from .base import Base
from re import sub
from os.path import exists, basename

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)
        self.name = 'fname'
        self.mark = '[fname]'
        self.rank = 500
        self.is_volatile = True

    def gather_candidates(self, context):
        if not exists(context['bufpath']):
            return []
        name = basename(context['bufpath'])
        return [{
            'word': name,
            'dup': 1
        }, {
            'word': sub(r"\.[^\.]*$", '', name),
            'dup': 1
        }]

