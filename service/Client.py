import cx_Oracle

def getClients():
    clients = []

    # Connect as user "hr" with password "welcome" to the "oraclepdb" service running on this computer.
    connection = cx_Oracle.connect("db1", "db1", "morassutti/xe")

    cursor = connection.cursor()
    cursor.execute("SELECT id, name FROM client")
    for id, name in cursor:
        print("Values:", id, name)
        client = {}
        client['id'] = id
        client['name'] = name

        clients.append(client)


    return clients