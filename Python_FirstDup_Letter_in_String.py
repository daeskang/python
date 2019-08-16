#exampleString = "abcdefghijklmnopqrstuvwxyz123456789z"

def hashtable(string):
    #print(len(string))
    hashDic = {}
    #parse letter in string into dictionary
    for letter in string:
        key = ord(letter)%len(string)
        #print("Key: " + str(key) + " : " + letter)
        #check for match
        if(key in hashDic):
            if (hashDic[key] == letter): 
                print("Duplication Character: " + letter)
                break
            #collsion found since key is present, but value(letter) does not match 
            else:
                #collision handler
                for collision in hashDic[key]:
                    if (collision == letter):
                        print("Duplication Collision Character: " + letter)
                        break
                    else:
                        #print(hashDic[key])
                        #print(letter)
                        hashDic[key] = hashDic[key] + letter
                        #print(hashDic[key])
        else:
            hashDic[key] = letter

exampleString = input("Entering String to check duplication: ")
hashtable(exampleString)
