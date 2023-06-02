from django.apps import AppConfig


class ProductConfig(AppConfig):
    name = 'product'

    def ready(self):
        from product.utils import insert_category, insert_product
        
        insert_category()
        insert_product()
        return super().ready()