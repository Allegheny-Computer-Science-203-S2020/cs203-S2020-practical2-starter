"""Test to ensure that the functions in the cookbook-style program are correct."""

from termfrequency import compute_tf_cookbook


def test_read_file_populates_data_0():
    """Checks that the size of the input variable is correct."""
    # pylint: disable=len-as-condition
    assert len(compute_tf_cookbook.data) == 0
    compute_tf_cookbook.read_file("inputs/input.txt")
    assert len(compute_tf_cookbook.data) != 0


def test_file_contains_singleline_comment_count_1():
    """Checks that the singleline comment count works."""
    # pylint: disable=len-as-condition
    compute_tf_cookbook.read_file("inputs/input.txt")
    assert len(compute_tf_cookbook.data) != 0


def test_file_contains_singleline_comment_count_2():
    """Checks that the singleline comment count works."""
    # pylint: disable=len-as-condition
    compute_tf_cookbook.read_file("inputs/input.txt")
    assert len(compute_tf_cookbook.data) != 0


def test_file_contains_singleline_comment_count_3():
    """Checks that the singleline comment count works."""
    # pylint: disable=len-as-condition
    compute_tf_cookbook.read_file("inputs/input.txt")
    assert len(compute_tf_cookbook.data) != 0


def test_file_contains_singleline_comment_count_4():
    """Checks that the singleline comment count works."""
    # pylint: disable=len-as-condition
    compute_tf_cookbook.read_file("inputs/input.txt")
    assert len(compute_tf_cookbook.data) != 0
