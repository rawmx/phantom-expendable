from app.greet import greet


def test_normal_name():
    assert greet("Ada") == "Hello, Ada!"


def test_name_with_surrounding_spaces():
    assert greet("  Ada \t") == "Hello, Ada!"


def test_empty_name():
    assert greet("") == "Hello, world!"


def test_blank_name():
    assert greet("   ") == "Hello, world!"
