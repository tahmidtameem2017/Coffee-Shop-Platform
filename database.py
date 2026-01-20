from db import get_connection

def viewCustomers():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("select * from Customers")
    customers = cursor.fetchall()

    for c in customers:
        print(f"{c["CustomerID"]} | {c['Name']} | {c['Email']}")
    
    cursor.close()
    conn.close()

def viewProducts()->None:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    print("\n👥 Products")
    for p in products:
        print(f"{p["ProductID"]} | {p["Name"]} | ${p["Price"]}")
        cursor.close()
        conn.close()

def viewOrders()->None:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
SELECT o.OrderID , c.Name as Customer , e.Name as Employee , o.OrderDate , o.OrderStatus 
FROM Orders o 
JOIN Customers c on c.CustomerID = o.OrderID 
JOIN Employees e ON o.EmployeeID = e.EmployeeID
ORDER BY o.OrderDate DESC
""")
    orders = cursor.fetchall()

    print("\n📋 Orders")
    for o in orders :
        print(f"Order #{o['OrderID']} | {o['Customer']} | Served by {o['Employee']} | {o['OrderStatus']}")
    cursor.close()
    conn.close()

def addCustomers(name:str , email:str , phone:str)->None:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("""
INSERT INTO Customers (Name , Email , Phone)
VALUES (%s,%s,%s) 
""",(name , email , phone ))
    conn.commit()
    cursor.close()
    conn.close()

def deleteCustomers(customer_id)->None:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
DELETE FROM Customers WHERE CustomerID = %s
""",(customer_id,))
    conn.commit()
    cursor.close()
    conn.close()