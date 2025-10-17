# problem4_tests.py
# Team Paldea – Problem 4.2
# Black Box Testing for find_gcd(a:int, b:int)

from problem4_code import find_gcd


# ------------------------------------------------------------
# Test valid cases (just checking outputs, not how it's coded)
# ------------------------------------------------------------
def test_valid_inputs():
    # Examples given in the instructions
    assert find_gcd(124, 12) == (4, 2), "Expected (4, 2) for (124, 12)"
    assert find_gcd(476, 630) == (14, 3), "Expected (14, 3) for (476, 630)"

    # Extra checks to confirm normal behavior
    assert find_gcd(10, 5) == (5, 1), "Expected (5, 1) for (10, 5)"
    assert find_gcd(9, 6) == (3, 2), "Expected (3, 2) for (9, 6)"
    assert find_gcd(8, 15) == (1, 3), "Expected (1, 3) for (8, 15)"
    assert find_gcd(13, 13) == (13, 1), "Expected (13, 1) for (13, 13)"
# ------------------------------------------------------------
# Test invalid inputs, should raise Exception
# ------------------------------------------------------------
def test_invalid_inputs():
    bad_numbers = [(0, 5), (5, 0), (-3, 7), (9, -2)]
    for a, b in bad_numbers:
        try:
            find_gcd(a, b)
            assert False, f"Expected Exception for inputs ({a}, {b})"
        except Exception:
            pass  # Correct behavior

    # Non-integer inputs
    bad_types = [("12", 4), (3.5, 7), (None, 1), ([10], 5)]
    for a, b in bad_types:
        try:
            find_gcd(a, b)
            assert False, f"Expected Exception for non-integer inputs ({a}, {b})"
        except Exception:
            pass  # Correct behavior
# ------------------------------------------------------------
# Simple runner to test by running the file directly
# ------------------------------------------------------------
if __name__ == "__main__":
    try:
        test_valid_inputs()
        test_invalid_inputs()
        print(" All tests passed successfully!")
    except AssertionError as e:
        print(" Test failed:", e)