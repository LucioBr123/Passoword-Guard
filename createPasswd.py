import random

password=''
###########Characters 


number=['0','1','2','3','4','5','6','7','8','9']

letters=['a','b','c','d','e','f',
'g','h','i','j','k','l','m','n','o',
'p','q','r','s','t','u','v','w','y',
'x','z']

symbols=['!','@','#','$','&','*','(',')']

######################
#functions select a random character

def num():
    global password
    number_random=random.choice(number)
    password+=number_random

def let():
    global password
    letters_random=random.choice(letters)
    password+=letters_random

def sym():
    global password
    symbols_random=random.choice(symbols)
    password+=symbols_random

######################################3



########################################
#parameters config#


characters=18
number_on= True
letter_on= True
symbol_on= True
##########################################





#GENERATE PASSWORD#
def create_password():
    global characters
    
    while(characters>0):
        

        if number_on==True:
            if characters==0:
                continue
            num()
            characters-= 1
            
            

        if letter_on==True:
            if characters==0:
                continue
            let()
            characters-= 1
            
        if symbol_on==True:
            if characters==0:
                continue
            sym()
            characters-= 1
    return password
        

    

##Tests

'''print(password)
create_password()
print(password)
'''


