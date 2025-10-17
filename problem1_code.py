def determine_primes(n: int):
    if not isinstance(n, int):
        raise Exception("Input must be an integer")

    if n < 2:
        #print("Provide an integer greater than 2")
        return ([], 0)

    # Initialize a boolean list for primality
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    traversal_count = 0

    # Sieve of Eratosthenes
    for p in range(2, int(n**0.5),1):
        if is_prime[p]:
            traversal_count += 1  # Each time we mark multiples of a prime
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False

    # Final traversal to collect primes
    primes = [i for i, prime in enumerate(is_prime) if prime]
    traversal_count += 1

    return(primes, traversal_count)


if __name__ == "__main__":
    print("Welcome to the Prime Number Finder!")
    print("This program will find all prime numbers from 2 up to the number you enter.\n")

    while True:
        try:
            n = int(input("Please enter a positive integer: "))

            # warn if less than 2 and ask again
            if n < 2:
                print(" The number must be 2 or greater. Please try again.\n")
                continue  # go back to the start of the loop

            primes, count = determine_primes(n)
            print(f"\nPrime numbers between 2 and {n}: {primes}")
            print(f"Number of traversals through the list: {count}")
            print("\nThank you for using the Prime Number Finder!")
            break  # exit the loop after successful run

        except ValueError:
            print("⚠️  That is not a valid number. Please enter an integer.\n")
        except Exception as e:
            print("Error:", e)