from pymongo import MongoClient
from models import Category

# Connect to MongoDB
conn = MongoClient('mongodb://localhost:27017')

db = conn['CRUD_db']

collection = db['categories']
# -----------------------------------------------------------
# Seed Data / Sample Data
# Proje ilk çalıştırıldığında veri tabanı yaratılırken buradaki oluşturulan koleksiyon ile yani data ile yaratılmasına denir
# Bize sağladığı avantaj örneğin hemen read operasyonlarını hızlıca yazabiliriz. Bir tane user yaratılmışsa testler yapılabilir vs vs
# !!!!!!! UYARI bu bloktaki kodları tek sefer çalıştırın
# categories = [
#     Category('Boxing Gloves', 'Everlast produce best boxing gloves').__dict__,
#     Category('Punching Bags', 'Everlast produce best punching bags').__dict__,
#     Category('Protective Equipments', 'Everlast produce best protective equipments').__dict__,
# ]
#
# collection.insert_many(categories)
