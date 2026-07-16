"""Functions to manage a users shopping cart items."""
# https://note.nkmk.me/en/python-collections-counter/
from collections import Counter


def add_item(current_cart, items_to_add):
    """Add items to shopping cart."""
    return dict(Counter(current_cart) + Counter(items_to_add))


def read_notes(notes):
    """Create user cart from an iterable notes entry."""
    return dict(Counter(notes))


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary."""
    return ideas | dict(recipe_updates)


def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order."""
    return {key: cart[key] for key in sorted(cart)}


def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information."""
    return {
        item: [cart[item]] + aisle_mapping[item] 
        for item in sorted(cart, reverse=True) 
        if item in aisle_mapping
    }


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order."""
    for item, info in fulfillment_cart.items():
        store_inventory[item][0] -= info[0]
        if store_inventory[item][0] <= 0:
            store_inventory[item][0] = 'Out of Stock'
                
    return store_inventory
