from demo_code import RandomNumberGenerator


def test_random_number_generator():
    """Test  number generator."""
    assert RandomNumberGenerator().get_number()
