# Abstract Factory
class GameFactory:
    def character(self):
        ...
    
    def weapon(self):
        ...


# Concrete Factory
class ElfFactory(GameFactory):
    def character(self):
        # Product
        return Elf()

    def weapon(self):
        # Product
        return Bow()


# Concrete Factory
class OrcFactory(GameFactory):
    def character(self):
        # Product
        return Orc()

    def weapon(self):
        # Product
        return Axe()


elf_factory = ElfFactory()
elf_character = elf_factory.create_character()
elf_weapon = elf_factory.create_weapon()

orc_factory = OrcFactory()
orc_character = orc_factory.create_character()
orc_weapon = orc_factory.create_weapon()