# Coffee_machine_manager
Simulation of a remote coffee machine management by python-socketio. Used Python 3.7.5
### Coffee_machine_manager_db_diagram


![coffee_machine_manager_db_diagram](https://user-images.githubusercontent.com/56352901/76962995-f0ee9f80-6928-11ea-9b0b-80deabacba98.png)

### To set up and use the database you need:
1. Install MySQL-server (necessarily) and MySQL Workbench (optionally)
2. Use coffee_machine_manager/database/coffee_machine_db_init.sql to create database and tables
3. Use coffee_machine_manager/database/coffee_machine_db_seed.sql to populate tables
4. Create coffee_machine_manager/app/db/config.py file and fill with your information:
config_for_db = {
    'host': 'your_host_name',
    'port': your_port_name,
    'database': 'coffee_machine_manager',
    'user': 'your_user_name',
    'password': 'your_password',
    'charset': 'utf8',
    'use_unicode': True,
    'get_warnings': True,
} 
5. Install mysql.connector
6. Use coffee_machine_manager/app/db/main.py  to test db connect
