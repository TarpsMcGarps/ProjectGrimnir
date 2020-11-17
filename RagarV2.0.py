#!/usr/bin/python3

###############################################################################################################################
### THIS GAME WAS CREATED BY JEFF "TARPS McGARPS" TARPLEY OF PSEUDOSOFT SOFTWORKS (tm) A SUBSIDIARY OF TRIFIRE STUDIOS (tm) ###
###############################################################################################################################

### TODO'S ###
"""## FIX EQUIPPING A OFFHAND WEAPON WHEN USING A BOTH HAND WEAPON"""
# IMPLEMENT ACCESSORIES
# IMPLEMENT CONSUMABLES
"""## IMPLEMENT CRITICAL HIT CHANCE"""
"""## IMPLEMENT DODGE CHANCE"""
"""## IMPLEMENT PERFECT DEFEND CHANCE"""
"""## IMPLEMENT COUNTER CHANCE"""
"""!!!MOVING FROM RIGHT SIDE TO LEFT AND RESETTING MOBS HAS BEEN IMPLEMENTED""" # IMPLEMENT MULTIPLE MAPS
"""!!!MATERIALS LEVEL BUT THAT SHOULD ONLY CAP IT AND HAVE A CHANCE OF DROPPING LOWER LEVEL GEAR""" ## IMPLEMENT MATERIAL LEVELING
"""## ALLOW NONCOMBATANTS TO MOVE DURING COMBAT"""
"""## CHECK ON PASSIVE RECOVERIES"""
# CREATE SPLASH SCREENS
# USE STORY TO CREATE CHARACTER
# [[[VERY LOW PRIORITY]]] ALLOW PLAYER TO UNEQUIP ITEMS
# CALCULATE RATINGS BASED ON PLAYER CLASS VERSUS ITEM CLASS
# [[LOW PRIORITY]] ALLOW PLAYER TO ATTACK FROM A DISTANCE
"""### CREATE ARRAYS TO DISPLAY HUD AROUND MAP AND IMPLEMNT INTO DISPLAY FUNCTION"""
### [[TIME ALLOWING, HIGH PRIORITY]] COMMENT EVERYTHING
# ADD ATTACK AND DEFENSE RATING TO VIEW EQUIPMENT
# DEVELOP ABILITY TO SNEAK

import os
import random

print("hello world")
metal   = ['iron', 'carved iron', 'steel', 'tempered steel', 'agran', 'alloyed agran']
leather = ['soft leather', 'rough leather', 'hardened leather', 'tanned leather', 'treated leather', 'reenforced leather']
cloth   = ['linen', 'canvas', 'embroidered', 'silken', 'double stitched', 'gilded']
wood    = ['oak', 'pressed oak', 'maple', 'reenforced maple', 'rosewood', 'carved rosewood']
shield  = ['pressed oak', 'reenforced maple', 'carved iron', 'carved rosewood', 'tempered steel', 'alloyed agran']
coin    = ['tin', 'bronze', 'copper', 'silver', 'gold', 'platinum']
#potion  = ['healing', 'invigorating', 'focusing']
#poison  = ['slowing']
#cheese  = ['wheel']
#scroll  = ['fire', 'freeze']
not_dead_mobs  = []
combatant_mobs = []
dead_mobs      = []

def splashPseudosoft():
    os.system('clear')
    print("\n\n\n")
    print("                 ________ _____   _______ ___   ___ _____    _______   _____   _______   _______ __________")
    print("                /  ___  // ___ \ /  ____//  /  /  // ___ \  /  __   \ / ___ \ /  __   \ /  ____//___   ___/")
    print("               /  /__/ // /__ \//  /_   /  /  /  // /  /  //  /  /  // /__ \//  /  /  //  /_       /  /")
    print("              /  _____/ \__  \ /   _/  /  /  /  // / /  / /  /  /  / \__  \ /  /  /  //   _/      /  /")
    print("             /  /     /\__/  //  /____ \  \_/  // //  /  /  /_ /  //\__/  //  /_ /  //  /        /  /")
    print("            /__/      \_____//_______/  \_____//____/    \_______/ \_____/ \_______//__/        /__/     tm")
    null = input()

def disclaimer():
    os.system('clear')
    print("\n\n\n\tDISCLAIMER:\n\t\tThis game will not hold your hand. The stats for your character matter, but how will not be explained unless you read how this game is programmed. The monsters will move even when you can not see them, it would be safe to assume that they move every time you perform any action. Some things may not be implemented yet but if that is the case I have done my best to leave messages that will let you know.")

splashPseudosoft()

def spawnMobs():
    mobKindChance = random.randint(1,20)
    if mobKindChance <= 6:
        mob = Mob(G(), 'goblin', '& ', 60, 20, [armor_drops, weapon_drops, misc_drops])
    elif mobKindChance <= 12:
        mob = Mob(G(), 'spider', '* ', 80, 20, [armor_drops, weapon_drops, misc_drops])
    elif mobKindChance <= 17:
        mob = Mob(G(), 'skeleton', '$ ', 100, 20, [armor_drops, weapon_drops, misc_drops])
    else:
        mob = Mob(G(), 'troll', '<>', 150, 20, [armor_drops, weapon_drops, misc_drops])
    unwalkable = True
    while unwalkable:
        col = random.randint(6,24)
        row = random.randint(6,16)
        if game_map[row][col].walkable:
            mob.row,mob.col = row,col
            unwalkable = False
    not_dead_mobs.append(mob)

