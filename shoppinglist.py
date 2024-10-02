shoppinglist=[]
def add_item():
    item = input("Bitte gib den Artikel ein, der zur Einkaufsliste hinzugefügt werden soll")
    print ("Ihre Artikel :", item)
    shoppinglist.append(item)
    print("der Artikel wurde der Liste hinzugefügt")
    print(shoppinglist)
    
add_item() 


def show_shoppinglist():
   
   if shoppinglist:
        print ("your shoppinglist ", shoppinglist)

   else:
       
        print("shoppinglist ist leer")

show_shoppinglist()


while True:
    print("------------------------------------------------ Einkaufsliste --------------------------------------------------------")
    print("1. Artikel zur Einkaufsliste hinzufügen")
    print("2. Einkaufsliste anzeigen")
    print("3. Programm beenden")
    choice = input("welche nummer wählen Sie aus? (also 1, 2 oder 3)")
    print("ihre Auswahl:", choice)
    if choice==1:
        add_item()
    elif choice==2:
        show_shoppinglist()
    elif choice==3:
        print("Programm wird beendet! Auf Wiedersehen")  
        break
    else:
        print("Ungültige Auswahl. Bitte wähle 1, 2 oder 3")   
          



    












  


