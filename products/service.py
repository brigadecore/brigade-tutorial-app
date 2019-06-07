import json

from nameko.web.handlers import http
from nameko_sqlalchemy import Database

from products.models import DeclarativeBase, Product


class ProductsService:
    name = "products"

    db = Database(DeclarativeBase)

    @http("POST", "/products/")
    def create_product(self, request):
        payload = json.loads(request.get_data(as_text=True))
        product = Product(**payload)
        with self.db.get_session() as session:
            session.add(product)

        return json.dumps({"id": product.id, "name": product.name})
