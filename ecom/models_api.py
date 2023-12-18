from ecom import models

class ProductsModels:

    def get_product_details_by_category_id(self, category_id: str):
        products_data = models.Products.objects.filter(category_id = category_id, is_active = True)
        return products_data
