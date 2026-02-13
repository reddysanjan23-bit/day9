import pandas as pd

products = pd.Series(
    [700, 150, 300],
    index=['Laptop', 'Mouse', 'Keyboard']
)

laptop_price = products['Laptop']   


first_two = products.iloc[:2]

print("Full Product Catalog:\n")
print(products)

