n = int(input())

scary_numbers = []
not_scary_numbers = []
none_numbers = []

for _ in range(n):
    num = int(input())
    if num % 3 == 0 and abs(num) > 9:
        scary_numbers.append(num)
    elif num % 3 != 0 and num % 2 != 0:
        not_scary_numbers.append(num)
    else:
        none_numbers.append(num)

max_scary = max(scary_numbers) if scary_numbers else None
sum_not_scary = sum(not_scary_numbers)
sum_abs_none = sum(abs(num) for num in none_numbers)

print(f"{max_scary if max_scary is not None else 'none'}: scary.")
print(f"{sum_not_scary}: not scary.")
print(f"{sum_abs_none}: none.")