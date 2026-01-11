MAX_WEIGHT = 20

max_items = int(input("Enter the maximum number of items to be shipped: "))

packages_sent = 0
total_weight = 0

current_weight = 0
unused_capacities = []

items_count = 0

while items_count < max_items:
    try:
        weight = int(input("Enter item weight (1-10 kg, 0 to stop): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if weight == 0:
        break

    if weight < 1 or weight > 10:
        print("Item weight must be between 1 and 10 kg.")
        continue

    items_count += 1

    if current_weight + weight > MAX_WEIGHT:
        packages_sent += 1
        total_weight += current_weight
        unused_capacities.append(MAX_WEIGHT - current_weight)
        current_weight = weight
    else:
        current_weight += weight

if current_weight > 0:
    packages_sent += 1
    total_weight += current_weight
    unused_capacities.append(MAX_WEIGHT - current_weight)

total_unused = packages_sent * MAX_WEIGHT - total_weight

max_unused = max(unused_capacities)
package_number = unused_capacities.index(max_unused) + 1

print("\n--- Shipping Summary ---")
print("Number of packages sent:", packages_sent)
print("Total weight of packages sent:", total_weight, "kg")
print("Total unused capacity:", total_unused, "kg")
print("Package with most unused capacity: Package", package_number,
      "with", max_unused, "kg unused")
