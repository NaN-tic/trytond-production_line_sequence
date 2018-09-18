# This file is part of the production_line_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import bom
from . import production


def register():
    Pool.register(
        bom.BOMInput,
        bom.BOMOutput,
        production.Production,
        module='production_line_sequence', type_='model')
