# file_obj = open("test.txt","r")
# print(file_obj.readlines())
# file_obj.close()
# X => create a file
#fo = open("newfile.txt","xt")
#write content = >
#fo.write("we are new to python")
# to close a file
#fo.close()

# fh = open("test.txt","wt")
# fh.write("testing overwritten feature againv")
# #fh.close()

with open("test.txt","rt") as fh:
    print(fh.read())