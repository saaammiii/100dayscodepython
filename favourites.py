import sqlite3
import webbrowser

conn = sqlite3.connect(':memory:')
c=conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS FAVOURITES(
          title text,
          url text
          ) """)
c.execute("INSERT INTO FAVOURITES VALUES('cb','https://codebreakthrough.com')")
conn.commit()

c.execute("SELECT * FROM FAVOURITES")
results = c.fetchall()


def get_fav(title):
    c.execute(""" select * from favourites where title=? """,(title,))
    return c.fetchone()

def get_ls():
    c.execute("select * from favourites")
    return c.fetchall()

def get_add(title,URL):
    with conn:
        c.execute("insert into favourites values (?,?)",(title,URL))

def remove_fav(title):
    with conn:
        c.execute("delete from favourites where title=?", (title,))

    

while True:
    response = input("v to visit the favourite, ls for list, add for new , rm to delete , q to quit:\n")
    if response == 'v':
        print("Visiting................")
        shortcut = input("What is the shortCut??: ")
        record = get_fav(shortcut)
        print(record)
        try:
            webbrowser.open(record[1])
        except:
            print("Cannot open")
        # webbrowser.open("https://google.com")

    elif response == 'ls':
        print("Listing.........")
        print(get_ls())

    elif response == 'add':
        shortcut = input('What is the short cut?')
        distination = input("Where you want this short cut to go?")
        get_add(shortcut,distination)
        print('Added.............')

    elif response == 'rm':
        shortcut = input('what is the shortcut?')
        remove_fav(shortcut)
        print("removing........")

        
    elif response == 'q':
        break
