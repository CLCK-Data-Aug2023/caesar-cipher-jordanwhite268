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
    " ":" "}
sentence = sentence.lower()
for l in sentence:
    print(right_shift_5[l], end="")



   
              