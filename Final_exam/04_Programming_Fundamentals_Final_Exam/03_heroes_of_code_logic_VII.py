number_heroes = int(input())
hp_and_mp_by_hero = {}
for _ in range(number_heroes):
    hero = [el for el in input().split()]
    name, health, mana= hero[0], int(hero[1]),int(hero[2])
    hp_and_mp_by_hero[name]={}
    hp_and_mp_by_hero[name].update({'HP': health})
    hp_and_mp_by_hero[name].update({'MP': mana})

cmd = input()
while not cmd == 'End':
    cmd = [el for el in cmd.split(" - ")]
    task, name = cmd[0], cmd[1]
    if task == 'CastSpell':
        mana_needed, spell_name = int(cmd[2]), cmd[3]
        if not mana_needed <= hp_and_mp_by_hero[name]['MP']:
            print(f"{name} does not have enough MP to cast {spell_name}!")
            cmd = input()
            continue
        hp_and_mp_by_hero[name]['MP'] -= mana_needed
        print(f"{name} has successfully cast {spell_name} and now has {hp_and_mp_by_hero[name]['MP']} MP!")
    elif task == 'TakeDamage':
        damage, attacker = int(cmd[2]), cmd[3]
        if hp_and_mp_by_hero[name]['HP'] <= damage:
            print(f"{name} has been killed by {attacker}!")
            del hp_and_mp_by_hero[name]
            cmd = input()
            continue
        hp_and_mp_by_hero[name]['HP'] -= damage
        print(f"{name} was hit for {damage} HP by {attacker} and now has {hp_and_mp_by_hero[name]['HP']} HP left!")
    elif task == 'Recharge':
        mana = int(cmd[2])
        if 200 < hp_and_mp_by_hero[name]['MP'] + mana:
            mana = 200 - hp_and_mp_by_hero[name]['MP']
            hp_and_mp_by_hero[name]['MP'] = 200
        else:
            hp_and_mp_by_hero[name]['MP'] += mana
        print(f"{name} recharged for {mana} MP!")
    elif task == 'Heal':
        health = int(cmd[2])
        if 100 < hp_and_mp_by_hero[name]['HP'] + health:
            health = 100 - hp_and_mp_by_hero[name]['HP']
            hp_and_mp_by_hero[name]['HP'] = 100
        else:
            hp_and_mp_by_hero[name]['HP'] += health
        print(f"{name} healed for {health} HP!")
    cmd = input()

for hero in hp_and_mp_by_hero:
    print(f"{hero}")
    print(f"  HP: {hp_and_mp_by_hero[hero]['HP']}")
    print(f"  MP: {hp_and_mp_by_hero[hero]['MP']}")


'''
TASK:
On the first line of the standard input, you will receive an integer n – the number of heroes that you can choose for 
your party. On the next n lines, the heroes themselves will follow with their hit points and mana points separated by a 
single space in the following format: 
"{hero name} {HP} {MP}"
HP stands for hit points and MP for mana points
a hero can have a maximum of 100 HP and 200 MP
After you have successfully picked your heroes, you can start playing the game. You will be receiving different commands, 
each on a new line, separated by " – ", until the "End" command is given. 
There are several actions that the heroes can perform:
"CastSpell – {hero name} – {MP needed} – {spell name}"
If the hero has the required MP, he casts the spell, thus reducing his MP. Print this message: 
"{hero name} has successfully cast {spell name} and now has {mana points left} MP!"
If the hero is unable to cast the spell print:
"{hero name} does not have enough MP to cast {spell name}!"
"TakeDamage – {hero name} – {damage} – {attacker}"
Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0) print:
"{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"
If the hero has died, remove him from your party and print:
"{hero name} has been killed by {attacker}!"
"Recharge – {hero name} – {amount}"
The hero increases his MP. If it brings the MP of the hero above the maximum value (200), MP is increased to 200. 
(the MP can't go over the maximum value).
 Print the following message:
"{hero name} recharged for {amount recovered} MP!"
"Heal – {hero name} – {amount}"
The hero increases his HP. If a command is given that would bring the HP of the hero above the maximum value (100), HP 
is increased to 100 (the HP can't go over the maximum value).
 Print the following message:
"{hero name} healed for {amount recovered} HP!"
Input
On the first line of the standard input, you will receive an integer n.
On the following n lines, the heroes themselves will follow with their hit points and mana points separated by a space 
in the following format.
You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given.
Output
Print all members of your party who are still alive, in the following format (their HP/MP need to be indented 2 spaces):
"{hero name}
  HP: {current HP}
  MP: {current MP}"
'''