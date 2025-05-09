from database import create_table
from user_manager import (
    add_user,
    view_users,
    search_user,
    delete_user,
    advance_search
)

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Advance Search")      # New option
    print("6. Exit")                # Exit shifted to 6

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-6): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            class_name = input("Enter class (A/B): ")
            add_user(name, email, class_name)

        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)

        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)

        elif choice == '4':
            try:
                user_id = int(input("Enter user ID to delete: "))
            except ValueError:
                print("Invalid ID format.")
                continue
            delete_user(user_id)

        elif choice == '5':
            # Advanced Search by ID and/or name
            id_input = input("Enter user ID to search (leave blank to skip): ")
            try:
                user_id = int(id_input) if id_input else None
            except ValueError:
                print("Invalid ID format.")
                continue
            name = input("Enter name to search (leave blank to skip): ")
            results = advance_search(user_id, name)
            if results:
                for user in results:
                    print(user)
            else:
                print("No matching users found.")

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
