from . views import Product


class ProductService:

    @staticmethod
    def return_list_products():
        products = Product.objects.all()
        if not products:
            return None
        return products
