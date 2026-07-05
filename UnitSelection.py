lessons_list =[]
sum_lesson = 0

while True:
    print('1) Add a lesson')
    print('2) Report')
    print('0) Exit')
    option = int(input('Enter your option: '))
    print("-" * 20)

    if option == 0:
        break
    elif option == 1:
        lesson = int(input('Enter a lesson units(1,2,3,5): '))
        sum_lesson = sum(lessons_list)
        if lesson in [1,2,3,5] and sum_lesson <= 17:
            lessons_list.append(lesson)
            print("lesson unit added")
        else:
            print("lesson unit not added, sum is greater than 17")
    elif option == 2:
        lessons_list.sort()
        print("lesson unit list" , lessons_list)
        for lesson in lessons_list:
            print(f"{lesson:10} {lessons_list.count(lesson) * '*'}")
        print("-" * 20)
        print("Sum: ", sum_lesson)
    else:
        print("Invalid option")
    print("-" * 20)