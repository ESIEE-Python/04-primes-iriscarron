"""
  fichier
    """

from math import sqrt

#### Fonction secondaire

def isprime(p):
    """
    Retourne si p est un nombre premier.

    Args:
        p: valeur entiere positive

    Returns:
        isprime(p) : False, False, True,.....
    """
    if p in (0,1):
        return False
    if p==2:
        return True
    premier = True
    for d in range (2, int(sqrt(p)+1)):
        if p%d == 0:
            premier = False
            break
    return premier

#### Fonction principale


def main():
    """
    blabla
    """
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
    help(isprime)
    help(main)
    print(print.__doc__)
