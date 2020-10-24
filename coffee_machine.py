# Write your code here
# water1 = 200
# milk1 = 50
# beans1 = 15
#
# wat = int(input("Write how many ml of water the coffee machine has: "))
# mil = int(input("Write how many ml of milk the coffee machine has: "))
# bea = int(input("Write how many grams of coffee beans the coffee machine has: "))
#
# cup = int(input("Write how many cups of coffee you will need: "))
#
# water2 = water1 * cup
# milk2 = milk1 * cup
# beans2 = beans1 * cup
#
# if water2 - wat >= 0 and milk2 - mil >= 0 and beans2 - bea >= 0:
#     pass

# cup = int(input("Write how many cups of coffee you well need: "))
# print("for ", cup, " cups of coffee you will need:")
# print(water1 * cup, "ml of water")
# print(milk1 * cup, "ml of milk")
# print(beans1 * cup, "g of coffee beans")
# print("Starting to make a coffee")
# print("Grinding coffee beans")
# print("Boiling water")
# print("Mixing boiled water with crushed coffee beans")
# print("Pouring coffee into the cup")
# print("Pouring some milk into the cup")
# print("Coffee is ready!")
pass
# n_water = int(input())
# n_milk = int(input())
# n_coffee_beans = int(input())
# n_cups = int(input())
#
# ingredients = {'water': 200, 'milk': 50, 'coffee beans': 15}
# units = {'water': 'ml', 'milk': 'ml', 'coffee beans': 'g'}
# keys = ['water', 'milk', 'coffee beans']
#
# if n_cups != 0 and n_water != 0:
#
#     n1 = n_cups * ingredients['water']
#     n2 = n_cups * ingredients['milk']
#     n3 = n_cups * ingredients['coffee beans']
#
#     p1 = n_water // n1
#     p2 = n_milk // n2
#     p3 = n_coffee_beans // n3
#
#     q = min(p1, p2, p3)
#
#     c1 = n_water // ingredients['water']
#     c2 = n_milk // ingredients['milk']
#     c3 = n_coffee_beans // ingredients['coffee beans']
#
#     k = min(c1, c2, c3)
#
#     if q == n_cups:
#         print("Yes, I can make that amount of coffee")
#     else:
#         if n_cups >= k:
#             print("No, I can make only {} cups of coffee".format(k))
#         else:
#             print("Yes, I can make that amount of coffee (and even {} more than that)".format(k - n_cups))
#
# elif n_cups != 0 and n_water == 0:
#     print("No, I can make only {} cups of coffee".format(n_water))
#
# elif n_cups == 0 and n_water != 0:
#
#     c1 = n_water // ingredients['water']
#     c2 = n_milk // ingredients['milk']
#     c3 = n_coffee_beans // ingredients['coffee beans']
#
#     k = min(c1, c2, c3)
#
#     print("Yes, I can make that amount of coffee (and even {} more than that)".format(k - n_cups))
#
# else:
#     print("Yes, I can make that amount of coffee")
pass
wat_in_meh = 400
mil_in_meh = 540
bea_in_meh = 120
cup_in_meh = 9
man_in_meh = 550

espresso_wat = 250
espresso_bea = 16
espresso_man = 4

latte_wat = 350
latte_mil = 75
latte_bea = 20
latte_man = 7

cappuccino_wat = 200
cappuccino_mil = 100
cappuccino_bea = 12
cappuccino_man = 6


def stats(wat, mil, bea, cup, man):
    print("The coffee machine has:")
    print(str(wat) + " of water")
    print(str(mil) + " of milk")
    print(str(bea) + " of coffee beans")
    print(str(cup) + " of disposable cups")
    print(str(man) + " of money")
    

while True:
    print("")
    print("Write action (buy, fill, take, remaining, exit): ")
    action = input()
    if action == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back to main menu:")
        buy_kof = input()
        if buy_kof == "1":
            if wat_in_meh - espresso_wat > 0:
                if bea_in_meh - cappuccino_bea > 0:
                    if cup_in_meh - 1 > 0:
                        print("I have enough resources, making you a coffee!")
                    else:
                        print("Sorry, not enough cup!")
                        continue
                else:
                    print("Sorry, not enough beans!")
                    continue
            else:
                print("Sorry, not enough water!")
                continue
            wat_in_meh -= espresso_wat
            bea_in_meh -= espresso_bea
            man_in_meh += espresso_man
            cup_in_meh -= 1

        elif buy_kof == "2":
            if wat_in_meh - latte_wat > 0:
                if mil_in_meh - latte_mil > 0:
                    if bea_in_meh - latte_bea > 0:
                        if cup_in_meh - 1 > 0:
                            print("I have enough resources, making you a coffee!")
                        else:
                            print("Sorry, not enough cup!")
                            continue
                    else:
                        print("Sorry, not enough beans!")
                        continue
                else:
                    print("Sorry, not enough milk!")
                    continue
            else:
                print("Sorry, not enough water!")
                continue
            wat_in_meh -= latte_wat
            mil_in_meh -= latte_mil
            bea_in_meh -= latte_bea
            man_in_meh += latte_man
            cup_in_meh -= 1

        elif buy_kof == "3":
            if wat_in_meh - cappuccino_wat > 0:
                if mil_in_meh - cappuccino_mil > 0:
                    if bea_in_meh - cappuccino_bea > 0:
                        if cup_in_meh - 1 > 0:
                            print("I have enough resources, making you a coffee!")
                        else:
                            print("Sorry, not enough cup!")
                            continue
                    else:
                        print("Sorry, not enough beans!")
                        continue
                else:
                    print("Sorry, not enough milk!")
                    continue
            else:
                print("Sorry, not enough water!")
                continue
            wat_in_meh -= cappuccino_wat
            mil_in_meh -= cappuccino_mil
            bea_in_meh -= cappuccino_bea
            man_in_meh += cappuccino_man
            cup_in_meh -= 1

        elif buy_kof == "back":
            continue

    elif action == "fill":
        print("Write how many ml of water do you want to add:")
        wat_in_meh_sot = int(input())
        print("Write how many ml of milk do you want to add:")
        mil_in_meh_sot = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        bea_in_meh_sot = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        cup_in_meh_sot = int(input())

        wat_in_meh += wat_in_meh_sot
        mil_in_meh += mil_in_meh_sot
        bea_in_meh += bea_in_meh_sot
        cup_in_meh += cup_in_meh_sot

    elif action == "take":
        print("I gave you $" + str(man_in_meh))
        man_in_meh -= man_in_meh

    elif action == "remaining":
        stats(
            wat_in_meh,
            mil_in_meh,
            bea_in_meh,
            cup_in_meh,
            man_in_meh
        )

    elif action == "exit":
        break
