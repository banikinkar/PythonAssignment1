import pickle

books={'book1':{'subject':'History','author':'Carol','price':50,'pages':100},
       'book2':{'subject':'Science','author':'Smith','price':66,'pages':90},
       'book3':{'subject':'Math','author':'Steve','price':80,'pages':110},
       'book4':{'subject':'Geography','author':'Jack','price':90,'pages':40}
      }
# print(books)
# print(type(books))
# try:
#     with open('books_detail.txt','w') as fh:
#       fh.write(books)
# except TypeError:
# with open('books_detail.txt','wt') as fh:
#        fh.write(str(books))

# print(type(books))

# with open('books_detail.txt', 'rt') as fh:
#     content= fh.read()
#     print(type(content))

# serialisation
with open('books_module.bin', 'bw') as f:
    for i in books:
        pickle.dump(books[i], f)

#deserialisation
with open('books_module.bin', 'rb') as f:
    data1 = pickle.load(f)
    print(data1,type(data1))
    data2 = pickle.load(f)
    print(data2,type(data2))
    data3 = pickle.load(f)
    print(data3,type(data3))






