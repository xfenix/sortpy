import random
from importlib import import_module
from unittest import TestCase


class BasicCase:
    def run_algo_case(self, sort_module):
        return None

    def run_case(self, test_cases, sort_module):
        module = import_module('xfsort.{}'.format(sort_module))
        for one_case in test_cases:
            self.assertEqual(tuple(module.sort(list(one_case['input']))),
                             tuple(one_case['result']))

    def test_quick(self):
        self.run_algo_case('quick')

    def test_bubble(self):
        self.run_algo_case('bubble')

    def test_merge(self):
        self.run_algo_case('merge')

    def test_insertion(self):
        self.run_algo_case('insertion')

    def test_heap(self):
        self.run_algo_case('heap')

    def test_shell(self):
        self.run_algo_case('shell')

    def test_counting(self):
        if not hasattr(self, 'is_fixture_case'):
            self.run_algo_case('counting')


class TestSortWithFixturesCase(TestCase, BasicCase):
    is_fixture_case = True
    algorithms = ('quick', 'bubble')
    test_cases = (
        dict(input=(100, 20, 1, 300, 100),
             result=(1, 20, 100, 100, 300)),
        dict(input=(1, 2, 3, 10, -1),
             result=(-1, 1, 2, 3, 10)),
        dict(input=(1000, 2000, 3000, 10, 0, -1000, 200),
             result=(-1000, 0, 10, 200, 1000, 2000, 3000)),
        dict(input=('z', 'x', 'abc', 'b', 'a', 'ya'),
             result=('a', 'abc', 'b', 'x', 'ya', 'z')),
    )

    def run_algo_case(self, sort_module):
        super().run_case(self.test_cases, sort_module)


class TestSortWithAutoRandomData(TestCase, BasicCase):
    total_cases = 30
    case_length_min = 100
    case_length_max = 3000

    def gen_cases(self):
        test_cases = []
        for _ in range(self.total_cases):
            input_data = []
            calc_case_length = random.randint(
                self.case_length_min, self.case_length_max)
            for _ in range(calc_case_length):
                input_data.append(random.randint(0, 100000))
            test_cases.append(
                dict(input=input_data, result=sorted(input_data)))
        return test_cases

    def run_algo_case(self, sort_module):
        super().run_case(self.gen_cases(), sort_module)
