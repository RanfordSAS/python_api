from flask import Flask, jsonify
import os
import pyodbc

app = Flask(__name__)

# Get environment variables
port = int(os.environ.get('PORT', 5000))
db_server = os.environ.get('DB_SERVER')
db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')

print(f'db_server: {db_server}')

# SQL Server connection string
connection_string = f'DRIVER={{SQL SERVER}};SERVER={db_server};DATABASE={db_name};UID={db_user};PWD={db_password};TRUST-CONNECTION=YES'

# Function to connect to the database
def get_db_connection():
    try:
        conn = pyodbc.connect(connection_string)
        return conn
    except Exception as e:
        return str(e)

@app.route('/ping')
def ping():
    return 'pong'

@app.route('/data')
def get_data():
    conn = get_db_connection()
    if isinstance(conn, str):  # If connection fails, return the error
        return jsonify({'error': conn}), 500

    try:
        cursor = conn.cursor()
        cursor.execute('SELECT TOP 1 * FROM RCC_T_GuiasRemision')  # Replace with your table name
        row = cursor.fetchone()
        if row:
            # return jsonify({'data': row})  # Return the first row as JSON
            #print row as string 

            return jsonify({'data': str(row)}), 200
        else:
            return jsonify({'message': 'No data found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)