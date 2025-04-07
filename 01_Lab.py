# Python Application üzerinden MongoDB veri tabanına erişmek için

from pymongo import MongoClient
from pprint import pprint
import re # Regex Modülü

# Connection String oluşturalım ki APP Site'tan Server Side'a erişebilelim.

conn = MongoClient('mongodb://localhost:(Port)')

# Server üzerinden bir veritabanı yaratım

db = conn['app_db']

# veri tabanı içerisinde bir collection yaratalım

collection = db['products']

# region Insert One Record

productname= input("Name: ")
price = input("Price: ")
product = {
    'name': productname,
    'price': price
}
result = collection.insert_one(product)
print(result)

# endregion

#region Insert Many Record

product_list = [
    {"_id": 1, "name": "Lenovo X1 Carbon", "price": 84.999},
    {"_id": 2, "name": "Macbook Pro M3", "price": 184.999},
    {"_id": 3, "name": "Asus Zen", "price": 144.999},
    {"_id": 4, "name": "Monster Abra A7", "price": 59.999},
    {"_id": 5, "name": "Monster Tulpar", "price": 33.999},
]
result = collection.insert_many(product_list)
print(result)

#endregion

# region Read ALL

for each in collection.find():
    print(each)


# endregion

region Fiyat 100k üstü sırala
filter_input = {
    "price": {
        "$gt": 100.000
    }
}
for i in collection.find(filter_input):
    print(i)

# endregion

# region Fiyat 80k'dan az yada eşit sırala
filter_input = {
    "price": {
        "$lte": 80.000
    }
}
for i in collection.find(filter_input):
    print(i)

# endregion

# region Fiyat 59.999 olan ürünleri sırala
filter_input = {
    "price": {
        "$eq": 59.999
    }
}
for i in collection.find(filter_input):
    print(i)

# endregion

# region Fiyat aralığı  üstü sırala
query = {
    "price": {
        "$gte": 10.000,
        "$lte": 60.000,
    },
    "name": {
        "$regex": "Monster"
    }
}
for i in collection.find(query):
    print(i)

# endregion

# region REGEX
# ^ sembolü kendisinden sonra gelen karakterli olmayanları eler
# * baş harf demek,
# . ise herhangi bir karakter demek (boşluk hariç)
# örnekteki Sadece L ile başlayanlar demek
pattern = re.compile('^L.*')
query = {
    'name': {"$regex": pattern}
}

for item in collection.find(query):
    pprint(item)
# endregion

# region Update

result = collection.update_one(
    {'name': 'Monster Abra'}, #filter
    {
        '$set': {                  #update
            'name': 'Machintosh',
            'price': 69.999
        }
    }
)

print(f"{result.modified_count} adet kayıt güncellendi")
# endregion
