#fp = open("demo.txt","r")
#data = fp.read()
#print(data)
#print(type(data))
#fp.close()


#f = open("demo.txt","w")

#data = f.write("Hi\ni am santanu mandal\nnow i am writing a code with java\njava is easy language")

#with open("demo.txt","r") as f:
#    data = f.read()

#new_data = data.replace("java","python")
#print(new_data)

#with open("demo.txt","w") as f:
#    f.write(new_data)

#word = "writing"

#with open("demo.txt","r") as f:
#    data = f.read()
   
#    if(data.find(word) != -1): # same -> if data in word  
#        print("data found")
#    else:
#        print("data not found")


def check_for_line():
    word = "Hi"
    data = True
    line_no = 1
    with open("demo.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

