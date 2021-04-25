
import Main

dict_prices = {
    "Onions" : .50,
    "Tomatoes" : .99,
    "Eggs" : 2.99,
    "Ice Cream" : 4.99
}

dict_quant = {
    "Onions" : 0,
    "Tomatoes" : 0,
    "Eggs" : 0,
    "Ice Cream" : 0
}

def add_item(key):
    dict_quant[key] += 1
 
def remove_item(key):
    if dict_quant[key] == 0:
        return
    else:
        dict_quant[key] -= 1

def clear_cart():
    for keys in dict_quant.keys():
        dict_quant[keys] = 0

def get_qty(key):
    return dict_quant[key]

def get_pr(key):
    return '${:,.2f}'.format(dict_prices[key])


def item_total(key):
    return '${:,.2f}'.format(dict_prices[key] * dict_quant[key])






def subtotal():
    dict_subtotal = {}
    for k,v in dict_prices.items():
        dict_subtotal[k] = v * dict_quant[k]
    return dict_subtotal

def get_total():
    total = 0
    subtotals = subtotal()
    for values in subtotals.values():
        total += values
    return '${:,.2f}'.format(total)



    





# add_item("Onions")
# add_item("Onions")
# add_item("Onions")
# remove_item("Onions")
# add_item("Ice Cream")
# add_item("Ice Cream")
# add_item("Ice Cream")

# subtotal = subtotal()
# total = total(subtotal)
# print(total)

# print(get_qty("Onions"))

# for k,v in x.items():
#     print(f"{k} subtotal {'${:,.2f}'.format(v)} dollars")

