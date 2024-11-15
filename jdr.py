class Personnage:

    def __init__(self, name, pv, attack, defense, catchphrase):
        self.name = name
        self.pv = pv
        self.attack = attack
        self.defense = defense
        self.catchphrase = catchphrase

    def sePresenter(self):
        print("Bonjour je suis " + self.name + " : " + self.catchphrase)

    def attaquer(self, personnage):
        coef_attack = self.attack - personnage.defense
        if coef_attack <= 0:
            coef_attack = 1
        personnage.pv = personnage.pv - coef_attack
        if personnage.pv < 0:
            personnage.pv = 0

class Guerrier(Personnage):
    
    def __init__(self, name, pv, attack, defense, catchphrase):
        super().__init__(name, pv, attack, defense, catchphrase)

    def criDeGuerre(self):
        print(self.catchphrase.upper())

class Clerc(Personnage):

    def __init__(self, name, pv, attack, defense, catchphrase):
        super().__init__(name, pv, attack, defense, catchphrase)

    def soigner(self, personnage):
        personnage.pv += 10

class Paladin(Guerrier, Clerc):

    def __init__(self, name, pv, attack, defense, catchphrase):
        super().__init__(name, pv, attack, defense, catchphrase)

class Archer(Personnage):

    def __init__(self, name, pv, attack, defense, catchphrase):
        super().__init__(name, pv, attack, defense, catchphrase)

    def tirer(self, personnage):
        personnage.pv = personnage.pv - self.attack
        if personnage.pv < 0:
            personnage.pv = 0

class Mage(Personnage):

    def __init__(self, name, pv, attack, defense, catchphrase, mana):
        super().__init__(name, pv, attack, defense, catchphrase)
        self.mana = mana

    def jeterUnSort(self, personnage):
        personnage.pv = personnage.pv - 20
        if personnage.pv < 0:
            personnage.pv = 0
        self.pv += 10
        self.mana -= 5


titi = Personnage("Titi", 50, 30, 60, "Z'ai cru voir un rominet !")
grosminet = Personnage("Sylvestre", 100, 40, 20, "Sapristi saucisse !")
titi.sePresenter()
grosminet.sePresenter()
print(f"Titi attaque grosminet qui a {grosminet.pv} pv : ")
titi.attaquer(grosminet)
print(f"Grosminet n'a plus que {grosminet.pv} pv !")
boromir = Guerrier("Boromir", 120, 60, 60, "Pour le Gondor !")
boromir.criDeGuerre()
arwen = Clerc("Arwen", 100, 50, 50, "...")
aragorn = Paladin("Aragorn", 150, 75, 75, "Pour Frodon !")
arwen.soigner(aragorn)
print(f"Arwen a soignÃ© Aragorn qui a maintenant {aragorn.pv} pv.")
aragorn.criDeGuerre()
aragorn.soigner(grosminet)
legolas = Archer("Legolas", 100, 60, 60, "Une aube rouge se lÃ¨ve ...")
legolas.criDeGuerre()
print(f"Legolas tire sur Boromis qui a {boromir.pv} pv : ")
legolas.tirer(boromir)
print(f"Boromir n'a plus que {boromir.pv} pv !")
gandalf = Mage("Gandalf", 100, 65, 65, "Vous ne passerez pas !", 100)
gandalf.jeterUnSort(legolas)
print(f"Gandalf a lancÃ© un sort sur Legolas qui n'a plus que {legolas.pv} pv et a maintenant {gandalf.pv} pv.")