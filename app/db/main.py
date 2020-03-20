import mysql.connector

from config import config


def main(db_config):
    output = []
    db = mysql.connector.Connect(**db_config)
    cursor = db.cursor()

    # Show all tables from connected db
    sql = "SHOW TABLES"
    cursor.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        output.append(repr(row))

    cursor.close()
    db.close()
    return output


if __name__ == '__main__':
    out = main(config)
    print('\n'.join(out))
