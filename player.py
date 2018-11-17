#!Python3
import buildings, units, tables


class Player:
    def __init__(self, name='player1'):
        self.text_name = name
        self.supplies = tables.playerStartResources
        self.has_buildings = {'Castle': buildings.Castle(self), }  # every new player must be created with the castle
        self.workers = [units.Worker(self) for i in range(3)]  # each player starts with 3 workers by default
        self.swordsmans = [units.Swordsman(self) for i in range(2)]  # each player starts with 2 swordsmans by default
        self.archers = [units.Archer(self) for i in range(3)]  # each player starts with 3 archers by default
        self.knights = []
        self.priests = []

    def update_supplies(self, purchase_cost):
        for source in purchase_cost.keys():
            self.supplies[source] -= purchase_cost[source]

    def check_supplies_to_create(self, purchase_cost):
        for source in purchase_cost.keys():
            if purchase_cost[source] > self.supplies[source]:
                return False
        return True

    def check_required_buildings(self, purchase):
        if purchase in tables.required_buildings.keys():
            for building in tables.required_buildings[purchase]:
                if building not in self.has_buildings.keys():
                    print('You have to build a '+building+' first.')
                    return False
            else:
                return True
        else:
            return True

    def output_status(self):
        print('You have got next buildings:')
        for building in self.has_buildings.keys():
            print(building)
        print('\n')

        print('You have got next units:')
        if self.workers:
            print('Workers - '+str(len(self.workers)))
        if self.swordsmans:
            print('Swordsman - '+str(len(self.swordsmans)))
        if self.archers:
            print('Archers - '+str(len(self.archers)))
        if self.knights:
            print('Knights - '+str(len(self.knights)))
        if self.priests:
            print('Priests - '+str(len(self.priests)))
        print('\n')

    def get_action(self):
        action = input('Please select a unit or a building to commit an action.\n'
                       'To select someone just type its name(ex. archer)')
        return action



