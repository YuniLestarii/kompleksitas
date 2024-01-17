def knapsack_backtracking(current_item, remaining_capacity, selected_items, current_value, best_solution):
    if current_item == len(items):
        if current_value > best_solution["value"] and remaining_capacity >= 0:
            best_solution["value"] = current_value
            best_solution["items"] = selected_items.copy()
        return

    # Coba tambahkan barang ke dalam tas
    if items[current_item]["weight"] <= remaining_capacity:
        selected_items.append(items[current_item]["name"])
        knapsack_backtracking(
            current_item + 1,
            remaining_capacity - items[current_item]["weight"],
            selected_items,
            current_value + items[current_item]["value"],
            best_solution
        )
        selected_items.pop()  # Backtrack

    # Coba tidak menambahkan barang ke dalam tas
    knapsack_backtracking(
        current_item + 1,
        remaining_capacity,
        selected_items,
        current_value,
        best_solution
    )

# Inisialisasi barang-barang dan kapasitas tas
items = [
    {"name": "Pedang Ajaib", "weight": 5, "value": 12},
    {"name": "Potion Kekekalan", "weight": 3, "value": 8},
    {"name": "Kompas Magis", "weight": 1, "value": 4},
    {"name": "Mantel Kehancuran", "weight": 6, "value": 20},
    {"name": "Tongkat Cahaya", "weight": 2, "value": 6}
]

capacity = 10

# Inisialisasi solusi terbaik
best_solution = {"value": 0, "items": []}

# Mulai proses backtracking
knapsack_backtracking(0, capacity, [], 0, best_solution)

# Output hasil
print("Kombinasi barang terbaik:", best_solution["items"])
print("Nilai total yang dapat diperoleh:", best_solution["value"])
