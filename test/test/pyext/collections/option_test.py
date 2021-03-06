import unittest

from pyext.option import some, none


class OptionTest(unittest.TestCase):

    def testMap(self):
        x = some(5)
        x = x.map(lambda v: v + 5)
        self.assertEqual(x, some(5 + 5))

    def testFlatMap(self):
        x = some(5)
        x = x.flatmap(lambda v: some(v * 3))
        self.assertEqual(x, some(5 * 3))

    def testNoneMap(self):
        def unreachable():
            raise ValueError('Unreachable')

        x = none()
        x = x.map(unreachable)
        self.assertEqual(x, none())

    def testNoneFlatMap(self):
        def unreachable():
            raise ValueError('Unreachable')

        x = none()
        x = x.flatmap(unreachable)
        self.assertEqual(x, none())

    def testFilter(self):
        x = some(0)
        self.assertEqual(x, x.filter(lambda x: x != 0))
        self.assertEqual(none(), x.filter(lambda x: x == 0))
