import mysql.connector
from mysql.connector import Error

def connect_to_db():
    try:
        # Note: Fixed hostname from 'hexahost' to 'hexhost' based on your website URL
        mydb = mysql.connector.connect(
            host="mohamed.hexhost.online",
            user="mohamedm_mohamedelwan",
            password="3030@Salma",
            database="mohamedm_nouralislam",
            port=3306,
            connect_timeout=10 # Added timeout
        )

        if mydb.is_connected():
            print("Successfully connected to the database!")
            
            cursor = mydb.cursor()
            
            # Fetch and show rows from 'firsttable'
            try:
                print("\nFetching data from 'firsttable'...")
                cursor.execute("SELECT * FROM firsttable")
                
                rows = cursor.fetchall()
                
                if not rows:
                    print("The table 'firsttable' is empty.")
                else:
                    # Print column names
                    column_names = [i[0] for i in cursor.description]
                    print(f"Columns: {column_names}")
                    print("-" * 30)
                    
                    for row in rows:
                        print(row)
                        
            except Error as table_err:
                print(f"Error accessing table: {table_err}")
                if table_err.errno == 1146:
                    print("TIP: The table 'firsttable' doesn't seem to exist in this database.")
            
            cursor.close()
            mydb.close()
            print("\nConnection closed.")
            
    except Error as e:
        # Error 1130 is the "Host not allowed" error common in MariaDB/MySQL whitelisting
        if e.errno == 1130:
            print("\n[REMOTE ACCESS DENIED] MariaDB Error 1130")
            print(f"Details: {e.msg}")
            print("TO FIX: Log into your cPanel, find 'Remote MySQL', and add your IP to the whitelist.")
        else:
            print(f"Error while connecting to MariaDB: {e}")
        
        # Specific advice for common hosting errors
        error_str = str(e)
        if "110" in error_str or "10060" in error_str:
            print("\nTIP: Connection Timed Out.")
            print("1. Ensure your IP address is allowed in cPanel -> 'Remote MySQL'.")
            print("2. Check if your firewall or ISP blocks port 3306.")
        elif "1045" in error_str:
            print("\nTIP: Access Denied. Check your username and password.")
        elif "2005" in error_str:
            print("\nTIP: Unknown MariaDB/MySQL server host. Double-check the hostname.")

if __name__ == "__main__":
    connect_to_db()
