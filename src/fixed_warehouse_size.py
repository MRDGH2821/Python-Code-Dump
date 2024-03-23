"""Fixed Warehouse Challenge."""

from __future__ import annotations


class Product:
    """Product class to create products with a global limit."""

    _count = 0

    def __init__(self, name: str) -> None:
        """Create a product & increase global product count."""
        if Product._count < Limit.get_limit():
            self.name = name
            Product._count += 1
        else:
            err_msg = f"Product {name} cannot be created Maximum {
                    Limit.get_limit()} products allowed."
            raise UserLimitExceededError(err_msg)

    def __del__(self) -> None:
        """Decrement global product count on delete."""
        Product._count -= 1


class UserLimitExceededError(Exception):
    """UserLimitExceededError to raise when user limit exceeds."""

    def __init__(self, message: str) -> None:
        """Assign error message to the exception."""
        super().__init__(message)
        self.message = message


class Limit:
    """Limit class to set and get the global limit of products."""

    _limit: int = 10

    @classmethod
    def get_limit(cls) -> int:
        """Return the global limit of products."""
        return cls._limit

    @classmethod
    def set_limit(cls, limit: int | str) -> None:
        """Set the global limit of products."""
        cls._limit = int(limit)


def main() -> None:
    """Create products and perform operations on them."""
    max_limit = int(input("Max Limit: "))
    Limit.set_limit(max_limit)
    products: dict[str, Product] = {}

    def new_product(name: str) -> str:
        product = Product(name)
        products[name] = product
        return f"Product {name} created"

    def del_product(name: str) -> str:
        product = products.get(name, f"{name} not found")
        if isinstance(product, Product):
            del products[name]
            return f"Product {name} deleted successfully"
        raise UserLimitExceededError(product)

    def print_product(name: str) -> str:
        product = products.get(name, f"{name} not found")
        if isinstance(product, Product):
            return f"Product {name} found"
        raise UserLimitExceededError(product)

    def change_limit(limit: str) -> str:
        Limit.set_limit(limit)
        return f"limit updated to {limit}"

    func_map = {
        "new": new_product,
        "del": del_product,
        "print": print_product,
        "limit": change_limit,
    }
    num_operations = int(input("Number of Operations: "))
    for _ in range(num_operations):
        cmd, arg = input("> ").split()
        try:
            res = func_map[cmd](arg)
            print(res)
        except UserLimitExceededError as e:
            print(e)


if __name__ == "__main__":
    main()
