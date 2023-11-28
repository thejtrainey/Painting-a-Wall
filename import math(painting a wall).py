import math

# Step 1: Read input values
wall_height = float(input())
wall_width = float(input())
paint_cost_per_can = float(input())

# Step 2: Calculate and output wall area
wall_area = wall_height * wall_width
print(f"Wall area: {wall_area:.1f} sq ft")

# Step 3: Calculate and output amount of paint needed
paint_needed = wall_area / 350
print(f"Paint needed: {paint_needed:.3f} gallons")

# Step 4: Calculate and output number of 1 gallon cans needed
cans_needed = math.ceil(paint_needed)
print(f"Cans needed: {cans_needed} can(s)")

# Step 5: Calculate and output paint cost, sales tax, and total cost
paint_cost = paint_cost_per_can * cans_needed
sales_tax = 0.07 * paint_cost
total_cost = paint_cost + sales_tax

print(f"Paint cost: ${paint_cost:.2f}")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Total cost: ${total_cost:.2f}")
