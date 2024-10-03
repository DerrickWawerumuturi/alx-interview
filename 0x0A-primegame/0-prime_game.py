#!/usr/bin/python3

#  consecutive 1 -> n(n included) = for loop
#  take turns removeing prime-numbers, and their multiples
#  x => rounds
#  

def sieve_of_eratosthenes(n):
    """ initalize a boolean that gets prime numbers from the list
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False
    return primes

def isWinner(x, nums):
    """ gets winner of the game
    """
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(primes[2: n + 1])

    if prime_count % 2 == 1:
        maria_wins += 1
    else:
        ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
