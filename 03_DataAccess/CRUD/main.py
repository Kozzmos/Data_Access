from bson.objectid import ObjectId
from service import CategoryService
from models import Category

service = CategoryService()

# pk = input("pk: ")
# service.get_by_id(pk)
name = input("Name: ")
desc = input("Description: ")
new_category = Category(name, desc)
service.create(new_category.__dict__)