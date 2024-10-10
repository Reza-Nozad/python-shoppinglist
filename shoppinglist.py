import sqlite3
conn=sqlite3.connect('shopping.db')
cursor=conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS groceries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(32) NOT NULL,
    amount VARCHAR(32) NOT NULL, 
    price INTEGER NOT NULL
    );
''')

def add_groceries(name, amount, price):
    cursor.execute('''
    INSERT INTO groceries (name, amount, price) VALUES (?, ?, ?)
    ''', (name, amount, price))
    conn.commit()
    print(f"{name} wurde hinzugefügt")
    
def show_shoppinglist():
    cursor.execute('SELECT id, name FROM groceries')
    groceries = cursor.fetchall()
    for name in groceries:
     print(name)
     
def update_groceries(id, name, amount, price):
    cursor.execute('''
    UPDATE Students SET name = ?, amount = ?, price = ?
    WHERE id = ?               
    ''',(name, amount, price, id))
    conn.commit()
    print(f"updated Shoppinglist with id {id}")
    
def delete_groceries(id):
    cursor.execute('''
    DELETE FROM groceries WHERE id = ?                
    ''',(id,))
    conn.commit()
    print(f"Groceries has been deleted with id {id}")
    
    
def main():
    while True:
        print("\n----- Shoppingliste -----")
        print("1. Groceries  hinzufügen")
        print("2. Shoppingliste anzeigen")
        print("3. Groceries aktualisieren")
        print("4. groceries löschen")       
        print("5. Programm beenden")

        choice = input("Bitte wähle eine Option (1,2,3,4 oder 5): ")

        if choice == "1":
            print("Bitte gib die Daten des neuen Grocerie ein: ")
            name = input("name: ")
            amount = input("amount: ")
            price = input("price: ")
            add_groceries(name, amount, price)
        elif choice == "2":
            show_shoppinglist()
        elif choice == "3":
            print("Bitte gib die aktualisierten Daten mit id ein: ")
            id = input("id: ")
            name = input("name: ")
            amount = input("amount: ")
            price = input("price: ")
            update_groceries(id, name, amount, price)
        elif choice == "4":
            print("Bitte gib die ID des zu löschenden Groceries ein: ")
            id = input("id: ")
            delete_groceries(id)
        elif choice == "5":
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe! Bitte wähle 1,2,3,4 oder 5")

if __name__ == "__main__":
    main()





# shoppinglist=[]

# def add_item():
#     item = input("Bitte gib den Artikel ein, der zur Einkaufsliste hinzugefügt werden soll: ")
    
#     if item:
#       print ("Ihre Artikel : ", item, " wurde der EinkaufListe hinzugefügt")
#       shoppinglist.append(item)
      
#     else:
#        print("Sie haben keinen Artikel hinzugefügt!")

   
      
# def show_shoppinglist():
     
#    if shoppinglist:
#        print("Deine Einkaufsliste:")
#        for item in shoppinglist:  
#         print(item) 
     
#    else:
#         print("Deine Einkaufsliste ist leer")


# def main():

#  while True:
#     print("------------------------------------------------ Einkaufsliste --------------------------------------------------------")
#     print("1. Artikel zur Einkaufsliste hinzufügen")
#     print("2. Einkaufsliste anzeigen")
#     print("3. Programm beenden")
#     choice = input("welche nummer wählen Sie aus? (also 1, 2 oder 3)")
#     print("ihre Auswahl:", choice)

#     if choice=="1":
#         add_item()
#     elif choice=="2":
#         show_shoppinglist()
#     elif choice=="3":
#         print("Programm wird beendet! Auf Wiedersehen")  
#         break
#     else:
#         print("Ungültige Auswahl. Bitte wähle 1, 2 oder 3") 

          
# main()


   


  




    












  


