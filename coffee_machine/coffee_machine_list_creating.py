no_of_guests = 0
guests_list = []

while no_of_guests >= 0:
    guest_name = input()
    if guest_name == ".":
        break
    no_of_guests += 1
    guests_list.append(guest_name)

print(guests_list)
print(no_of_guests)
