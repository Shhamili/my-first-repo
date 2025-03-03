# sales_data.py

# Weekly sales data: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]
sales_data = [230, 200, 310, 290, 400, 150, 180]
print(f"Sales data for the week: {sales_data}")


def total_sales(data):
    return sum(data)

def average_sales(data):
    return sum(data)/len(data)

print(f'total vanzari: {total_sales(sales_data)} lei')
print(f'media vanzarilor: {average_sales(sales_data):.3f} lei')


def remove_value_min_200(data):
    return [item for item in data if item > 200]

new_data_sales = remove_value_min_200(sales_data)
print(f'vanzarile mai mari de 200: {new_data_sales}')


