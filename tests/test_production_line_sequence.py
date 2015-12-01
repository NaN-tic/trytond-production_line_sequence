# This file is part of the production_line_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class ProductionLineSequenceTestCase(ModuleTestCase):
    'Test Production Line Sequence module'
    module = 'production_line_sequence'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        ProductionLineSequenceTestCase))
    return suite