import mysql.connector

# Database connection details
db_config = {
    'host': 'puneet-mysql-server.mysql.database.azure.com',
    'user': 'puneetadmin',
    'password': 'Azure@1234',
    'database': 'companydb',
    'port': 3306
}

# Function to execute SQL script
def execute_sql_script(script_path):
    try:
        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Open and read the SQL script
        with open(script_path, 'r') as file:
            sql_commands = file.read().split(';')

        # Execute each SQL command
        for command in sql_commands:
            if command.strip():
                try:
                    cursor.execute(command)
                except mysql.connector.Error as err:
                    # Ignore duplicate column errors
                    if err.errno == 1060:
                        print("⚠️ Column already exists. Skipping...")
                    else:
                        raise

        # Commit changes
        connection.commit()
        print("✅ SQL script executed successfully!")

    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")

    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Run the script
execute_sql_script('schema_changes.sql')