class Item():
    def __init__(self, kind, material, playerClass, rating, slot, armor, weapon, consumable):
        self.kind = kind
        self.material = material
        self.playerClass = playerClass
        self.rating = rating
        self.slot = slot
        self.armor = armor
        self.weapon = weapon
        self.consumable = consumable

armor_drops = [
        #Item         #   Chance Material Slot           Class                                Rating Armor  Weapon Consumable
        ['Null',      0,  100,   0,       0,             0,                                   0,     0,     0,     0    ],
        ['helmet',    1,  40,    metal,   'head',        ['warrior'],                         10,    True,  False, False],
        ['hood',      1,  40,    cloth,   'head',        ['ranger', 'rogue', 'mage'],         2,     True,  False, False],
        ['hat',       1,  20,    cloth,   'head',        ['bard'],                            2,     True,  False, False],
        ['pauldrons', 1,  30,    metal,   'shoulders',   ['warrior'],                         12,    True,  False, False],
        ['bracers',   1,  30,    leather, 'arms',        ['warrior', 'ranger', 'rogue'],      8,     True,  False, False],
        ['gauntlets', 1,  40,    metal,   'arms',        ['warrior'],                         10,    True,  False, False],
        ['gloves',    1,  40,    leather, 'arms',        ['ranger', 'rogue'],                 6,     True,  False, False],
        ['gloves',    1,  10,    cloth,   'arms',        ['mage', 'bard'],                    2,     True,  False, False],
        ['cuirass',   1,  50,    metal,   'chest',       ['warrior'],                         20,    True,  False, False],
        ['cuirass',   1,  40,    leather, 'chest',       ['ranger'],                          10,    True,  False, False],
        ['robes',     1,  20,    cloth,   'chest',       ['mage'],                            2,     True,  False, False],
        ['cloak',     1,  20,    cloth,   'chest',       ['ranger', 'rogue'],                 4,     True,  False, False],
        ['tunic',     1,  10,    cloth,   'chest',       ['rogue', 'mage', 'bard'],           2,     True,  False, False],
        ['greaves',   1,  20,    metal,   'legs',        ['warrior'],                         10,    True,  False, False],
        ['chaps',     1,  10,    leather, 'legs',        ['ranger'],                          8,     True,  False, False],
        ['pants',     1,  10,    cloth,   'legs',        ['rogue', 'mage', 'bard'],           2,     True,  False, False],
        ['boots',     1,  80,    metal,   'feet',        ['warrior'],                         10,    True,  False, False],
        ['boots',     1,  60,    leather, 'feet',        ['ranger', 'rogue', 'mage', 'bard'], 6,     True,  False, False],
        ['shield',    1,  10,    shield,  'offhand',     ['warrior'],                         50,    True,  False, False]
                ]

weapon_drops = [
        #Item         #   Chance Material  Slot          Class                                Rating Armor  Weapon Consumable
        ['Null',      0,  100,   0,        0,            0,                                   0,     0,     0,     0    ],
        ['sword',     2,  40,    metal,    'either',     'warrior',                           30,    False, True,  False],
        ['axe',       2,  40,    metal,    'either',     'warrior',                           25,    False, True,  False],
        ['dagger',    2,  50,    metal,    'either',     'rogue',                             20,    False, True,  False],
        ['bow',       1,  30,    wood,     'both',       'ranger',                            25,    False, True,  False],
        ['staff',     1,  20,    wood,     'mainhand',   'mage',                              30,    False, True,  False],
        ['lute',      1,  10,    wood,     'both',       'bard',                              25,    False, True,  False]
                ]

misc_drops = [
        #Item         #   Chance Material  Slot          Class                                Rating Armor  Weapon Consumable
        ['Null',      1,  100,   0,        0,            0,                                   0,     0,     0,     0,   ],
        ['piece(s)',  10, 30,    coin,     'gold',       0,                                   1,     False, False, False]
#        ['potion(s)', 2,  10,    potion,   'consumable', 0,                                   1,     False, False, True ],
#        ['poison(s)', 1,  10,    poison,   'consumable', 0,                                   1,     False, False, True ],
#        ['cheese',    1,  10,    cheese,   'consumable', 0,                                   1,     False, False, True ],
#        ['scroll',    1,  10,    scroll,   'consumable', 0,                                   1,     False, False, True ],
#        ['rune',      1,  1,     scroll,   'consumable', 0,                                   1,     False, False, True ]
              ]

races = [
        #Race      S      A      D      P      I      E
        ["human",  2, 10, 2, 10, 2, 10, 2, 10, 2, 10, 2, 10],
        ["dwarf",  3, 11, 1, 9,  2, 10, 1, 11, 2, 10, 3, 11],
        ["elf",    1, 9,  2, 10, 1, 9,  3, 11, 3, 11, 2, 10],
        ["orc",    3, 11, 2, 10, 2, 10, 1, 9,  1, 9,  3, 11],
        ["ent",    3, 11, 1, 9,  1, 9,  1, 9,  3, 11, 3, 11],
        ["vaeron", 3, 11, 1, 9,  3, 11, 1, 9,  1, 9,  3, 11]
         ]

