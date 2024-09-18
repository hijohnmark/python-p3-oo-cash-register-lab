#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
      self.discount = discount
      self.total = 0
      self.items = []
      self.last_transaction = {"price": 0, "quantity": 0}

  def add_item(self, title, price, quantity=1):
      for _ in range(quantity):
          self.items.append(title)
      self.total += price * quantity
      self.last_transaction = {"price": price, "quantity": quantity}
    
  def apply_discount(self):
      if self.discount == 0:
         print("There is no discount to apply.") 
      else:
          self.total -= self.total * (self.discount/100)
          print(f"After the discount, the total comes to ${int(self.total)}.")
  

  def void_last_transaction(self):
      if self.items:
          for _ in range(self.last_transaction["quantity"]):
              self.items.pop()
          self.total -= self.last_transaction["price"] * self.last_transaction["quantity"]
      else:
          self.total = 0.0
          