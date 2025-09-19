class Weapon:
    def __init__(self, bullets):
        self.bullets = bullets

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"

    def shoot(self):
        if 0 < self.bullets:
            self.bullets -= 1
            return f"shooting..."

        else:
            return f"no bullets left"


weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)


'''
TASK:
Create a class Weapon. The __init__ method should receive the number of bullets (integer). Create an attribute called 
bullets to store them. The class should also have the following methods:
shoot() - if there are bullets in the weapon, reduce them by 1 and return a message "shooting...". If there are no 
bullets left, return: "no bullets left".
__repr__() - returns "Remaining bullets: {amount_of_bullets}". You can read more about the __repr__ method here: link.
'''