# รับราคาสินค้า 6 รายการ
prices = []

print("Enter prices of 6 items:")

for i in range(6):
    price = int(input(f"Item {i + 1}: "))
    prices.append(price)

# รับงบประมาณ
budget = int(input("\nEnter total budget: "))

bought_items = []
total = 0

# ตรวจสอบราคาสินค้าตามลำดับ
for i in range(6):
    if total + prices[i] <= budget:
        bought_items.append(prices[i])
        total = total + prices[i]
        print(f"\nItem {i + 1} = {prices[i]} -> buy")
        print(f"Current total = {total}")
    else:
        print(f"\nItem {i + 1} = {prices[i]} -> cannot buy")
        print(f"Current total = {total}")

# แสดงผลสรุป
print("\nBought items:", bought_items)
print("Total spent:", total)
print("Remaining budget:", budget - total)