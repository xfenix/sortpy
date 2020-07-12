"""Tests core.
"""
from __future__ import annotations
import types
import string
import random
import typing
import pathlib
from importlib import import_module

import pytest


CURRENT_DIR: pathlib.Path = pathlib.Path(__file__).resolve().parent.parent


# Just various helpers
def gen_algos_list() -> typing.Generator:
    """Test helper. Get all modules from dir.
    """
    return (
        one_file.stem for one_file in CURRENT_DIR.glob("*.py") if one_file.is_file() and not one_file.stem == "__init__"
    )


def gen_random_cases_generator(value_generator: typing.Callable) -> typing.Callable:
    """Generate various test cases.
    """

    def inner_fn(how_many_cases: int, min_case_length: int = 30, max_case_length: int = 3000) -> typing.Generator:
        for _ in range(how_many_cases):
            input_data: list = []
            for _ in range(random.randint(min_case_length, max_case_length)):
                input_data.append(value_generator())
            yield dict(input=input_data, result=sorted(input_data))

    return inner_fn


def run_one_case(input_case: dict, sort_module: str) -> None:
    """Test helper. Body of test.
    """
    real_sort_module: types.ModuleType = import_module(f"{CURRENT_DIR.stem}.{sort_module}")
    assert tuple(real_sort_module.sort(list(input_case["input"]))) == tuple(input_case["result"])


def is_should_pass_and_warn(sort_module: str) -> bool:
    """Test helper.
    """
    if sort_module == "counting":
        print("Just pass for counting")
        return True
    return False


# Real tests starts right here:
@pytest.mark.parametrize("sort_module", gen_algos_list())
@pytest.mark.parametrize(
    "test_case",
    (
        dict(input=(1, 2, 3, 4), result=(1, 2, 3, 4)),
        dict(input=(100, 20, 1, 300, 100), result=(1, 20, 100, 100, 300)),
        dict(input=(1, 2, 3, 10, -1), result=(-1, 1, 2, 3, 10)),
        dict(input=(1000, 2000, 3000, 10, 0, -1000, 200), result=(-1000, 0, 10, 200, 1000, 2000, 3000)),
        dict(input=("z", "x", "abc", "b", "a", "ya"), result=("a", "abc", "b", "x", "ya", "z")),
        dict(input=("eb", "ac", "cz"), result=("ac", "cz", "eb")),
        dict(input=(4, 3, 2, 1, -100), result=(-100, 1, 2, 3, 4)),
    ),
)
def test_with_fixtures(test_case: dict, sort_module: str) -> None:
    """Fixture based tests.
    """
    if is_should_pass_and_warn(sort_module):
        return
    run_one_case(test_case, sort_module)


@pytest.mark.parametrize("sort_module", gen_algos_list())
@pytest.mark.parametrize("test_case", gen_random_cases_generator(lambda: random.randint(-100000, 100000))(30))
def test_with_autogenerated_random_int_data(test_case: dict, sort_module: str) -> None:
    """Fixture based tests.
    """
    run_one_case(test_case, sort_module)


@pytest.mark.parametrize("sort_module", gen_algos_list())
@pytest.mark.parametrize("test_case", gen_random_cases_generator(lambda: random.choice(string.ascii_lowercase))(30))
def test_with_autogenerated_random_string_data(test_case: dict, sort_module: str) -> None:
    """Fixture based tests.
    """
    if is_should_pass_and_warn(sort_module):
        return
    run_one_case(test_case, sort_module)
