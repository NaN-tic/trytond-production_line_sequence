# This file is part stock_move_extra_products_supply module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['Production']
__metaclass__ = PoolMeta


class Production:
    __name__ = "production"

    def _explode_move_values(self, from_location, to_location, company,
            bom_io, quantity):
        move = super(Production, self)._explode_move_values(from_location,
            to_location, company, bom_io, quantity)
        move.sequence = bom_io.sequence if bom_io else 1
        return move
