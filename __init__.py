# This file is part of the production_line_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .bom import *
from .production import *


def register():
    Pool.register(
        BOMInput,
        BOMOutput,
        Production,
        module='production_line_sequence', type_='model')
