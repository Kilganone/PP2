import csv
from connect import get_connection

def insert_from_csv(filename):
    conn = get_connection()
    cur = conn.cursor()

    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            firstname, secondname, phone = row
            cur.execute(
                "INSERT INTO phonebook (firstname, secondname, phonenumber) VALUES (%s, %s, %s)",
                (firstname, secondname, phone)
            )

    conn.commit()
    cur.close()
    conn.close()

def insert_from_console():
    firstname = input("First name: ")
    secondname = input("Second name: ")
    phone = input("Phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO phonebook (firstname, secondname, phonenumber) VALUES (%s, %s, %s)",
        (firstname, secondname, phone)
    )

    conn.commit()
    cur.close()
    conn.close()

def query_contacts():
    conn = get_connection()
    cur = conn.cursor()

    print("1. Show all")
    print("2. Search by name")
    print("3. Search by phone prefix")

    choice = input("Choose: ")

    if choice == "1":
        cur.execute("SELECT * FROM phonebook")

    elif choice == "2":
        name = input("Enter name: ")
        cur.execute(
            "SELECT * FROM phonebook WHERE firstname ILIKE %s",
            ('%' + name + '%',)
        )

    elif choice == "3":
        prefix = input("Enter prefix: ")
        cur.execute(
            "SELECT * FROM phonebook WHERE phonenumber LIKE %s",
            (prefix + '%',)
        )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def update_contact():
    contact_id = input("Enter ID: ")
    new_name = input("New name: ")
    new_phone = input("New phone: ")

    conn = get_connection()
    cur = conn.cursor()

    if new_name:
        cur.execute(
            "UPDATE phonebook SET firstname = %s WHERE id = %s",
            (new_name, contact_id)
        )

    if new_phone:
        cur.execute(
            "UPDATE phonebook SET phonenumber = %s WHERE id = %s",
            (new_phone, contact_id)
        )

    conn.commit()
    cur.close()
    conn.close()

def delete_contact():
    print("1. Delete by name")
    print("2. Delete by phone")

    choice = input("Choose: ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        name = input("Enter name: ")
        cur.execute(
            "DELETE FROM phonebook WHERE firstname = %s",
            (name,)
        )

    elif choice == "2":
        phone = input("Enter phone: ")
        cur.execute(
            "DELETE FROM phonebook WHERE phonenumber = %s",
            (phone,)
        )

    conn.commit()
    cur.close()
    conn.close()

def main():
    while True:
        print("1. Import from CSV")
        print("2. Add contact")
        print("3. Query contacts")
        print("4. Update contact")
        print("5. Delete contact")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_from_csv("contacts.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            query_contacts()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            break

if __name__ == "__main__":
    main()