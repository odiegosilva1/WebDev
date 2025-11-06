from product import Product


def generate_projects ():
    list_products = []

    # Gera produtos
    for x in range(10):
        p = Product(name = f"Product {x + 1}", price = 4.90 * x )
        list_products.append(p)

    return list_products    