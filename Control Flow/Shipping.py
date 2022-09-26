# Shipping
# Jomer Cabrera

weight = 34.4

#Ground Shipping
cost_ground = 20
if weight <= 2:
  cost_ground += weight * 1.5
elif weight <= 6:
  cost_ground += weight * 3.0
elif weight <= 10:
  cost_ground += weight * 4.0
else:
  cost_ground += weight * 4.75

print("Ground Shipping: $", cost_ground)

#Premium Ground Shipping
premiumGroundShipping = 125.00
print("Ground Shipping Premium: $", premiumGroundShipping)

#Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.5
elif weight <= 6:
  cost_drone = weight * 9.0
elif weight <= 10:
  cost_drone = weight * 12.0
else:
  cost_drone = weight * 14.25

print("Drone Shipping: $",cost_drone)