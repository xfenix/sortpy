import random
from importlib import import_module
from unittest import TestCase


class BasicCase(TestCase):
    def _run_algo_case(self, test_cases, sort_module):
        module = import_module('xfsort.{}'.format(sort_module))
        for one_case in test_cases:
            self.assertEqual(tuple(module.sort(list(one_case['input']))),
                             tuple(one_case['result']))


class TestSortWithFixturesCase(BasicCase):
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

    def _run_algo_case(self, sort_module):
        super()._run_algo_case(self.test_cases, sort_module)

    def test_quick(self):
        self._run_algo_case('quick')

    def test_bubble(self):
        self._run_algo_case('bubble')

    def test_merge(self):
        self._run_algo_case('merge')

    def test_heap(self):
        self._run_algo_case('heap')


class TestSortWithAutoRandomData(BasicCase):
    total_cases = 30
    case_length_min = 900
    case_length_max = 5000

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

    def _run_algo_case(self, sort_module):
        super()._run_algo_case(self.gen_cases(), sort_module)

    def test_quick(self):
        self._run_algo_case('quick')

    def test_heap(self):
        self._run_algo_case('heap')
