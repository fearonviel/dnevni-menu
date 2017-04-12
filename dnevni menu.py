#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("Pozdravljeni.")

jedilnik = {}

while True:
    vnos_jedi = raw_input("Vnesite dnevno jed: ")
    vnos_cene = raw_input("Vnesite ceno: ")
    jedilnik[vnos_jedi] = vnos_cene

    new = raw_input("Želite vnesti novo jed? (Da/ne)").lower()

    if new == "ne":
        break

with open("menu.txt", "w+") as menu_file:
    print("Dnevni menu:")
    menu_file.write("Dnevni menu:\n")
    for item in jedilnik:
        print(item + "    " + jedilnik[item] + " €")
        menu_file.write(item + "    " + jedilnik[item] + " €" + "\n")