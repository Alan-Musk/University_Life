with open("n.txt","r") as input_file:
    text=input_file.read()
    text=text.replace(",","\n").replace(".","\n")
    

with open("out.txt","w") as output_file:
    output_file.write(text)