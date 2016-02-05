def item_order(order):
    s = order.count('salad')
    b = order.count('hamburger')
    w= order.count('water')    
   
    return 'salad:' + str(s) + ' hamburger:' + str(b) + ' water:' + str(w)
    
print item_order('salad water hamburger salad hamburger')
