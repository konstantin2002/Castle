#!Python3

import tables, buildings


class Unit:
    # all the units will have following attributes, but it is thought that the workers will be the most numerous, so
    # -> the default values are set for workers.
    def __init__(self, owner, text_name):
        self.owner = owner
        self.alive = True
        self.properties = tables.units_properties[text_name.lower()]
        self.properties['health'] = self.properties['max_health']
        self.level = 1  # unit's current level/max = 5

    def move(self, direction):
        if not self.alive:
            print("Dead can't dance")
            return self
        print('The unit moved '+str(self.properties['speed'])+' '+direction+'.')

    def describe_unit(self):
        if not self.alive:
            print("He's already dead...")
            return self
        print('-----'+self.text_name+'-----')
        print('maximum health - '+str(self.properties['max_health']),
              'speed - '+str(self.properties['speed']),
              'attack - '+str(self.properties['attack']),
              'time for creating - '+str(self.properties['creating_time']),
              sep='\n')
        print('Cost for breeding:')
        for source, amount in self.breeding_cost.items():
            print('   '+source+' - '+str(amount))

    def attack(self, enemy_unit=''):
        if not self.alive:
            print("The dead doesn't bite...")
            return self
        if isinstance(enemy_unit, Unit):
            print(self.text_name+' is attacking the '+enemy_unit.text_name)
            enemy_unit.properties['health']-=self.properties['attack']
            if enemy_unit.properties['health']<=0:
                print('The '+enemy_unit.text_name+' was cut down in battle...')
                enemy_unit.alive = False
        else:
            print('Choose the unit to be attacked...')

    def upgrade(self):
        if not self.alive:
            print("The dead can't be upgrayyed...")
            return self
        if self.level < 5:
            print('The unit is upgrading...')
            self.level += 1
            self.properties['speed'] += 2
            self.properties['attack'] += 5
            self.properties['creating_time'] -= 1
            self.properties['health'] += 10
            self.properties['max_health'] += 10

            print('The unit has been upgraded to level '+str(self.level))
        else:
            print('The unit can not be uprgayyed more...')


class Worker(Unit):
    # workers are created mainly for collecting resources but can be used for battle at an emergency
    def __init__(self, owner):
        self.text_name = 'Worker'
        super().__init__(owner, self.text_name)

    def work(self, work_obj=None):
        if not self.alive:
            print("His work is finished...")
            return self
        if work_obj == 'forest':
            print('The worker is starting to chop the trees...')
        else:
            print('The worker is starting to work...')

    def build(self, type_of_building):
        if type_of_building not in self.owner.has_buildings:
            if self.owner.check_supplies_to_create(tables.building_cost[type_of_building]):
                self.owner.update_supplies(tables.building_cost[type_of_building])
                if type_of_building == 'Barracks':
                    self.owner.has_buildings[type_of_building] = buildings.Barracks(self.owner)
                elif type_of_building == 'Castle':
                    self.owner.has_buildings[type_of_building] = buildings.Castle(self.owner)
                elif type_of_building == 'Church':
                    self.owner.has_buildings[type_of_building] = buildings.Church(self.owner)
            else:
                print('You haven\'t got enough supplies to build.')


class Swordsman(Unit):
    def __init__(self, owner):
        self.text_name = 'Swordsman'
        super().__init__(owner, self.text_name)


class Archer(Unit):
    def __init__(self, owner):
        self.text_name = 'Archer'
        super().__init__(owner, self.text_name)

    def shoot_an_arrow(self, enemy_unit=''):
        if not self.alive:
            print("The dead doesn't bite...")
            return self
        if isinstance(enemy_unit, Unit):
            print('The '+self.text_name+' is shooting an arrow at the '+enemy_unit.text_name+'...')
            enemy_unit.properties['health']-=5
            if enemy_unit.properties['health']<=0:
                print('The '+enemy_unit.text_name+' was cut down in battle...')
                enemy_unit.alive = False
        else:
            print('Choose the enemy unit to be shot...')


class Priest(Unit):
    def __init__(self, owner):
        self.text_name = 'Priest'
        super().__init__(owner, self.text_name)

    def heal(self, wounded_unit=''):
        if not self.alive:
            print("This priest now can heal only the souls...")
            return self
        if not wounded_unit.alive:
            print("It's no use healing the dead guy...")
            return self
        if isinstance(wounded_unit, Unit):
            print('The unit is being healed...')
            if wounded_unit.properties['health'] < wounded_unit.properties['max_health']:
                wounded_unit.properties['health']+=2
                if wounded_unit.properties['health'] > wounded_unit.properties['max_health']:
                    wounded_unit.properties['health'] = wounded_unit.properties['max_health']
        else:
            print('Choose the unit to be healed...')


class Knight(Unit):
    def __init__(self, owner):
        self.text_name = 'Knight'
        super().__init__(owner, self.text_name)