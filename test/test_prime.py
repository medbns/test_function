from prime import is_prime

def test_prime_number():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(1) is False
    assert is_prime(17) is True
    assert is_prime(18) is False
    assert is_prime(19) is True
    assert is_prime(0) is False
    assert is_prime(-5) is False
