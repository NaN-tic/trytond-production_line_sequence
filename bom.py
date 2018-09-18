# This file is part of the production_line_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields, sequence_ordered
from trytond.pool import PoolMeta

__all__ = ['BOMInput', 'BOMOutput']


class BOMInput(sequence_ordered(), metaclass=PoolMeta):
    __name__ = 'production.bom.input'


class BOMOutput(sequence_ordered(), metaclass=PoolMeta):
    __name__ = 'production.bom.output'