class Mob():
    """This is a monster"""
    walkable = False
    def __init__(self, standing_on, kind, sym, health, attack, drops):
        self.standing_on = standing_on
        self.kind = kind
        self.sym = sym
        self.row = 0
        self.col = 0
        self.maxHealth = health
        self.health = health
        self.attack = attack
        self.drops = drops

    def dropItem(self):
        if pC.level < 5:
            material = 0
        elif pC.level < 10:
            material = 1
        elif pC.level < 15:
            material = 2
        elif pC.level < 20:
            material = 3
        elif pC.level < 25:
            material = 4
        elif pC.level >= 25:
            material = 5
        kindOfItem = random.choice(self.drops)
        KOI = kindOfItem
        chanceSum = 0
        for drop in range(len(kindOfItem)):
            chanceSum += kindOfItem[drop][2]
        dropRoll = random.randint(1,chanceSum)
        chanceSum = 0
        for drop in range(len(kindOfItem)):
            chanceSum += kindOfItem[drop][2]
            if dropRoll <= chanceSum:
                break
        if KOI[drop][0] != 'Null':
            droppedItem = Item(KOI[drop][0], KOI[drop][3][material], KOI[drop][5], KOI[drop][6], KOI[drop][4], KOI[drop][7], KOI[drop][8], KOI[drop][9])
            droppedItem.rating *= material + 1
            pC.inventory.append(droppedItem)

    def __str__(self):
        return self.sym


