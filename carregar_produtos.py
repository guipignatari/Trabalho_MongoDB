import random
import string
from pymongo import MongoClient

# Função para gerar um ID aleatório
def generate_id(prefix, length=6):
    return prefix + ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


# Função para gerar um produto aleatório
def generate_product():
    product_names = product_names = [
    "Arroz Integral", "Feijão Preto", "Macarrão", "Azeite", "Farinha",
    "Açúcar", "Café", "Leite", "Pão", "Manteiga", "Queijo", "Presunto",
    "Frango", "Carne Moída", "Peixe", "Cenoura", "Batata", "Tomate",
    "Alface", "Maçã", "Banana", "Laranja", "Uva", "Morango", "Melancia",
    "Mamão", "Abacaxi", "Iogurte", "Requeijão", "Margarina", "Biscoito",
    "Cereal", "Granola", "Aveia", "Mel", "Geléia", "Suco de Laranja",
    "Refrigerante", "Água Mineral", "Vinho", "Cerveja", "Whisky", "Vodka",
    "Gin", "Rum", "Tequila", "Licor", "Champagne", "Salsicha", "Linguiça",
    "Bacon", "Salmão", "Camarão", "Atum", "Sardinha", "Ovos", "Amendoim",
    "Castanha", "Nozes", "Amêndoa", "Pistache", "Torrada", "Maionese",
    "Ketchup", "Mostarda", "Molho de Soja", "Vinagre", "Sal", "Pimenta",
    "Orégano", "Manjericão", "Salsa", "Coentro", "Louro", "Alho", "Cebola",
    "Pepino", "Pimentão", "Abobrinha", "Berinjela", "Brócolis", "Couve-flor",
    "Espinafre", "Rúcula", "Chá Verde", "Chá Preto", "Chá de Camomila",
    "Chá de Hortelã", "Bebida de Soja", "Leite de Amêndoa", "Leite de Coco",
    "Leite de Aveia", "Iogurte Grego", "Queijo Cottage", "Ricota",
    "Creme de Leite", "Leite Condensado", "Doce de Leite", "Chocolate",
    "Sorvete"
]
    descriptions = descriptions = [
    "Pacote de 1kg", "Pacote de 500g", "Garrafa de 1L", "Pacote de 250g",
    "Lata de 350ml", "Lata de 500ml", "Caixa com 12 unidades", "Caixa com 6 unidades",
    "Frasco de 200ml", "Frasco de 500ml", "Saco de 2kg", "Saco de 5kg",
    "Embalagem de 300g", "Embalagem de 400g", "Embalagem de 600g", "Embalagem de 800g",
    "Garrafão de 5L", "Pote de 1kg", "Pote de 500g", "Pote de 200g",
    "Barra de 100g", "Barra de 200g", "Caixa de 1L", "Caixa de 2L",
    "Saco de 250g", "Saco de 1kg", "Saco de 500g", "Vidro de 300ml",
    "Vidro de 700ml", "Vidro de 1L", "Garrafa de 750ml", "Garrafa de 2L",
    "Garrafa de 330ml", "Pacote de 100g", "Pacote de 50g", "Embalagem de 1kg",
    "Pacote de 5kg", "Caixa com 4 unidades", "Caixa com 8 unidades", "Caixa com 10 unidades",
    "Lata de 1kg", "Lata de 2kg", "Lata de 300g", "Lata de 400g",
    "Frasco de 100ml", "Frasco de 250ml", "Frasco de 750ml", "Vidro de 500ml",
    "Embalagem de 100g", "Embalagem de 150g", "Embalagem de 250g", "Embalagem de 500g",
    "Pacote de 1.5kg", "Pacote de 750g", "Garrafa de 3L", "Saco de 3kg",
    "Saco de 4kg", "Barra de 300g", "Caixa com 20 unidades", "Caixa com 24 unidades",
    "Caixa com 30 unidades", "Pote de 2kg", "Pote de 3kg", "Pote de 700g",
    "Garrafa de 1.5L", "Garrafa de 600ml", "Vidro de 250ml", "Vidro de 200ml",
    "Pacote de 2.5kg", "Pacote de 3kg", "Caixa com 18 unidades", "Caixa com 16 unidades",
    "Lata de 600ml", "Lata de 750ml", "Embalagem de 50g", "Embalagem de 75g",
    "Pacote de 400g", "Pacote de 150g", "Saco de 750g", "Saco de 600g",
    "Frasco de 150ml", "Frasco de 100ml", "Barra de 150g", "Barra de 50g",
    "Garrafa de 500ml", "Garrafa de 2.5L", "Vidro de 750ml", "Vidro de 1.5L",
    "Caixa de 500g", "Caixa de 1.5kg", "Lata de 150g", "Lata de 500g",
    "Embalagem de 2kg", "Embalagem de 4kg", "Pacote de 2kg", "Pacote de 5kg"
]
    price = round(random.uniform(2.0, 20.0), 2)
    product_name = random.choice(product_names)
    description = random.choice(descriptions)
    return {
        "product_id": generate_id("prod"),
        "name": product_name,
        "description": f"{product_name} - {description}",
        "price": price
    }

# Função para gerar uma loja aleatória
def generate_store(product_list):
    store_names = ["Supermercado Central", "Mercado do Bairro", "Loja de Conveniência", "Hipermercado ABC", "Mini Mercado XYZ"]
    locations = ["Cidade X", "Cidade Y", "Cidade Z", "Cidade W", "Cidade V"]
    inventory = [{"product_id": product["product_id"], "quantity": random.randint(10, 200)} for product in random.sample(product_list, random.randint(1, 5))]
    return {
        "store_id": generate_id("store"),
        "name": random.choice(store_names),
        "location": random.choice(locations),
        "inventory": inventory
    }

# Gerar uma lista de produtos
product_list = [generate_product() for _ in range(10)]

# Gerar uma lista de lojas com produtos associados
store_list = [generate_store(product_list) for _ in range(5)]

# Conectando ao servidor do MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Selecionando o banco de dados
db = client.supermarket_inventory

# Selecionando as coleções
stores_collection = db.stores
products_collection = db.products

# Inserindo produtos no banco de dados
for product in product_list:
    products_collection.insert_one(product)

# Inserindo lojas no banco de dados
for store in store_list:
    stores_collection.insert_one(store)

# Consultando produtos em uma loja
for item in stores_collection.find({"store_id": store_list[0]['store_id']}):
    print(item)

# Atualizando o estoque de um produto em uma loja
stores_collection.update_one(
    {"store_id": store_list[0]['store_id'], "inventory.product_id": product_list[0]['product_id']},
    {"$set": {"inventory.$.quantity": 140}}
)

print("\nLista de produtos:")
for product in products_collection.find():
    print(product)

print("\nLista de lojas:")
for store in stores_collection.find():
    print(store)
