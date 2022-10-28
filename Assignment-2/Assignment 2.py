class Product:
    print("*** Morgan's Sample Stock Statment ***")
    def __init__(self,code,name,price,manu_cost,stock,month_units):
        print("Product Code:",code,)
        print("Product Name:",name,)

        print("Sale Price:",price,"CAD")
        print("Manufacture Cost:",manu_cost,"CAD")
        print("Monthly Production:",month_units,"units (Approx.)")
    
    



class Application:

    print("Welcome to Morgan's Magnificent Products")
    code = input("Please enter your Product's code: ")
    name = input("Please enter the Name of your Product: ")
    price = input("Please enter the Price of the Product: ")
    manu_cost = input("Please enter the Manufacturing Cost: ")
    stock = input("Please enter the amount of Stock of the Product: ")
    month_units = input("Please enter the amount of stock made in a month: ")



    
    App_product = Product(code,name,price,manu_cost,stock,month_units)
