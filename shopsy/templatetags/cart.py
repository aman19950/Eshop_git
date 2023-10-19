from django import template

register = template.Library()


@register.filter(name="isexistincart")
def isexistincart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False


@register.filter(name="cartquantity")
def cartquantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return False



@register.filter(name="total_price")
def total_price(product, cart):
    tp = product.product_price * cartquantity(product,cart)
    return tp


@register.filter(name="checkout_price")
def checkout_price(product, cart):
    s = 0
    for i in product:
        s =  s + total_price(i,cart)
    return s


@register.filter(name="total_order_price")
def total_order_price(price, quantity):
    return price * quantity
    