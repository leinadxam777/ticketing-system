import datetime

# Function to calculate the total cost of tickets
def calculate_total_cost(adult_tickets, child_tickets, senior_tickets):
    adult_price = 20
    child_price = 12
    senior_price = 11

    total_cost = (adult_tickets * adult_price) + (child_tickets * child_price) + (senior_tickets * senior_price)
    return total_cost

# Function to print the ticket
def print_ticket(surname, adult_tickets, child_tickets, senior_tickets, parking_pass, date_time):
    ticket_info = f"\n*************** Ticket Details ***************\n" \
                  f"Lead Booker Surname: {surname}\n" \
                  f"Adult Tickets: {adult_tickets}\n" \
                  f"Child Tickets: {child_tickets}\n" \
                  f"Senior Citizen Tickets: {senior_tickets}\n"

    if parking_pass:
        ticket_info += "Parking Pass: Yes\n"
    else:
        ticket_info += "Parking Pass: No\n"

    ticket_info += f"Date: {date_time}\n" \
                   "*********************************************\n"

    print(ticket_info)

    # Save ticket information to a file
    save_to_file(surname, ticket_info)

# Function to save ticket information to a file
def save_to_file(surname, ticket_info):
    filename = f"{surname}_ticket.txt"
    with open(filename, 'w') as file:
        file.write(ticket_info)
    print(f"Ticket information saved to {filename}")

# Welcome message
print("Welcome to Enchanted Kingdom Ticketing System!")

# Display entrance ticket prices
print("\nEntrance Ticket Prices:")
print("Adult: £20\nChild: £12\nSenior Citizen: £11")

# Data validation for the number of tickets
while True:
    try:
        # Ask for the number of tickets
        adult_tickets = int(input("How many adult tickets are required? "))
        child_tickets = int(input("How many child tickets are required? "))
        senior_tickets = int(input("How many senior citizen tickets are required? "))

        if adult_tickets >= 0 and child_tickets >= 0 and senior_tickets >= 0:
            break
        else:
            print("Please enter a valid number of tickets (>= 0).")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Ask for lead booker surname
surname = input("Enter the lead booker surname: ")

# Ask if they require a parking pass
while True:
    parking_input = input("Do you require a parking pass for the car park? (yes/no) ").lower()

    if parking_input == 'yes':
        parking_pass = True
        break
    elif parking_input == 'no':
        parking_pass = False
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Calculate total cost
total_cost = calculate_total_cost(adult_tickets, child_tickets, senior_tickets)

# Display total cost
print(f"\nTotal Cost: £{total_cost}")

# Get the current date and time
current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Print ticket
print_ticket(surname, adult_tickets, child_tickets, senior_tickets, parking_pass, current_date_time)

# Thank the customer for their purchase
print("\nThank you for purchasing tickets from Enchanted Kingdom!")