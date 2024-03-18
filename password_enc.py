"""
Author : Jaehyeok Jang (UF ID : 98532294), jaehyeok.jang@ufl.edu
Date   : 2024/03/18
Assignment : Lab 6 - Version control

Description
1. If user select menu 1, get user input {var_user_password}, encode it and display the following message:
    "Your password has been encoded and stored!"
2. If user select menu 2, decode encoded password and display the following message:
    "The encoded password is {}, and the original password is {}."
"""


def encode(org_password):  # Encryption : Add 3 for each digit and concatenate every string
    str_encoded_pass = ""

    for i in org_password:
        var_encode_temp = int(i) + 3  # Add 3 for each digit
        str_encoded_pass += str(var_encode_temp)[-1]  # Concatenate every string

    return str_encoded_pass


def main():

    while True:

        # Get the user input for menu selection
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        var_menu_sel = int(input("Please enter an option: "))

        if var_menu_sel == 1:
            var_user_password = input("Please enter your password to encode: ")
            var_encoded_pass = encode(var_user_password)
            print("Your password has been encoded and stored!")
            print()
        elif var_menu_sel == 2:
            pass
        elif var_menu_sel == 3:
            break

    # 1st while end : var_decode_continue


if __name__ == '__main__':
    main()

# main end
