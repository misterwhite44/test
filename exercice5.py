import unicodedata
import re


def compter_caracteres(phrase):
    if phrase == "":
        return 0
    return 1 + compter_caracteres(phrase[1:])

def nettoyer_chaine(chaine):
    chaine = ''.join(c for c in unicodedata.normalize('NFD', chaine) if unicodedata.category(c) != 'Mn')
    chaine = re.sub(r'[^a-zA-Z0-9]', '', chaine).lower()
    return chaine

def est_palindrome(chaine):
    chaine = nettoyer_chaine(chaine)
    if len(chaine) <= 1:
        return True
    return chaine[0] == chaine[-1] and est_palindrome(chaine[1:-1])


# Exemple d'utilisation
phrase = "Salut salut !"
print("Nombre de caractères :", compter_caracteres(phrase))
phrase = "Élu par cette crapule"
print(f"La phrase '{phrase}' est un palindrome :" , est_palindrome(phrase))
