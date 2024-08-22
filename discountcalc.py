
def calculate_discount(price, percentage_discount):
    if percentage_discount >= 20:

        final_price = price - (price *(percentage_discount/100))
        return final_price

    else:
        return price

original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percentage)

if final_price != original_price:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${original_price:.2f}")