class Player():
    walkable = False
    """This is the player character"""
    def __init__(self):
        self.standing_on = G()
        self.row = 1
        self.col = 1
        self.name = "ragnar"
        self.race = "human"
        self.playerClass = "warrior"
        self.level = 1
        self.xp = 0
        self.xp2LevelUp = 1000
        self.levelUpPoints = 0
        self.maxHealth = 100
        self.health = 100
        self.maxStamina = 100
        self.stamina = 100
        self.maxMana = 100
        self.mana = 100
        self.attack = 10
        self.defense = 10
        self.maxStrength = 10
        self.strength = 2
        self.maxAgility = 10
        self.agility = 2
        self.maxDexterity = 10
        self.dexterity = 2
        self.maxPerception = 10
        self.perception = 2
        self.maxIntelligence = 10
        self.intelligence = 2
        self.maxEndurance = 10
        self.endurance = 2
        self.inventory = []
        self.equipment = {'head':'empty', 'shoulders':'empty', 'chest':'empty', 'arms':'empty', 'legs':'empty', 'feet':'empty', 'mainhand':'empty', 'offhand':'empty', 'accessory':'empty', 'heldItem':'empty'}

    def setRace(self, selectedRace):
        self.race            = races[selectedRace][0]
        self.strength        = races[selectedRace][1]
        self.maxStrength     = races[selectedRace][2]
        self.agility         = races[selectedRace][3]
        self.maxAgility      = races[selectedRace][4]
        self.dexterity       = races[selectedRace][5]
        self.maxDexterity    = races[selectedRace][6]
        self.perception      = races[selectedRace][7]
        self.maxPerception   = races[selectedRace][8]
        self.intelligence    = races[selectedRace][9]
        self.maxIntelligence = races[selectedRace][10]
        self.endurance       = races[selectedRace][11]
        self.maxEndurance    = races[selectedRace][12]

    def equipSomething(self):
        os.system('clear')
        if self.inventory:
            print("\n\tWhat kind of item would you like to equip?")
            print("\t\t1. Weapon")
            print("\t\t2. Armor")
            print("\t\t3. Accessory")
            print("\t\t4. Consumable")
            choice = input()
            if choice == '1':
                theseOnes = []
                while True:
                    number = 1
                    print("\n\tWeapons:")
                    for item in self.inventory:
                        if item.weapon:
                            theseOnes.append(item)
                            print("\t\t" + str(number) + ". " + item.material.title() + " " + item.kind.title())
                            number += 1
                    if theseOnes == []:
                        null = input()
                        break
                    for item in theseOnes:
                        self.inventory.remove(item)
                    choice = input()
                    if choice:
                        try:
                            choice = int(choice) - 1
                            choice = theseOnes[choice]
                        except:
                            os.system('clear')
                            print("\n\tYou have to enter a valid number. Or press only enter to go back to previous menu.")
                            null = input()
                            for item in theseOnes:
                                self.inventory.append(item)
                            continue
                        if choice.slot == 'either':
                            os.system('clear')
                            print("\n\tWhich hand do you want to equip this " + choice.material + " " + choice.kind + " in?")
                            print("\t\t1. Mainhand")
                            print("\t\t2. Offhand")
                            hand = input()
                            if hand:
                                if hand == '1':
                                    if self.equipment['mainhand'] != 'empty':                                                                                                                                       self.inventory.append(self.equipment['mainhand'])
                                    self.equipment['mainhand'] = choice
                                    theseOnes.remove(choice)
                                elif hand == '2':
                                    if self.equipment['offhand'] != 'empty':
                                        self.inventory.append(self.equipment['offhand'])
                                    if self.equipment['mainhand'] == 'both':
                                        self.inventory.append(self.equipment['mainhand'])
                                        self.equipment['mainhand'] = 'empty'
                                    self.equipment['offhand'] = choice
                                    theseOnes.remove(choice)
                                else:
                                    os.system('clear')
                                    print("\n\tYou have to enter a valid number. Or press only enter to go back to previous menu.")
                                    null = input()
                                    for item in theseOnes:
                                        self.inventory.append(item)
                                    continue
                            else:
                                print("\n\tYou have to enter something. Or press only enter to go back to previous menu.")
                                for item in theseOnes:
                                    self.inventory.append(item)
                                continue
                        elif choice.slot == 'both':
                            if self.equipment['offhand'] != 'empty':
                                self.inventory.append(self.equipment['offhand'])
                                self.equipment['offhand'] = 'empty'
                            if self.equipment['mainhand'] != 'empty':
                                self.inventory.append(self.equipment['mainhand'])
                            self.equipment['mainhand'] = choice
                            theseOnes.remove(choice)
                        else:
                            if self.equipment['mainhand'] != 'empty':
                                self.inventory.append(self.equipment['mainhand'])
                            self.equipment['mainhand'] = choice
                            theseOnes.remove(choice)
                    if theseOnes != []:
                        for item in theseOnes:
                            self.inventory.append(item)
                    break
            elif choice == '2':
                theseOnes = []
                while True:
                    number = 1
                    print("\n\tArmor:")
                    for item in self.inventory:
                        if item.armor:
                            theseOnes.append(item)
                            print("\t\t" + str(number) + ". " + item.material.title() + " " + item.kind.title())
                            number += 1
                    if theseOnes == []:
                        null = input()
                        break
                    for item in theseOnes:
                        self.inventory.remove(item)
                    choice = input()
                    if choice:
                        try:
                            choice = int(choice) - 1
                            choice = theseOnes[choice]
                        except:
                            os.system('clear')
                            print("\n\tYou have to enter a valid number. Or press only enter to go back to previous menu.")
                            null = input()
                            for item in theseOnes:
                                self.inventory.append(item)
                            continue
                        if self.equipment[choice.slot] != 'empty':
                            self.inventory.append(self.equipment[choice.slot])
                        self.equipment[choice.slot] = choice
                        theseOnes.remove(choice)
                    if theseOnes != []:
                        for item in theseOnes:
                            self.inventory.append(item)
                    break
            elif choice == '3':
                print("Accessories haven't been implemented yet")
                null = input()
            elif choice == '4':
                while True:
                    number = 1
                    theseOnes = []
                    print("\n\tConsumables:")
                    for item in self.inventory:
                        if item.consumable:
                            theseOnes.append(item)
                            self.inventory.remove(item)
                            print("\t\t" + str(number) + ". " + item.material.title() + " " + item.kind.title())
                            number += 1
                    if theseOnes == []:
                        null = input()
                        break
                    choice = input()
                    if choice:
                        try:
                            choice = int(choice) - 1
                            choice = theseOnes[choice]
                        except:
                            os.system('clear')
                            print("\n\tYou have to enter a valid number. Or press only enter to go back to previous menu.")
                            null = input()
                            for item in theseOnes:
                                self.inventory.append(item)
                            continue
                        if self.equipment[choice.slot] != 'empty':
                            self.inventory.append(self.equipment[choice.slot])
                        self.equipment[choice.slot] = choice
                        theseOnes.remove(choice)
                    if theseOnes != []:
                        for item in theseOnes:
                            self.inventory.append(item)
                    break
        else:
            print("You don't have anything in your inventory.")
            null = input()

    def showEquipment(self):
        os.system('clear')
        for slot, item in self.equipment.items():
            print(slot.title() + ":")
            if item == 'empty':
                print("\t" + item.title())
            else:
                print("\t" + item.material.title() + " " + item.kind.title())
        null = input()

    def viewInventory(self):
        if self.inventory:
            for item in self.inventory:
                print(item.material.title() + " " + item.kind.title())
            null = input()

    def calculateRatings(self):
        self.attack = 0
        self.defense = 0
        for slot, item in self.equipment.items():
            if slot == 'mainhand':
                if item == 'empty':
                    self.attack = 10
            if item == 'empty':
                self.defense += 1
            elif item.armor:
                self.defense += item.rating
            elif item.weapon:
                self.attack += item.rating

    def levelUpCheck(self):
        while self.xp > self.xp2LevelUp:
            self.xp -= self.xp2LevelUp
            self.level += 1
            self.maxHealth += 10
            self.health = self.maxHealth
            self.maxStamina += 10
            self.stamina = self.maxStamina
            self.maxMana += 10
            self.mana = self.maxMana
            self.levelUpPoints += 1
            self.xp2LevelUp *= 2
            self.levelUp()

    def levelUp(self):
        while self.levelUpPoints > 0:
            os.system('clear')
            print("\n\tYou just leveled up! Your Level is " + str(self.level) + ". You have " + str(self.levelUpPoints) + " stat points left.")
            print("\t\tPick a stat to increase:")
            print("\t\t    Stat          Current  Max")
            print("\t\t 1. Strength      " + str(self.strength) + "\t" + str(self.maxStrength))
            print("\t\t 2. Agility       " + str(self.agility) + "\t" + str(self.maxAgility))
            print("\t\t 3. Dexterity     " + str(self.dexterity) + "\t" + str(self.maxDexterity))
            print("\t\t 4. Perception    " + str(self.perception) + "\t" + str(self.maxPerception))
            print("\t\t 5. Intelligence  " + str(self.intelligence) + "\t" + str(self.maxIntelligence))
            print("\t\t 6. Endurance     " + str(self.endurance) + "\t" + str(self.maxEndurance))
            choice = input()
            if choice == '1':
                if self.strength < self.maxStrength:
                    self.strength += 1
                    self.levelUpPoints -= 1
            elif choice == '2':
                if self.agility < self.maxAgility:
                    self.agility += 1
                    self.levelUpPoints -= 1
            elif choice == '3':
                if self.dexterity < self.maxDexterity:
                    self.dexterity += 1
                    self.levelUpPoints -= 1
            elif choice == '4':
                if self.perception < self.maxPerception:
                    self.perception += 1
                    self.levelUpPoints -= 1
            elif choice == '5':
                if self.intelligence < self.maxIntelligence:
                    self.intelligence += 1
                    self.levelUpPoints -= 1
            elif choice == '6':
                if self.endurance < self.maxEndurance:
                    self.endurance += 1
                    self.levelUpPoints -= 1

    def __str__(self):
        return "0 "

