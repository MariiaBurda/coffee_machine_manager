import mysql.connector

from app.operations.config import config_for_db


def get_db_tables(db_config):
    db = mysql.connector.Connect(**db_config)
    cursor = db.cursor()

    # show all tables from connected db
    sql = "SHOW TABLES"
    cursor.execute(sql)
    rows = cursor.fetchall()

    cursor.close()
    db.close()

    return rows


def get_all_receipts(db_config):
    db = mysql.connector.Connect(**db_config)
    cursor = db.cursor()

    sql = "SELECT id, name " \
          "FROM receipt"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows


if __name__ == '__main__':
    list_of_db_tables = get_db_tables(config_for_db)
    print(list_of_db_tables)

    receipts_list = get_all_receipts(config_for_db)
    print(receipts_list)