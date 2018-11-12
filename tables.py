#! Python3

playerStartResources = {'food':100,
                         'wood':200,
                         'gold':100,
                         'stones':50,
                         'iron':100,
                         'coal':0,
                         'oil':0}

breeding_cost = {'worker': {'food': 40},
                 'swordsman': {'food': 40},
                 'archer': {'food': 50, 'wood': 30},
                 'priest': {'gold': 90},
                 'knight': {'food': 50, 'gold': 100, 'iron': 50}
                 }

building_cost = {'Barracks': {'wood': 100, 'stones': 50},
                 'HorseStable': {'wood': 100, 'iron': 100, 'stones': 50}
                 }

'''
'max_health' - maximum amount of the unit's health points
'speed' - the number of pixels that the unit passes by one iteration of the main loop
'attack' - the points of health that the enemy will lose after each attack
'creating_time' - seconds per creating
'level' - unit's current level/max = 5
'''

units_properties = {'worker': {'max_health': 30, 'speed': 10, 'attack': 5, 'creating_time': 10},
                    'swordsman': {'max_health': 50, 'speed': 12, 'attack': 15, 'creating_time': 20},
                    'archer': {'max_health': 40, 'speed': 12, 'attack': 10, 'creating_time': 20},
                    'priest': {'max_health': 30, 'speed': 10, 'attack': 5, 'creating_time': 40},
                    'knight': {'max_health': 80, 'speed': 20, 'attack': 20, 'creating_time': 30,}
                   }

'''
'defense' - basic amount of the buildings's defense points
'size' - the tuple which contains the length and the width of the building
'time_to_build' - seconds per creating
'''

building_properties = {'Castle': {'size': (200, 200), 'time_to_build': 150, 'defense': 1000},
                       'Barracks': {'size': (60, 100), 'time_to_build': 90, 'defense': 400},
                       'Church': {'size': (80, 80), 'time_to_build': 90, 'defense': 200}
                       }

required_buildings = {'knight': ['Horse Stable',]}