class W():
    """This is a wall"""
    walkable = False

    def __str__(self):
        return "X "

class G():
    """This is grass"""
    walkable = True

    def __str__(self):
        return "  "

pre_map = [
    ["#               "],
    ["#  Directions   "],
    ["#   W. North    "],
    ["#   A. West     "],
    ["#   S. South    "],
    ["#   D. East     "],
    ["#               "],
    ["#  Options      "],
    ["#   1. View     "],
    ["#    Inventory  "],
    ["#   2. Equip    "],
    ["#    Something  "],
    ["#   3. Show     "],
    ["#    Equipment  "],
    ["#               "],
    ["#               "],
    ["#               "],
    ["#               "]
]

game_map = [
    [W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W()],
    [W(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), W()],
    [W(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), W()],
    [W(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), W()],
    [W(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), W()],
    [W(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), W()],
    [W(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), W()],
    [W(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), W()],
    [W(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), W()],
    [W(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), W()],
    [W(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), W()],
    [W(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), W()],
    [W(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), W()],
    [W(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), W()],
    [W(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), W()],
    [W(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), W()],
    [W(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), G(), W()],
    [W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W(), W()]
]
"""This is the Game Map, it is an array. Essentially it is just lists within lists."""

post_map = [
    ["              #"],
    [" Monsters     #"],
    ["  &-Goblin    #"],
    ["  *-Spider    #"],
    ["  $-Skeleton  #"],
    [" <>-Troll     #"],
    ["              #"],
    ["              #"],
    ["              #"],
    ["              #"],
    ["              #"],
    ["              #"],
    ["              #"],
    ["              #"],
    ["              #"],
    ["              #"],
    ["              #"],
    ["              #"]
]

for i in range(random.randint(10,15)):
    spawnMobs()
"""This just calls the Mob Spawning Function."""

pC = Player()
"""This instantiates the Player Character using the Player Class."""

def nameCharacter():
    os.system('clear')
    print("\n\tPlease enter your name:")
    name = input()
    pC.name = name
    playerCharacterCreation()

def pickRace():
    os.system('clear')
    print("\n\tWhat Race are you?")
    print("\t\t1. Human")
    print("\t\t2. Dwarf")
    print("\t\t3. Elf")
    print("\t\t4. Orc")
    print("\t\t5. Ent")
    print("\t\t6. Vaeron")
    choice = input()
    if choice == '1':
        pC.setRace(0)
    elif choice == '2':
        pC.setRace(1)
    elif choice == '3':
        pC.setRace(2)
    elif choice == '4':
        pC.setRace(3)
    elif choice == '5':
        pC.setRace(4)
    elif choice == '6':
        pC.setRace(5)
    else:
        pickRace()
    playerCharacterCreation()

def pickClass():
    os.system('clear')
    print("\n\tWhat is your profession?")
    print("\t\t1. Warrior")
    print("\t\t2. Ranger")
    print("\t\t3. Rogue")
    print("\t\t4. Farmer")
    print("\t\t5. Bard")
    print("\t\t6. Mage")
    choice = input()
    if choice == '1':
        pC.playerClass = "Warrior"
    elif choice == '2':
        pC.playerClass = "Ranger"
    elif choice == '3':
        pC.playerClass = "Rogue"
    elif choice == '4':
        pC.playerClass = "Farmer"
    elif choice == '5':
        pC.playerClass = "Bard"
    elif choice == '6':
        pC.playerClass = "Mage"
    else:
        pickClass()
    playerCharacterCreation()

