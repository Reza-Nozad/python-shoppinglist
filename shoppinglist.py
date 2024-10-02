shoppinglist=[]
def add_item():
    item = input("Bitte gib den Artikel ein, der zur Einkaufsliste hinzugefügt werden soll")
    print ("Ihre Artikel :", item)
    shoppinglist.append(item)
    print("der Artikel wurde der Liste hinzugefügt")
    print(shoppinglist)

add_item()  

  


