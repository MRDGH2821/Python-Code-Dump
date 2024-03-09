"""
Fixed Warehouse Challenge
"""


class Product:
    _count = 0

    def __init__(self, name: str):
        if Product._count < Limit.get_limit():
            self.name = name
            Product._count += 1
        else:
            raise UserLimitExceeded(
                f"Product {name} cannot be created Maximum {
                    Limit.get_limit()} products allowed."
            )

    def __del__(self):
        Product._count -= 1


class UserLimitExceeded(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class Limit:
    _limit: int = 10

    @classmethod
    def get_limit(cls) -> int:
        return cls._limit

    @classmethod
    def set_limit(cls, limit: int | str):
        cls._limit = int(limit)


def main():
    max_limit = int(input("Max Limit: "))
    Limit.set_limit(max_limit)
    products: dict['str', 'Product'] = {}

    def new_product(name: str) -> str:
        product = Product(name)
        products[name] = product
        return f"Product {name} created"

    def del_product(name: str) -> str:
        product = products.get(name, f"{name} not found")
        if isinstance(product, Product):
            del products[name]
            return f"Product {name} deleted successfully"
        raise UserLimitExceeded(product)

    def print_product(name: str) -> str:
        product = products.get(name, f"{name} not found")
        if isinstance(product, Product):
            return f"Product {name} found"
        raise UserLimitExceeded(product)

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
        except UserLimitExceeded as e:
            print(e)


if __name__ == "__main__":
    main()
