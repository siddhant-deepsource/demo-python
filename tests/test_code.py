from demo_code import RandomNumberGenerator


def test_random_number_generator():
    """Tests random number generator."""
    assert RandomNumberGenerator().get_number()
