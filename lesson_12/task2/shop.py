"""
External module with classes for Item, User, Purchase
"""


class Item:
    """
    Represents an item in the shop
    """

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return self.name + ", price: " + str(self.price)


class User:
    """
    Represents a user in the shop
    """

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return self.name + " " + self.surname


class Purchase:
    """
    Represents a purchase in the shop
    """

    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        """
        Change the amount of items in the purchase
        :param item: The item itself
        :param cnt:  The quantity of the item
        """
        self.products[item] = cnt

    def __str__(self):
        items_str = "\n".join(
            [f"{item.name}: {cnt} pcs." for item, cnt in self.products.items()]
        )
        return f"User: {self.user.name} {self.user.surname}\n" f"Items:\n{items_str}"

    def get_total(self):
        """
        Calculates the total cost of purchase
        :return: The total cost
        """
        return sum(item.price * cnt for item, cnt in self.products.items())
