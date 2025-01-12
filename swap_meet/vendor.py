class Vendor:
    def __init__(self, inventory = None):
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        try:
            self.inventory.remove(item)
        except ValueError:
            print("That item is not in the inventory.")
            return False
        else:
            return item
    
    def get_by_category(self, category):
        items_with_category = [item for item in self.inventory if item.category == category]
        return items_with_category
    
    def swap_items(self, vendor, item1, item2):
        try: 
            index_item1 = self.inventory.index(item1) #check for items in respective vendors inventory
            index_item2 = vendor.inventory.index(item2)  
        except ValueError:
            print("Item not found")
            return False
        else:
            self.inventory[index_item1] = item2
            vendor.inventory[index_item2] = item1
            return True

    def swap_first_item(self, vendor):
        try:
            your_item = self.inventory[0] #check that each vendor has an item in their inventory
            their_item = vendor.inventory[0]
        except IndexError:
            print("Item not found")
            return False
        else:
            self.swap_items(vendor, your_item, their_item)
            return True

    def get_best_by_category(self, category):

        #create a list of items with the category
        category_items = [item for item in self.inventory if item.category == category]
        #get the item where item.condition is the greatest
        best_item = max(category_items, key=lambda item: item.condition, default = None)
        return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):

        their_best_item = other.get_best_by_category(my_priority)
        my_best_item = self.get_best_by_category(their_priority)
        return self.swap_items(other, my_best_item, their_best_item)