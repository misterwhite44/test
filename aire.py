longueur = float(input("Entrez la longueur du quadrilatère : "))
largeur = float(input("Entrez la largeur du quadrilatère : "))

if longueur > 0 and largeur > 0:
    # Calcul de l'aire et du périmètre
    aire = longueur * largeur
    perimetre = 2 * (longueur + largeur)

    print("\nRésultats :")
    print("Aire du quadrilatère :", aire)
    print("Périmètre du quadrilatère :", perimetre)
    

    for i in range(int(largeur)):
        print("- " * int(longueur))
else:
    print("Les dimensions doivent être supérieures à zéro pour calculer l'aire et le périmètre.")
