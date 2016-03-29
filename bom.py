# This file is part of the production_line_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
__all__ = ['BOMInput', 'BOMOutput']


class BOMInput:
    __metaclass__ = PoolMeta
    __name__ = 'production.bom.input'
    sequence = fields.Integer('Sequence')

    @classmethod
    def __setup__(cls):
        super(BOMInput, cls).__setup__()
        cls._order.insert(0, ('sequence', 'ASC'))


class BOMOutput:
    __metaclass__ = PoolMeta
    __name__ = 'production.bom.output'
    sequence = fields.Integer('Sequence')

    @classmethod
    def __setup__(cls):
        super(BOMOutput, cls).__setup__()
        cls._order.insert(0, ('sequence', 'ASC'))
