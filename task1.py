import random

id_numbers = ["".join(random.sample("00112233445566778899", 11)) for i in range(1000)]

evenCount = 0
count = 0
for ID in id_numbers:
    for number in ID:
        if int(number) % 2 == 0:
            count += 1
    if count == 4:
        evenCount += 1
    count = 0

print(f"სიაში არის {evenCount} პირადი ნომერი, რომელიც შეიცავს მხოლოდ 4 ლუწ ციფრს")


countNumbers = 0
moreThanSeven = 0
for ID in id_numbers:
    for number in ID:
        countNumbers += int(number)
    if countNumbers/11 > 7:
        moreThanSeven += 1
    countNumbers = 0

print(f"სიაში არის {moreThanSeven} პირადი ნომერი, რომელთა ციფრთა ჯამი აღემატება 7 ს")
