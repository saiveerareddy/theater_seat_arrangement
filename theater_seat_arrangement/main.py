# Dictionary to store user data
user_data = {}

# Dictionary to store seat data for each screen
screens = {
    "Screen1": {"rows": 17, "columns": 22, "seats": {}},
    "Screen2": {"rows": 17, "columns": 22, "seats": {}},
    "Screen3": {"rows": 17, "columns": 22, "seats": {}}
}

# Seat comfort levels
comfort_levels = ["Standard", "Premium", "VIP"]


# Function to handle user login
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in user_data and user_data[username]["password"] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password.")
        return None


# Function to handle user account creation
def create_account():
    username = input("Enter a new username: ")
    if username in user_data:
        print("Username already exists. Please choose another one.")
        return

    password = input("Enter a password: ")
    user_data[username] = {"password": password}
    print("Account created successfully!")

# Function to book seats
def book_seats(screen):
    print('''
            Rs.200 Recliner_____________________________________________________________________________________
            A | A1 A2 A3 A4 A5                                                                    A6 A7 A8 A9   |

            Rs.150 Platinum______________________________________________________________________________________
            B | B1 B2 B3 B4               B5                                                    B6 B7 B8 B9     |
            C | C1 C2 C3 C4               C5 C6 C7 C8 C9 C10 C11 C12 C13 C14                    C15 C16 C17 C18 |
            D | D1 D2 D3 D4               D5 D6 D7 D8 D9 D10 D11 D12 D13 D14                    D15 D16 D17 D18 |
            E | E1 E2 E3 E4               E5 E6 E7 E8 E9 E10 E11 E12 E13 E14                    E15 E16 E17 E18 |
            F | F1 F2 F3 F4               F5 F6 F7 F8 F9 F10 F11 F12 F13 F14                    F15 F16 F17 F18 |
            G | G1 G2 G3 G4               G5 G6 G7 G8 G9 G10 G11 G12 G13 G14 G15 G16            G17 G18 G19 G20 |
            H | H1 H2 H3 H4               H5 H6 H7 H8 H9 H10 H11 H12 H13 H14 H15 H16            H17 H18 H19 H20 |
            I | I1 I2 I3 I4               I5 I6 I7 I8 I9 I10 I11 I12 I13 I14 I15 I16            I17 I18 I19 I20 |
            Rs.150 Gold__________________________________________________________________________________________
            J | J1 J2 J3 J4                J5 J6 J7 J8 J9 J10 J11 J12 J13 J14 J15 J16           J17 J18 J19 J20 |
            K | K1 K2 K3 K4                K5 K6 K7 K8 K9 K10 K11 K12 K13 K14 K15 K16           K17 K18 K19 K20 |
            L | L1 L2 L3 L4                L5 L6 L7 L8 L9 L10 L11 L12 L13 L14 L15 L16           L17 L18 L19 L20 |
            M | M1 M2 M3 M4                M5 M6 M7 M8 M9 M10 M11 M12 M13 M14 M15 M16           M17 M18 M19 M20 |
            N | N1 N2 N3 N4                N5 N6 N7 N8 N9 N10 N11 N12 N13 N14 N15 N16           N17 N18 N19 N20 |
            O | O1 O2 O3 O4                O5 O6 O7 O8 O9 O10 O11 O12 O13 O14 O15 O16           O17 O18 O19 O20 |
            P | P1 P2 P3 P4                P5 P6 P7 P8 P9 P10 P11 P12 P13 P14 P15 P16           P17 P18 P19 P20 |
            Q | Q1 Q2 Q3 Q4                Q5 Q6 Q7 Q8 Q9 Q10 Q11 Q12 Q13 Q14 Q15 Q16           Q17 Q18 Q19 Q20 |

                               [=======================================================]
                                                          SCREEN
            ''')
    
    row = input("Enter row (A to Q): ")
    column = int(input("Enter seat number (1 to 22): "))

    # Convert row to uppercase for consistency
    row = row.upper()

    if row in [chr(i) for i in range(65, 65 + screens[screen]["rows"])] and 1 <= column <= 22:
        seat = (row, column)
        if seat not in screens[screen]["seats"]:
            comfort_level = input("Select comfort level (Standard/Premium/VIP): ")
            if comfort_level in comfort_levels:
                screens[screen]["seats"][seat] = {"comfort_level": comfort_level, "status": "Booked"}
                print("Seat booked successfully!")
            else:
                print("Invalid comfort level.")
        else:
            print("Seat already booked.")
    else:
        print("Invalid seat.")


# Function to search for booked seats
def search_seats(screen):
    booked_seats = [seat for seat, info in screens[screen]["seats"].items() if info["status"] == "Booked"]
    if booked_seats:
        print("Booked seats:")
        for seat in booked_seats:
            print(f"Row: {seat[0]}, Column: {seat[1]}")
    else:
        print("No seats have been booked yet.")


# Function to handle updating seat information
def update_seat(screen):
    row = input("Enter row (A to Q): ")
    column = int(input("Enter seat number (1 to 22): "))

    # Convert row to uppercase for consistency
    row = row.upper()

    if row in [chr(i) for i in range(65, 65 + screens[screen]["rows"])] and 1 <= column <= 22:
        seat = (row, column)
        if seat in screens[screen]["seats"]:
            if screens[screen]["seats"][seat]["status"] == "Booked":
                new_comfort_level = input("Enter new comfort level (Standard/Premium/VIP): ")
                if new_comfort_level in comfort_levels:
                    screens[screen]["seats"][seat]["comfort_level"] = new_comfort_level
                    print("Seat information updated successfully!")
                else:
                    print("Invalid comfort level.")
            else:
                print("Seat is not booked.")
        else:
            print("Seat not found.")
    else:
        print("Invalid seat.")


# Function to handle deleting user booked seats
def delete_seat(screen):
    row = input("Enter row (A to Q): ")
    column = int(input("Enter seat number (1 to 22): "))

    # Convert row to uppercase for consistency
    row = row.upper()

    if row in [chr(i) for i in range(65, 65 + screens[screen]["rows"])] and 1 <= column <= 22:
        seat = (row, column)
        if seat in screens[screen]["seats"]:
            if screens[screen]["seats"][seat]["status"] == "Booked":
                del screens[screen]["seats"][seat]
                print("Seat deleted successfully!")
            else:
                print("Seat is not booked.")
        else:
            print("Seat not found.")
    else:
        print("Invalid seat.")



# Main function
def main():
    while True:
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = login()
            if username:
                select_screen()
        elif choice == "2":
            create_account()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to handle CRUD operations for seats
def manage_seats(screen):
    while True:
        print("1. Book Seats")
        print("2. Search Seats")
        print("3. Update Seat")
        print("4. Delete Seat")
        print("5. Back")
        choice = input("Enter your choice: ")

        if choice == "1":
            book_seats(screen)
        elif choice == "2":
            search_seats(screen)
        elif choice == "3":
            update_seat(screen)
        elif choice == "4":
            delete_seat(screen)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

# Function to select screen after login
def select_screen():
    while True:
        print("1. Screen1")
        print("2. Screen2")
        print("3. Screen3")
        print("4. Back")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Screen1 selected.")
            manage_seats("Screen1")
        elif choice == "2":
            print("Screen2 selected.")
            manage_seats("Screen2")
        elif choice == "3":
            print("Screen3 selected.")
            manage_seats("Screen3")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

# Main function
if __name__ == "__main__":
    main()


