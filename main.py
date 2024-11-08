from math import sqrt

def is_prime(number):
    """Retourne True si le nombre est premier, sinon False."""
    if number < 2:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def main():
    """Affiche tous les nombres premiers inférieurs à 100."""
    for n in range(100):
        if is_prime(n):
            print(n, end=", ")
    print()

if __name__ == "__main__":
    main()