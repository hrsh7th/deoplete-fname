from .base import Base
from re import sub
from os.path import exists, basename

class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)
        self.name = 'fname'
        self.mark = '[fname]'
        self.rank = 500

    def get_complete_position(self, context):
        return len(context['input']) + 1

    def gather_candidates(self, context):
        if not exists(context['bufpath']):
            return []
        name = basename(context['bufpath'])
        return [{'word': name, 'menu': 'fn'}, {'word': sub(r"\..*?$", '', name), 'menu': 'fn'}]

