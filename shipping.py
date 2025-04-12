#This program calculates the shipping cost based on weight and type of shipping.

#variables
weight = 4.8
flat_charge = 20.00

#Ground Shipping
if weight <= 2.00:
  price = weight * 1.5 + flat_charge
  print("Ground Shipping Price is " + str(price))
elif weight > 2 and weight <= 6:
  price = weight * 3.0 + flat_charge
  print("Ground Shipping Price is " + str(price))
elif weight > 6 and weight <= 10:
  price = weight * 4.0 + flat_charge
  print("Ground Shipping Price is " + str(price))
else:
  price = weight * 4.75 + flat_charge
  print("Ground Shipping Price is " + str(price))

#Ground Shipping Premium
ground_shipping_premium = 125
print("Ground Shipping Premium is " + str(ground_shipping_premium))

#Drone Shipping
if weight <= 2.00:
  price = weight * 4.5
  print("Drone Price is " + str(price))
elif weight > 2 and weight <= 6:
  price = weight * 9.0
  print("Drone Price is " + str(price))
elif weight > 6 and weight <= 10:
  price = weight * 12.0
  print("Drone Price is " + str(price))
else:
  price = weight * 14.25
  print("Drone Price is " + str(price))  

print("The cheapest option is Ground Shipping") 
print("The second cheapest option is Drone Shipping")