def viewCharacter():
    os.system('clear')
    print("\n\tThis is who you are:")
    print("\t\t" + pC.name + " the " + pC.race + " " + pC.playerClass)
    print("\t\tLevel:        " + str(pC.level))
    print("\n\t\tStrength:     " + str(pC.strength))
    print("\t\tAgility:      " + str(pC.agility))
    print("\t\tDexterity:    " + str(pC.dexterity))
    print("\t\tPerception:   " + str(pC.perception))
    print("\t\tIntelligence: " + str(pC.intelligence))
    print("\t\tEndurance:    " + str(pC.endurance))
    null = input()
    playerCharacterCreation()

def playerCharacterCreation():
    os.system('clear')
    print("\n\tCreate your character!")
    print("\t\t1. Name")
    print("\t\t2. Race")
    print("\t\t3. Class")
    print("\t\t4. View Character")
    print("\t\t5. Move on")
    choice = input()
    if choice == '1':
        nameCharacter()
    elif choice == '2':
        pickRace()
    elif choice == '3':
        pickClass()
    elif choice == '4':
        viewCharacter()
    elif choice == '5':
        print("Next...")
    else:
        playerCharacterCreation()

playerCharacterCreation()

def display():
    """This function is for displaying(printing) the Game Map. You can't just print it because it will print the brackets and everything. You also have to use for loops to print each position and in the array. But first it makes sure all of the Mobs and the Player Character are on the map."""
    os.system('clear')
    print("\t" + pC.name.title() + " the level " + str(pC.level) + " " + pC.race.title() + " " + pC.playerClass.title())
    print("###################################################################################")
    for row in range(18):
        print(pre_map[row][0], end='')
        for col in range(26):
            print(game_map[row][col], end=''),
        print(post_map[row][0])

def largeHealthBar(maxHealth, health):
    """This function takes a max and current stat then converts it to a percentage of the max value. Then it prints a start line followed by an incremented 5 at a time for the percentage. If the percentage is less than the max value it will printing empty spaces for the difference."""
    percent = 100 * health / maxHealth
    print("|", end='')
    if percent >= 5:
        print("-", end='')
    for i in range(1,20):
        if percent >= i * 5:
            print(str(i * 5) + "-", end='')
        else:
            print("   ", end='')
    print("|", end='')

def smallBar(maxStat, currentStat):
    """This function is the same as the one above but increments by 10 instead of 5."""
    percent = 100 * currentStat / maxStat
    print("|", end='')
    if percent >= 10:
        print("-", end='')
    for i in range(1, 10):
        if percent >= i * 10:
            print(str(i * 10) + "-", end='')
        else:
            print("   ", end='')
    print("|", end='')

def playerBars():
    print("#    HEALTH ", end='')
    largeHealthBar(pC.maxHealth, pC.health)
    print("           #\n#  STAMINA ", end='')
    smallBar(pC.maxStamina, pC.stamina)
    print(" ", end='')
    smallBar(pC.maxMana, pC.mana)
    print(" MANA     #")
    print("#                        XP ", end='')
    smallBar(pC.xp2LevelUp, pC.xp)
    print(" " + str(pC.xp) + "/" + str(pC.xp2LevelUp))
    print("###################################################################################")

def moveUp():
    """These are the functions to move the Player Character, it checks to make sure the Player is trying to move onto a position that is walkable, and then if it is, it puts what the player was standing on back into its position on the map. Next is moves the Player Character and puts what was on the map into the Player class as what the player is standing on."""
    if game_map[pC.row - 1][pC.col].walkable:
        game_map[pC.row][pC.col] = pC.standing_on
        pC.row -= 1
        pC.standing_on = game_map[pC.row][pC.col]

def moveLeft():
    """See above."""
    if game_map[pC.row][pC.col - 1].walkable:
        game_map[pC.row][pC.col] = pC.standing_on
        pC.col -= 1
        pC.standing_on = game_map[pC.row][pC.col]

def moveDown():
    """See above."""
    if game_map[pC.row + 1][pC.col].walkable:
        game_map[pC.row][pC.col] = pC.standing_on
        pC.row += 1
        pC.standing_on = game_map[pC.row][pC.col]

def moveRight():
    """See above."""
    if game_map[pC.row][pC.col + 1].walkable:
        game_map[pC.row][pC.col] = pC.standing_on
        pC.col += 1
        pC.standing_on = game_map[pC.row][pC.col]
    elif pC.col == 24 and pC.row in range(8, 9):
        for mob in dead_mobs:
            game_map[mob.row][mob.col] = mob.standing_on
        game_map[pC.row][pC.col] = pC.standing_on
        pC.col = 1
        pC.standing_on = game_map[pC.row][pC.col]
        game_map[pC.row][pC.col] = pC
        for i in range(random.randint(10,15)):
            spawnMobs()

