class Kangaroo:
    def __init__(self):
        self.pouch_contents=[]
    def put_in_pouch(self,s):
        if s in self.pouch_contents:
            print("object already in pounch")
        else:
            self.pouch_contents.append(s)
    def __str__(self):
        if self.pouch_contents==None:
            return "The kangaroo's pounch is empty."
        else:
            return "The kangaroo's pounch contains:{}".format(self.pouch_contents)
    
anne=Kangaroo()
anne.put_in_pouch("a little kangaroo baby")
anne.put_in_pouch("a little kangaroo baby")
anne.put_in_pouch("dsd")
anne.put_in_pouch("dgdf")
print(anne)

