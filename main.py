"""
Programme qui permet de vérifier si une chaine est un palindrome ou non.
"""
import string
#### Fonction secondaire

def nettoyer_chaine(p):
    """
    Permet de nettoyer la chaine de caractères et de supprimer les accents et les espaces.
    """
    mappingaccents = str.maketrans("àáâäãåçèéêëìíîïñòóôöõùúûüýÿ", "aaaaaaceeeeiiiinooooouuuuyy")
    mappingespaces = str.maketrans("", "", string.whitespace + string.punctuation)
    p = p.lower()
    p = p.translate(mappingaccents)
    return p.translate(mappingespaces)

def ispalindrome(p):
    """ Vérifie si la chaine est un palindrome """
    # votre code ici
    p = nettoyer_chaine(p)
    return p == p[::-1]

#### Fonction principale


def main():
    """Teste la fonction palindrome"""
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie","La mariée ira mal"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
