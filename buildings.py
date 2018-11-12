#!Python3
import units, tables

class Building:
    def __init__(self, owner, text_name):
        self.owner = owner
        self.properties = tables.building_properties[text_name]

    def breed(self, type_of_unit):
        type_of_unit = type_of_unit.lower()
        if type_of_unit in self.allow_to_build:
            if self.owner.check_supplies_to_create(tables.breeding_cost[type_of_unit]):
                if self.owner.check_required_buildings(type_of_unit):
                    self.owner.update_supplies(tables.breeding_cost[type_of_unit])
                    if type_of_unit == 'worker':
                        self.owner.workers.append(units.Worker(self.owner))
                    elif type_of_unit == 'swordsman':
                        self.owner.swordsmans.append(units.Swordsman(self.owner))
                    elif type_of_unit == 'archer':
                        self.owner.archers.append(units.Archer(self.owner))
                    elif type_of_unit == 'priest':
                        self.owner.priests.append(units.Priest(self.owner))
                    elif type_of_unit == 'knight':
                        self.owner.knights.append(units.Knight(self.owner))
            else:
                print('You haven\'t got enough supplies to breed.')





class Castle(Building):
    allow_to_build = {'worker', }

    def __init__(self, owner):
        self.text_name = 'Castle'
        super().__init__(owner, self.text_name)

class Barracks(Building):
    allow_to_build = {'swordsman', 'archer', 'knight'}

    def __init__(self, owner):
        self.text_name = 'Barracks'
        super().__init__(owner, self.text_name)


class Church(Building):
    allow_to_build = {'priest', }

    def __init__(self, owner):
        self.text_name = 'Church'
        super().__init__(owner, self.text_name)


class HorseStable(Building):
    def __init__(self, owner):
        self.text_name = 'Horse stable'
        super().__init__(owner, self.text_name)