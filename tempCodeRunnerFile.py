def view_only_Tanker_ID():
    try:
        c.execute("SELECT Tanker_ID FROM Tanker")
        data = c.fetchall()
        print(data)
        return data
    except mysql.connector.Error as err:
        logging.error("Error fetching tanker IDs: %s", err)
        return None

view_only_Tanker_ID()