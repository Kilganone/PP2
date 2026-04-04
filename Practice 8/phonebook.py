from connect import get_connection

def search_contacts():
    pattern = input("Enter search pattern (name/surname/phone): ").strip()
    if not pattern:
        return
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
        results = cur.fetchall()
        if not results:
            print("No contacts found.")
        else:
            print(f"Found {len(results)} record(s):")
            for row in results:
                print(row)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()

def paginated_view():
    try:
        limit = int(input("Contacts per page (default 5): ").strip() or 5)
        page = int(input("Page number (default 1): ").strip() or 1)
    except ValueError:
        limit, page = 5, 1
    offset = (page - 1) * limit

    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
        results = cur.fetchall()
        if not results:
            print("No data for this page.")
        else:
            print(f"--- Page {page} (size: {limit}) ---")
            for row in results:
                print(row)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()

def upsert_contact():
    fn = input("First name: ").strip()
    sn = input("Second name: ").strip()
    phone = input("Phone: ").strip()
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("CALL upsert_contact(%s, %s, %s)", (fn, sn, phone))
        conn.commit()
        print("Updated or inserted.")
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()

def bulk_insert():
    print("Enter contacts: First,Second,Phone (empty line to finish)")
    contacts = []
    while True:
        line = input().strip()
        if not line:
            break
        contacts.append(line)

    if not contacts:
        print("No contacts entered.")
        return

    conn = get_connection()
    cur = conn.cursor()
    try:
        conn.notices = []
        cur.execute("CALL insert_many_contacts(%s)", (contacts,))
        conn.commit()
        if conn.notices:
            print("Validation results:")
            for notice in conn.notices:
                print(notice.strip())
        else:
            print("All contacts inserted successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()

def delete_contact():
    value = input("Enter name or phone to delete: ").strip()
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("CALL delete_contact(%s)", (value,))
        conn.commit()
        print(f"Records matching '{value}' deleted.")
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()

def main():
    while True:
        print("\n=== PhoneBook v2 (Functions & Procedures) ===")
        print("1. Search by pattern")
        print("2. Paginated view")
        print("3. Upsert contact")
        print("4. Bulk insert with validation")
        print("5. Delete contact")
        print("0. Exit")

        choice = input("Choose: ").strip()
        if choice == "1":
            search_contacts()
        elif choice == "2":
            paginated_view()
        elif choice == "3":
            upsert_contact()
        elif choice == "4":
            bulk_insert()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()