class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product):
        if len(self.storage) < self.capacity:
            self.storage.append(product)

    def get_products(self):
        return self.storage


'''
TASK:
Create a class Storage. The __init__ method should accept one parameter - the capacity of the storage. The Storage class
 should also have an attribute called storage, where all the items will be stored. The class should have two additional 
 methods:
add_product(product) - adds the product in the storage if there is space for it
get_products() - returns the storage list
'''