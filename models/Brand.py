#! python3

from .Model import Model


class Brand(Model):

    def __init__(self):
        super(Brand, self).__init__()
        self.table = 'brands'