def followOrRandomMove():
    for mob in not_dead_mobs:
        rowProx = mob.row - pC.row
        colProx = mob.col - pC.col
        randRow = random.randint(-1,1)
        randCol = random.randint(-1,1)
        if 4 >= rowProx >= -4 and 4 >= colProx >= -4:
                if mob.row > pC.row:
                    if game_map[mob.row - 1][mob.col].walkable:
                        game_map[mob.row][mob.col] = mob.standing_on
                        mob.row -= 1
                        mob.standing_on = game_map[mob.row][mob.col]
                if mob.row < pC.row:
                    if game_map[mob.row + 1][mob.col].walkable:
                        game_map[mob.row][mob.col] = mob.standing_on
                        mob.row += 1
                        mob.standing_on = game_map[mob.row][mob.col]
                if mob.col > pC.col:
                    if game_map[mob.row][mob.col - 1].walkable:
                        game_map[mob.row][mob.col] = mob.standing_on
                        mob.col -= 1
                        mob.standing_on = game_map[mob.row][mob.col]
                if mob.col < pC.col:
                    if game_map[mob.row][mob.col + 1].walkable:
                        game_map[mob.row][mob.col] = mob.standing_on
                        mob.col += 1
                        mob.standing_on = game_map[mob.row][mob.col]
        else:
            if game_map[mob.row + randRow][mob.col].walkable:
                game_map[mob.row][mob.col] = mob.standing_on
                mob.row = mob.row + randRow
                mob.standing_on = game_map[mob.row][mob.col]
            if game_map[mob.row][mob.col + randCol].walkable:
                game_map[mob.row][mob.col] = mob.standing_on
                mob.col = mob.col + randCol
                mob.standing_on = game_map[mob.row][mob.col]

def combatCheck():
    for mob in not_dead_mobs:
        rowProx = mob.row - pC.row
        colProx = mob.col - pC.col
        if 1 >= rowProx >= -1 and 1 >= colProx >= -1:
            not_dead_mobs.remove(mob)
            combatant_mobs.append(mob)

def activeDefend():
    defenseStrength = 1
    for i in range(pC.endurance):
        defenseStrength += 0.2
    defenseStrength *= pC.defense
    perfectDefenseChance = 100
    for i in range(pC.endurance):
        perfectDefenseChance /= 0.8
    perfectDefenseChance -= perfectDefenseChance % 1
    for mob in combatant_mobs:
        perfectDefenseChance = random.randint(1, perfectDefenseChance)
        if perfectDefenseChance == 1:
            os.system('clear')
            print("You just defended against a " + mob.kind.title() + " perfectly, you take no damage from it's attack.")
            null = input()
        else:
            pC.health -= mob.attack / defenseStrength
    passiveRecoverStamina(0.1)
    passiveRecoverMana(0.075)

def passiveDefend():
    dodgeChance = 100
    counterChance = 100
    for i in range(pC.agility):
        dodgeChance /= 0.8
    for i in range(pC.dexterity):
        counterChance /= 0.8
    dodgeChance -= dodgeChance % 1
    counterChance -= counterChance % 1
    for mob in combatant_mobs:
        dodgeChance = random.randint(1, dodgeChance)
        counterChance = random.randint(1, counterChance)
        if dodgeChance == 1 and counterChance == 1:
            mob.health -= mob.attack
            os.system('clear')
            print("You just dodged and countered a " + mob.kind.title() + " for as much damage as it would have caused you.")
            if mob.health <= 0:
                mob.dropItem()
                combatant_mobs.remove(mob)
                dead_mobs.append(mob)
                pC.xp += mob.maxHealth
                pC.levelUpCheck()
            null = input()
        elif dodgeChance == 1:
            os.system('clear')
            print("You just got dodged all damage from a " + mob.kind.title() + ".")
            null = input()
        elif counterChance == 1:
            pC.health -= mob.attack / pC.defense
            mob.health -= mob.attack
            os.system('clear')
            print("You just countered a " + mob.kind.title() + " hurting it as much as it hurt you.")
            if mob.health <= 0:
                mob.dropItem()
                combatant_mobs.remove(mob)
                pC.xp += mob.maxHealth
                pC.levelUpCheck()
            null = input()
        else:                                                                                                                                                                             pC.health -= mob.attack / pC.defense

def attack():
    attacks = pC.agility * 0.5
    if pC.equipment['mainhand'] != 'empty':
        if pC.equipment['mainhand'].kind == 'dagger':
            attacks = pC.agility * 0.75
    if pC.equipment['offhand'] != 'empty':
        if pC.equipment['offhand'].kind == 'dagger':
            attacks += pC.agility * 0.1
    while attacks > 0 and combatant_mobs!= [] and pC.stamina > 0:
        staminaCost = 70
        for i in range(pC.endurance):
            staminaCost *= 0.7
        staminaCost -= staminaCost % 1
        if pC.stamina < staminaCost:
            os.system('clear')
            print("You don't have enough stamina!")
            break
        os.system('clear')
        print("Whick one do you want to attack?")
        mobNumber = 1
        for mob in combatant_mobs:
            print("\t" + str(mobNumber) + ". " + mob.kind.title() + "\n\t\t", end='')
            mob.health -= mob.health % 1
            largeHealthBar(mob.maxHealth, mob.health)
            print(str(mob.health) + "/" + str(mob.maxHealth))
            mobNumber += 1
        thisOne = input()
        try:
            thisOne = int(thisOne) - 1
            thisOne = combatant_mobs[thisOne]
        except:
            break
        if pC.equipment['mainhand'] == 'empty':
            multiplier = pC.strength
        elif pC.equipment['mainhand'].playerClass == 'warrior':
            multiplier = pC.strength
        elif pC.equipment['mainhand'].playerClass == 'ranger':
            multiplier = pC.perception
        elif pC.equipment['mainhand'].playerClass == 'rogue':
            multiplier = pC.agility
        elif pC.equipment['mainhand'].playerClass == 'mage':
            multiplier = pC.intelligence
        elif pC.equipment['mainhand'].playerClass == 'bard':
            multiplier = pC.dexterity
        attackStrength = 1
        for i in range(multiplier):
            attackStrength += 0.2
        attackStrength *= pC.attack
        criticalChance = 100
        for i in range(pC.perception):
            criticalChance /= 0.8
        criticalChance -= criticalChance % 1
        criticalChance = random.randint(1, criticalChance)
        if criticalChance == 1:
            attackStrength *= 2.5
            os.system('clear')
            print("You just got a critical hit for 2.5X damage.")
            null = input()
        thisOne.health -= attackStrength
        pC.stamina -= staminaCost
        if thisOne.health <= 0:
            thisOne.dropItem()
            combatant_mobs.remove(thisOne)
            dead_mobs.append(thisOne)
            pC.xp += thisOne.maxHealth
            pC.levelUpCheck()
        attacks -= 1
    passiveDefend()
    passiveRecoverMana(0.075)

