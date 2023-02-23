print("AutoLeagueLogger Data Collector")
print('\n')
while True:
    amount_acc = input("Enter amount of ur accounts: ")
    print('\n')
    if not amount_acc.isdigit():
        print("Enter a number!")
    else:
        break

with open("Data.txt", "w") as file:
    if int(amount_acc) > 0:
        for x in range(int(amount_acc)):
            username_data = input("Enter Your Login: ".format(x + int(amount_acc)))
            pass_data = input("Enter Your Password: ".format(x + int(amount_acc)))
            print('\n')
            file.write("Account nr {}: login = %{}, password = /{}\n".format(x + 1, username_data, pass_data))
    else:
        print("Enter number above 0 lol")
