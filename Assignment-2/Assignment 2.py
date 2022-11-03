import random
class Product:
    def __init__(self,code,name,price,manu_cost,stock,month_units):
        print("*** Morgan's Sample Stock Statment ***")
        print("Product Code:",code,)
        print("Product Name:",name,)

        print("Sale Price:",price,"CAD")
        print("Manufacture Cost:",manu_cost,"CAD")
        print("Monthly Production:",month_units,"units (Approx.)")

        for month in range(1,12):
            print("Month",month,":")
            print("Manufactured:",month_units,)
            Sold = month_units + random.randrange(-10,10)
            print("Sold:",Sold,)
            new_stock = stock - Sold
            print("Stock:",new_stock)



    
    

the_loop = False

class Application:

    
    print("Welcome to Morgan's Magnificent Products")
    code = input("Please enter your Product's code: ")
    name = input("Please enter the Name of your Product: ")
    price = input("Please enter the Price of the Product: ")
    manu_cost = input("Please enter the Manufacturing Cost: ")
    stock = input("Please enter the amount of Stock of the Product: ")
    month_units = input("Please enter the amount of Stock made in a Month: ")
    App_product = Product(code,name,price,manu_cost,stock,month_units)