def activeHeal():
    manaCost = 70
    healthRecover = 0.15
    for i in range(pC.intelligence):
        manaCost *= 0.7
    for i in range(pC.intelligence):
        healthRecover += 0.02
    if pC.mana < manaCost:
        os.system('clear')
        print("You don't have enough Mana!")
        null = input()
    else:
        pC.mana -= manaCost
        pC.health += pC.maxHealth * healthRecover
        if pC.health > pC.maxHealth:
            pC.health = pC.maxHealth
    passiveDefend()
    passiveRecoverStamina(0.075)

def passiveRecoverStamina(multiplier):
    if pC.stamina > pC.maxStamina:
        pC.stamina = pC.maxStamina
    elif pC.stamina < pC.maxStamina:
        pC.stamina += pC.maxStamina * multiplier

def passiveRecoverMana(multiplier):
    if pC.mana > pC.maxMana:
        pC.mana = pC.maxMana
    elif pC.mana < pC.maxMana:
        pC.mana += pC.maxMana * multiplier

def passiveRecoverHealth(multiplier):
        if pC.health > pC.maxHealth:
            pC.health = pC.maxHealth
        elif pC.health < pC.maxHealth:
            pC.health += pC.maxHealth * multiplier

def runAway():
    print("Running away hasn't been implemented yet.")
    null = input()

def gimmeASecond():
    print("Consumables have not been implemented yet.")
    null = input()

def combat():
    while combatant_mobs:
        actionCost = 70
        if pC.equipment['mainhand'] == 'empty':
            drain = pC.stamina
            maxDrain = pC.maxStamina
            multiplier = pC.endurance
            stat = "Stamina"
        elif pC.equipment['mainhand'].playerClass == 'mage':
            drain = pC.mana
            maxDrain = pC.maxMana
            multiplier = pC.intelligence
            stat = "Mana"
        elif pC.equipment['mainhand'].playerClass == 'bard':
            drain = pC.mana
            maxDrain = pC.maxMana
            multiplier = pC.dexterity
            stat = "Mana"
        else:
            drain = pC.stamina
            maxDrain = pC.maxStamina
            multiplier = pC.endurance
            stat = "Stamina"
        for i in range(multiplier):
            actionCost *= 0.7
        os.system('clear')
        print("You are being attacked by:")
        mobNumber = 1
        for mob in combatant_mobs:
            print("\t" + str(mobNumber) + ". " + mob.kind.title() + "\n\t\t", end='')
            mob.health -= mob.health % 1
            largeHealthBar(mob.maxHealth, mob.health)
            print(str(mob.health) + "/" + str(mob.maxHealth))
            mobNumber += 1
        print("What do you want to do?\n\t1. Attack\n\t2. Defend\n\t3. Heal\n\t4. Run\n\t5. Use Equipped Consumable")
        playerBars()
        choice = input()
        if choice == '1':
            if 0 < drain - actionCost:
                attack()
                drain -= actionCost
            else:
                os.system('clear')
                print("You don't have enough " + stat + "!")
                null = input()
        elif choice == '2':
            activeDefend()
        elif choice == '3':
            activeHeal()
        elif choice == '4':
            runAway()
        elif choice == '5':
            gimmeASecond()
        followOrRandomMove()

for mob in not_dead_mobs:
    game_map[mob.row][mob.col] = mob
game_map[pC.row][pC.col] = pC
while pC.health > 0:
    passiveRecoverHealth(0.05)
    passiveRecoverStamina(0.1)
    passiveRecoverMana(0.1)
    display()
    playerBars()
    direction = input()
    if direction == 'w':
        moveUp()
    elif direction == 'a':
        moveLeft()
    elif direction == 's':
        moveDown()
    elif direction == 'd':
        moveRight()
    elif direction == '1':
        pC.viewInventory()
    elif direction == '2':
        pC.equipSomething()
        pC.calculateRatings()
    elif direction == '3':
        pC.showEquipment()
    game_map[pC.row][pC.col] = pC
    followOrRandomMove()
    for mob in not_dead_mobs:
        game_map[mob.row][mob.col] = mob
    combatCheck()
    if combatant_mobs:
        combat()
