guests_count = 0

with open('guests.txt', 'rt', encoding="utf-8") as file:
    # guests_count = len(file.readlines())
    for line in file:
        print(line)
        guests_count += 1


print(f"Количество гостей = {guests_count}")
