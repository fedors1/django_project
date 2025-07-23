from .views import Product


class ProductService:

    @staticmethod
    def return_list_products(category_id=None):
        if category_id is None:
            return Product.objects.all()
        return Product.objects.filter(category_id=category_id)
