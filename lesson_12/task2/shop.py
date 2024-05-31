"""
External module with classes for Item, User, Purchase
"""


class Item:
    """
    Represents an item in the shop
    """

    def __init__(
        self, name: str, price: float, description: str, dimensions: str
    ) -> None:
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self) -> str:
        return self.name + ", price: " + str(self.price)


class User:
    """
    Represents a user in the shop
    """

    def __init__(self, name: str, surname: str, numberphone: str) -> None:
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self) -> str:
        return self.name + " " + self.surname


class Purchase:
    """
    Represents a purchase in the shop
    """

    def __init__(self, user: User) -> None:
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item: Item, cnt: int) -> None:
        """
        Change the amount of items in the purchase
        :param item: The item itself
        :param cnt:  The quantity of the item
        """
        self.products[item] = cnt

    def __str__(self) -> str:
        items_str = "\n".join(
            [f"{item.name}: {cnt} pcs." for item, cnt in self.products.items()]
        )
        return f"User: {self.user.name} {self.user.surname}\n" f"Items:\n{items_str}"

    def get_total(self) -> float:
        """
        Calculates the total cost of purchase
        :return: The total cost
        """
        return sum(item.price * cnt for item, cnt in self.products.items())
