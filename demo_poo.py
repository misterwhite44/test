class Wolf:
    kind = 'loup gris'

    def __init__(self, name):
        self.name = name

    def jouer(self):
        print(f"{self.name} joue!")

ghost = Wolf("Fantôme")
nymeria = Wolf("Nymeria")

print(f"{ghost.name} est de type
      
      é {ghost.kind}")
print(f"{nymeria.name} est de type {nymeria.kind}")

        