parking_list = []

while True:
    print("1) Enter car's plate")
    print("2) Remove car")
    print("3) Parking report")
    print("4) Search car")
    print("0) Exit")

    option = int(input('Enter your option: '))
    print("-" * 20)

    match option:
        case 0:
            break
        case 1:
            plate = input('Enter plate: ')
            if plate not in parking_list:
                parking_list.append(plate)
                print("plate added")
            else:
                print("Your plate is already in the parking list")
        case 2:
            plate = input('Enter plate: ')
            if plate in parking_list:
                parking_list.remove(plate)
                print("plate removed")
            else:
                print("Your plate is not in the parking list")
        case 3:
            parking_list.sort()
            for plate in parking_list:
                print("Plate number: ", plate)
        case 4:
            plate = input('Enter plate: ')
            if plate in parking_list:
                print("Your plate is in the parking list", plate)
            else:
                print("Not found!!")
        case _:
            print("Invalid option")
    print("-" * 20)