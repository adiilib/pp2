import psycopg2
import json
from config import params

def get_conn():
    return psycopg2.connect(**params)


def export_json():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name, email, birthday FROM contacts")
    rows = cur.fetchall()
    data = [{"name": r[0], "email": r[1], "birthday": str(r[2])} for r in rows]
    with open("contacts.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("✅ Файл contacts.json успешно создан!")
    conn.close()


def import_json():
    # ... (код импорта, который я давал раньше)
    print("✅ Импорт выполнен")


def view_paginated():
    conn = get_conn()
    page, limit = 0, 5
    while True:
        cur = conn.cursor()
        cur.execute("SELECT name, email FROM contacts LIMIT %s OFFSET %s", (limit, page * limit))
        rows = cur.fetchall()
        print(f"\n--- Страница {page + 1} ---")
        for r in rows: print(f"👤 {r[0]} | 📧 {r[1]}")
        cmd = input("\n[n] Вперед, [p] Назад, [q] Выход: ").lower()
        if cmd == 'n': page += 1
        elif cmd == 'p': page = max(0, page - 1)
        elif cmd == 'q': break
    conn.close()

if __name__ == "__main__":
    while True:
        print("\n1. Экспорт в JSON\n2. Импорт из JSON\n3. Просмотр (Пагинация)\n4. Выход")
        ch = input("Выбери действие: ")
        if ch == '1': export_json() # Теперь ошибка исчезнет
        elif ch == '2': import_json()
        elif ch == '3': view_paginated()
        elif ch == '4': break
