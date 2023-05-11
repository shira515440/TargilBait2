# submitted by: Shira Tam 212591770
# this program presents the user 3 options: 1- to choose a rectangle tower. 2- to choose a triangle tower. 3- to exit.
import math


def print_triangle(height, width):
    # initialize the first row of the triangle
    triangle = ""
    h = 0
    stars = 1
    space = (width - 1) / 2
    s = 0
    while s < space:
        triangle = triangle + " "
        s = s + 1
    triangle = triangle + "*"
    s = 0
    while s < space:
        triangle = triangle + " "
        s = s + 1
    triangle = triangle + "\n"
    s = 0
    # order the rows
    # getting the number of different groups with different number of stars
    num_of_diff_rows = (width - 1) / 2 - 1

    if num_of_diff_rows > 0:
        # getting the number of rows in each group
        rows = int((height - 2) / num_of_diff_rows)
        # check if there is extra rows for the first group
        extra_rows = (height - 2) % num_of_diff_rows
        # initialize the first group of stars with the same number of stars
        rows_for_group1 = rows + extra_rows
        start = 0
        space = space - 1
        while start <  rows_for_group1:
            while s < space:
                triangle = triangle + " "
                s = s + 1
            s = 0
            triangle = triangle + "***"
            while s < space:
                triangle = triangle + " "
                s = s + 1
            s = 0
            triangle = triangle + "\n"
            start = start + 1
    # if there is more then one group
    if num_of_diff_rows > 1:
        stars = 5
        start = 0
        space = space - 1
        num_of_diff_rows = num_of_diff_rows - 1
        num = 0

        while num < num_of_diff_rows:
            while start < rows:
                while s < space:
                    triangle = triangle + " "
                    s = s + 1
                s = 0
                while s < stars:
                    triangle = triangle + "*"
                    s = s + 1
                s = 0
                while s < space:
                    triangle = triangle + " "
                    s = s + 1
                s = 0
                start = start + 1
                triangle = triangle + "\n"
            start = 0
            num = num + 1
            space = space - 1
            stars = stars + 2
    # initialize the last row of the triangle
    s = 0
    while s < width:
        triangle = triangle + "*"
        s = s + 1

    print(triangle)


def handle_triangle_choice(height, width):
    option = input("Press 1 for getting the scope of the triangle\nPress 2 for printing the triangle\n ")
    if option == "1":
        # Calculate the length of the equal sides of the triangle
        side_length = math.sqrt((width / 2) ** 2 + height ** 2)
        scope = side_length * 2 + width
        print("The scope of the triangle is: ", scope)
    elif option == "2":
        if width % 2 == 0 or width > height * 2:
            print("The triangle could not be printed\n")
        else:
            print_triangle(height,width)
    else:
        print("Wrong input")


def handle_rectangle_choice(height, width):
    difference = height - width
    if difference > 5 or difference < -5:
       area = height * width
       print (area)
    else:
        scope = height * 2 + width * 2
        print("The scope of the rectangle is: " , scope)


def get_values():
    flag = False
    while flag == False:
          height = int(input("Enter height equal or greater then 2\n"))
          if height >= 2:
              flag = True
    width = int(input("Enter width\n"))
    return height, width


def main():
    flag = True
    while flag == True:
        option = input("Press 1 for rectangle tower\nPress 2 for a triangle tower\npress 3 to exit\n")
        if option == "1":
            values = get_values()
            handle_rectangle_choice(values[0], values[1])
        elif option == "2":
            values = get_values()
            handle_triangle_choice(values[0], values[1])
        elif option == "3":
            print("Good Bye!")
            flag = False
        else:
            print("Wrong input")


if __name__ == "__main__":
    # Call the main handler function
    main()
