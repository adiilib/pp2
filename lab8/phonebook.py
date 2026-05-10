import psycopg2
from connect import get_conn


def setup():
    conn = get_conn()
    cur = conn.cursor()
    for fname in ("functions.sql", "procedures.sql"):
        with open(fname, encoding="utf-8") as f:
            cur.execute(f.read())
    conn.commit()
    cur.close()
    conn.close()
    print("Functions and procedures created.")


def search_contacts():
    pattern = input("Enter search pattern: ")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(f"  {row[0]}. {row[1]} — {row[2]}")
    else:
        print("  No results.")
    cur.close()
    conn.close()


def upsert_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()
    print("Done.")
    cur.close()
    conn.close()


def insert_many():
    print("Enter contacts (name,phone) one per line, empty line to finish:")
    names = []
    phones = []
    while True:
        line = input("  > ").strip()
        if not line:
            break
        parts = line.split(",", 1)
        if len(parts) != 2:
            print("  Bad format, skip.")
            continue
        names.append(parts[0].strip())
        phones.append(parts[1].strip())

    if not names:
        print("Nothing to insert.")
        return

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM insert_many_contacts(%s, %s)", (names, phones))
    invalid = cur.fetchall()
    conn.commit()
    if invalid:
        print("Invalid entries (bad phone):")
        for row in invalid:
            print(f"  {row[0]} — {row[1]}")
    else:
        print("All contacts inserted successfully.")
    cur.close()
    conn.close()


def view_paginated():
    page = 0
    limit = 5
    conn = get_conn()
    while True:
        cur = conn.cursor()
        cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, page * limit))
        rows = cur.fetchall()
        cur.close()
        print(f"\n--- Page {page + 1} ---")
        if rows:
            for row in rows:
                print(f"  {row[0]}. {row[1]} — {row[2]}")
        else:
            print("  No contacts on this page.")
        cmd = input("[n] Next  [p] Prev  [q] Quit: ").strip().lower()
        if cmd == "n":
            page += 1
        elif cmd == "p":
            page = max(0, page - 1)
        elif cmd == "q":
            break
    conn.close()


def delete_contact():
    print("Delete by: [1] Name  [2] Phone")
    ch = input("Choice: ").strip()
    conn = get_conn()
    cur = conn.cursor()
    if ch == "1":
        name = input("Name: ")
        cur.execute("CALL delete_contact(p_name => %s)", (name,))
    elif ch == "2":
        phone = input("Phone: ")
        cur.execute("CALL delete_contact(p_phone => %s)", (phone,))
    else:
        print("Invalid choice.")
        cur.close()
        conn.close()
        return
    conn.commit()
    print("Deleted.")
    cur.close()
    conn.close()


def main():
    setup()
    while True:
        print("\n1. Search contacts")
        print("2. Add / update contact")
        print("3. Bulk insert from list")
        print("4. View all (paginated)")
        print("5. Delete contact")
        print("6. Exit")
        ch = input("Choice: ").strip()
        if ch == "1":
            search_contacts()
        elif ch == "2":
            upsert_contact()
        elif ch == "3":
            insert_many()
        elif ch == "4":
            view_paginated()
        elif ch == "5":
            delete_contact()
        elif ch == "6":
            break


if __name__ == "__main__":
    main()
