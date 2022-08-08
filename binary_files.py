import pickle

books1 = [ .......... ]
books2 = [ .......... ]
books3 = [ .......... ]
books4 = [ .......... ]

#writing
try:
    with open("out.bin", "wb") as file:
        pickle.dump(book1, file)
        pickle.dump(book2, file)
        pickle.dump(book3, file)
        pickle.dump(book4, file)
except:
    print("Ошибка при работе с файлом")
    
# reading    
try:
    with open("out.bin", "rb") as file:
        b1 = pickle.dump(file)
        b2 = pickle.dump(file)
        b3 = pickle.dump(file)
        b4 = pickle.dump(file)
except:
    print("Ошибка при работе с файлом")

print(b1, b2, b3, b4, sep="\n")
