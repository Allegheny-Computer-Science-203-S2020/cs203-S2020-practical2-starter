"""Test to ensure that the functions in the cookbook-style program are correct."""

from termfrequency import compute_tf_cookbook

# TODO: Add in at least four more test cases and assertions
# TODO: Make sure that you test as many functions as is possible
# TODO: Use the following test case as an example for your own tests


def test_read_file_populates_data_0():
    """Checks that the size of the input variable is correct."""
    # pylint: disable=len-as-condition
    assert len(compute_tf_cookbook.data) == 0
    compute_tf_cookbook.read_file("inputs/input.txt")
    assert len(compute_tf_cookbook.data) != 0
