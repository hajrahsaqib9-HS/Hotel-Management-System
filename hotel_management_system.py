hotel_management_system.py
MAX_ROOMS = 5
MAX_QUEUE = 5
MAX_STACK = 5
# ---------- ROOMS (ARRAY) ----------
rooms = []
for i in range(MAX_ROOMS):
    rooms.append({
        "room_no": i + 1,
        "booked": False,
        "customer": ""
    })
# ---------- STACK (Cancelled Bookings) ----------
cancelled_stack = []
# ---------- QUEUE (Waiting List) ----------
waiting_queue = []
# ---------- FUNCTIONS ----------
def book_room():
    name = input("Enter customer name: ")
    for room in rooms:
        if not room["booked"]:
            room["booked"] = True
            room["customer"] = name
            print(f"Room {room['room_no']} booked successfully!")
            return
    print("All rooms are full! Adding to waiting list...")
    add_to_waiting_list(name)
def show_rooms():
    print("\nRoom Status:")
    for room in rooms:
        if room["booked"]:
            print(f"Room {room['room_no']} : Booked by {room['customer']}")
        else:
            print(f"Room {room['room_no']} : Available")
def cancel_booking():
    room_no = int(input("Enter room number to cancel: "))

    if room_no < 1 or room_no > MAX_ROOMS:
        print("Invalid room number!")
        return
    room = rooms[room_no - 1]
    if room["booked"]:
        if len(cancelled_stack) < MAX_STACK:
            cancelled_stack.append(room["customer"])   # STACK PUSH
        print(f"Booking cancelled for {room['customer']}")
        room["booked"] = False
        room["customer"] = ""
        # Assign to waiting customer (QUEUE)
        if waiting_queue:
            room["customer"] = waiting_queue.pop(0)   # QUEUE DEQUEUE
            room["booked"] = True
            print(f"Room assigned to waiting customer: {room['customer']}")
    else:
        print("Room is already empty!")
def add_to_waiting_list(name):
    if len(waiting_queue) < MAX_QUEUE:
        waiting_queue.append(name)   # QUEUE ENQUEUE
        print("Added to waiting list.")
    else:
        print("Waiting list is full!")
def show_waiting_list():
    if not waiting_queue:
        print("Waiting list is empty.")
    else:
        print("Waiting List:")
        for name in waiting_queue:
            print(name)
def show_cancelled_bookings():
    if not cancelled_stack:
        print("No cancelled bookings.")
    else:
        print("Cancelled Bookings (Stack):")
        for name in reversed(cancelled_stack):
            print(name)
# ---------- MAIN MENU ----------
while True:
    print("\n===== HOTEL MANAGEMENT SYSTEM =====")
    print("1. Book Room")
    print("2. Show Rooms")
    print("3. Cancel Booking")
    print("4. Show Waiting List")
    print("5. Show Cancelled Bookings")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        book_room()
    elif choice == "2":
        show_rooms()
    elif choice == "3":
        cancel_booking()
    elif choice == "4":
        show_waiting_list()
    elif choice == "5":
        show_cancelled_bookings()
    elif choice == "6":
        print("Exiting system...")
        break
    else:
        print("Invalid choice!")
Initial commit - Hotel Management System source code
