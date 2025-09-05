product_name, product_code = input().split()
product_code = int(product_code)
products=[]
# Please write your code here.
class product:
    def __init__(self,name='',code=0):
        self.name=name 
        self.code=code 

for _ in range(2):
    products.append(product(()))

products[0].name="codetree"
products[0].code=50
products[1].name=product_name
products[1].code=product_code

for i in range(len(products)):
    print(f"product {products[i].code} is {products[i].name}")

