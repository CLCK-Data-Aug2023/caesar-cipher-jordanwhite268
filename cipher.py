sentence= input("Please enter a sentence:" )
right_shift_5 = {   
    "a":"f",    
    "b":"g",   
    "c":"h",   
    "d":"i",   
    "e":"j",    
    "f":"k",   
    "g":"l",   
    "h":"m",
    "i":"n",  
    "j":"o",  
    "k":"p", 
    "l":"q", 
    "m":"r", 
    "n":"s",  
    "o":"t",  
    "p":"u",  
    "q":"v",  
    "r":"w",
    "s":"x",  
    "t":"y",  
    "u":"z",  
    "v":"a",  
    "w":"b",  
    "x":"c",  
    "y":"d", 
    "z":"e", 
    " ":" ", 
    "_":"_",
    "!":"!",
    "#":"#",
    "$":"$",
    "%":"%",
    "^":"^",
    "&":"&",
    "*":"*",
    "(":"(",
    ")":")",
    "1":"1",
    "2":"2",
    "3":"3",
    "4":"4",
    "5":"5",
    "6":"6",
    "7":"7", "8":"8","9":"9","0":"0", ".":"."
    
}
sentence = sentence.lower()
encrypted_sent = []
for l in sentence:
    encrypted_sent.append(right_shift_5[l])

print("The encrypted sentence is:", "".join(encrypted_sent))
   
              