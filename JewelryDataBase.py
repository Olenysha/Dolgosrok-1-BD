
import sqlite3

conn = sqlite3.connect("JewelryStore.db")
cur = conn.cursor()

# there is sample == proba
cur.execute("""
    CREATE TABLE IF NOT EXISTS materials (
    id INTEGER PRIMARY KEY,
    name TEXT,
    sample TEXT
    )""")
conn.commit()

cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    id_material INTEGER,
    cost INTEGER
    )""")
conn.commit()

cur.execute("""
    CREATE TABLE IF NOT EXISTS pr_or(
    id INTEGER,
    id_order INTEGER,
    id_product INTEGER,
    count INTEGER
    )""")
conn.commit()

cur.execute("""
    CREATE TABLE IF NOT EXISTS customers(
    id INTEGER PRIMARY KEY,
    FIO TEXT,
    INN INTEGER
    )""")
conn.commit()

cur.execute("""
    CREATE TABLE IF NOT EXISTS orders(
    id INTEGER,
    date DATE,
    id_costumer INTEGER
    )""")
conn.commit()

cur.execute("""
    CREATE TABLE IF NOT EXISTS basket(
    id INTEGER,
    id_costumer INTEGER,
    id_product INTEGER
    )""")
conn.commit()

def insert_materials():
    primary_key = 1
    materials_id = 1
    materials_name = ["","gold","silver","platinum","palladium","steel"]
    gold_sample = [None,375, 500, 538, 585, 750, 958, 999]
    silver_sample = [None,800, 830, 875, 925, 960, 999]
    platinum_sample = [None,850, 900, 950]
    palladium_sample = [None,500,850]
    steel_sample = [750]
    for materials_id in range (1,6):
        if materials_id == 1:
            for num in range (1,8):
                cur.execute("INSERT INTO materials VALUES (?,?,?)", (primary_key,materials_name[materials_id],gold_sample[num]))
                conn.commit()
                primary_key += 1
        elif materials_id == 2:
            for num in range(1, 7):
                cur.execute("INSERT INTO materials VALUES (?,?,?)",
                            (primary_key, materials_name[materials_id], silver_sample[num]))
                conn.commit()
                primary_key += 1
        elif materials_id == 3:
            for num in range(1, 4):
                cur.execute("INSERT INTO materials VALUES (?,?,?)",
                            (primary_key, materials_name[materials_id], platinum_sample[num]))
                conn.commit()
                primary_key += 1
        elif materials_id == 4:
            for num in range(1, 3):
                cur.execute("INSERT INTO materials VALUES (?,?,?)",
                            (primary_key, materials_name[materials_id], palladium_sample[num]))
                conn.commit()
                primary_key += 1
        else:
            cur.execute("INSERT INTO materials VALUES (?,?,?)",
                        (primary_key, materials_name[materials_id], steel_sample[0]))
            conn.commit()
            primary_key += 1

def insert_customers():

    for primary_key in range (1,21,1):
        cur.execute("INSERT INTO customers VALUES (?,?,?)",
                    (primary_key, FIO[primary_key], INN[primary_key]))
        conn.commit()

def insert_products():
    for primary_key in range (1,77):
        cur.execute("INSERT INTO products VALUES (?,?,?,?)",
                    (primary_key, names[primary_key],(primary_key%19)+1,cost[primary_key%6] ))
        conn.commit()
def insert_basket():
    id_customer = 1
    id = 1
    for i in range (1,60):
        for j in range (0,3):
            cur.execute("INSERT INTO basket VALUES (?,?,?)",
                (id, id_customer, names[i+j]))
            conn.commit()
            id += 1
        id_customer += 1

def pr_or():
    for i in range (1,31):
        cur.execute("INSERT INTO pr_or VALUES (?,?,?,?)",
                    (i, i, i+30,count[i%5]))
        conn.commit()

def insert_orders():
    for i in range(1,31):
        cur.execute("INSERT INTO orders VALUES (?,?,?)",
                    (i, date[len(date)%i], 20%i+1))
        conn.commit()

if __name__ == '__main__':
    FIO = ["", "Курочкин Никита Дмитриевич", "Иванов Иван Иванович", "Смирнов Алексей Сергеевич",
           "Петрова Екатерина Андреевна",
           "Соколов Максим Александрович", "Алексеева Ольга Владимировна", "Кузнецов Даниил Игоревич",
           "Федорова Анастасия Павловна",
           "Морозов Артем Валерьевич", "Никитина Юлия Владимировна", "Лебедев Денис Сергеевич",
           "Кузьмин Александр Алексеевич",
           "Степанова Екатерина Александровна", "Новиков Михаил Викторович", "Орлова Анастасия Ивановна",
           "Андреев Дмитрий Владимирович",
           "Григорьева Мария Петровна", "Белов Николай Егорович", "Кудряшова Алина Сергеевна",
           "Тимофеев Павел Андреевич"]
    INN = ["", "123456789012", "234567890123", "345678901234", "456789012345", "567890123456", "678901234567",
           "789012345678", "890123456789", "901234567890", "212345678901", "123456789012", "234567890123",
           "345678901234",
           "456789012345", "567890123456", "678901234567", "789012345678", "890123456789", "901234567890",
           "112345678901"]
    names = ["", "Кольцо 'Nature's Attendants'", "Кольцо 'Illusory Orb'", "Кольцо 'Laguna Blade'",
             "Кольцо 'Static Link'", "Кольцо 'Avalanche'", "Кольцо 'Enchant'", "Кольцо 'Static Storm'",
             "Кольцо 'Atrophy Aura'", "Кольцо 'Conjure Image'", "Кольцо 'Teleportation'", "Кольцо 'Gust'",
             "Кольцо 'Permanent Invisibility'", "Кольцо 'Echo Slam'", "Кольцо 'Bloodrage'", "Кольцо 'Hawk'",
             "Кольцо 'Press the Attack'", "Сережки 'Poison Touch'", "Сережки 'Stifling Dagger'",
             "Сережки 'Sticky Napalm'", "Сережки 'Time Walk'", "Сережки 'Toss'", "Сережки 'Ravage'",
             "Сережки 'Viper Strike'", "Сережки 'Chaos Bolt'", "Сережки 'Ghost Walk'", "Сережки 'Blink Strike'",
             "Сережки 'Black Hole'", "Сережки 'Ethereal Blade'", "Сережки 'Stone Gaze'", "Сережки 'Chronosphere'",
             "Сережки 'Nether Swap'", "Сережки 'Nether Strike'", "Сережки 'Mystic Flare'", "Сережки 'Mana Void'",
             "Сережки 'Duel'", "Сережки 'Dismember'", "Подвеска 'Poison Touch'", "Подвеска 'Stifling Dagger'",
             "Подвеска 'Sticky Napalm'", "Подвеска 'Time Walk'", "Подвеска 'Toss'", "Подвеска 'Ravage'",
             "Подвеска 'Viper Strike'", "Подвеска 'Chaos Bolt'", "Подвеска 'Ghost Walk'", "Подвеска 'Blink Strike'",
             "Подвеска 'Black Hole'", "Подвеска 'Ethereal Blade'", "Подвеска 'Stone Gaze'", "Подвеска 'Chronosphere'",
             "Подвеска 'Nether Swap'", "Подвеска 'Nether Strike'", "Подвеска 'Mystic Flare'", "Подвеска 'Mana Void'",
             "Подвеска 'Duel'", "Подвеска 'Dismember'", "Кулон 'Poison Touch'", "Кулон 'Stifling Dagger'",
             "Кулон 'Sticky Napalm'", "Кулон 'Time Walk'", "Кулон 'Toss'", "Кулон 'Ravage'", "Кулон 'Viper Strike'",
             "Кулон 'Chaos Bolt'", "Кулон 'Ghost Walk'", "Кулон 'Blink Strike'", "Кулон 'Black Hole'",
             "Кулон 'Ethereal Blade'", "Кулон 'Stone Gaze'", "Кулон 'Chronosphere'", "Кулон 'Nether Swap'",
             "Кулон 'Nether Strike'", "Кулон 'Mystic Flare'", "Кулон 'Mana Void'", "Кулон 'Duel'", "Кулон 'Dismember'"]
    cost = [3000, 4000, 5000, 6000, 8000, 1000]
    date = ["16.05.23", "17.05.23", "18.05.23", "19.05.23", "20.05.23", "21.05.23", "22.05.23", "23.05.23",
            "24.05.23", "25.05.23", "26.05.23", "27.05.23", "28.05.23", "29.05.23", "30.05.23", "31.05.23",
            "01.06.23", "02.06.23", "03.06.23", "04.06.23", "05.06.23", "06.06.23", "07.06.23", "08.06.23",
            "09.06.23", "10.06.23", "11.06.23", "12.06.23", "13.06.23", "14.06.23", "15.06.23", "16.06.23",
            "17.06.23", "18.06.23", "19.06.23", "20.06.23", "21.06.23", "22.06.23", "23.06.23", "24.06.23",
            "25.06.23", "26.06.23", "27.06.23", "28.06.23", "29.06.23", "30.06.23", "01.07.23", "02.07.23",
            "03.07.23", "04.07.23", "05.07.23", "06.07.23", "07.07.23", "08.07.23", "09.07.23", "10.07.23",
            "11.07.23", "12.07.23", "13.07.23", "14.07.23", "15.07.23", "16.07.23", "17.07.23", "18.07.23",
            "19.07.23", "20.07.23", "21.07.23", "22.07.23", "23.07.23", "24.07.23", "25.07.23", "26.07.23",
            "27.07.23", "28.07.23", "29.07.23", "30.07.23", "31.07.23", "01.08.23", "02.08.23", "03.08.23",
            "04.08.23", "05.08.23", "06.08.23", "07.08.23", "08.08.23", "09.08.23", "10.08.23", "11.08.23",
            "12.08.23", "13.08.23", "14.08.23", "15.08.23", "16.08.23", "17.08.23", "18.08.23", "19.08.23",
            "20.08.23", "21.08.23", "22.08.23", "23.08.23", "24.08.23", "25.08.23", "26.08.23", "27.08.23",
            "28.08.23", "29.08.23", "30.08.23", "31.08.23", "01.09.23", "02.09.23", "03.09.23", "04.09.23",
            "05.09.23", "06.09.23", "07.09.23", "08.09.23"]
    count = [1,2,3,4,5]

    insert_materials()
    insert_customers()
    insert_products()
    insert_basket()
    pr_or()
    insert_orders()

