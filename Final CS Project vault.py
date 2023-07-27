# COMPUTER SCIENCE PROJECT CLASS 12
# "Secured Data Vault"
# by Sehajdeep Singh : Class XII - B

'''This program securely stores data/notes in the file "vault.dat",
using a user defined "MASTER PASSWORD" To Encrypt the text'''

# IMPORTS
#Hello
import pickle
import random

# ENCRYPTION DICTIONARIES
enc_dict1= {'a': 'z','b': '+','c': 'β', 'd': 'd','e': 'δ','f': 'σ','g': 'G',
            'h': 'ϕ','i': 'π','j': 'Q', 'k': 'ν','l': '¥','m': 'm','n': 'Σ',
            'o': '}','p': 'γ','q': '*', 'r': '$','s': 'α','t': 'Δ','u': 'l', 
            'v': 'k','w': 'η','x': 'u', 'y': 'ω','z': 'Ψ',' ': 'ε','~': '^',
            '.': '`',',': '.','?': '%', '0': '_','1': 'o','2': '|','3': '0',
            '4': '/','5': 'a','6': '#', '7': '?','8': '<','9': '9'}

enc_dict2= {'a': '5','b': 'q','c': 'u', 'd': 'd','e': 'b','f': 'e','g': '7',
            'h': 'j','i': 'y','j': '8', 'k': 'x','l': 'c','m': '{','n': '%', 
            'o': 't','p': '2','q': 'h', 'r': '1','s': 'm','t': 'i','u': 'o', 
            'v': 'f','w': 's','x': '9', 'y': 'w','z': '6',' ': 'n','~': '^',
            '.': 'g',',': 'r','?': 'p', '0': 'z','1': 'v','2': '?','3': '3',
            '4': '-','5': 'l','6': '0', '7': 'k','8': '4','9': 'a'}


enc_dict3= {'a': 'γ','b': 'δ','c': 'ο', 'd': 'λ','e': 'κ','f': 'Φ','g': 'ψ',
            'h': 'σ','i': 'y','j': 'ξ', 'k': 'ι','l': 'υ','m': '{','n': '}',
            'o': 'ρ','p': 'ν','q': 'μ', 'r': 'φ','s': 'τ','t': 'Ψ','u': 'Ω', 
            'v': 'f','w': 's','x': '9', 'y': 'η','z': 'θ',' ': 'Σ','~': '|',
            '.': 'ζ',',': 'π','?': 'ε', '0': 'α','1': 'v','2': '?','3': 'ω',
            '4': '-','5': 'Θ','6': 'β', '7': 'Ξ','8': 'Λ','9': 'Π'}

# DECRYPTION DICTIONARIES
denc_dict1={'9' :'9','<' :'8','?' :'7' ,'#' :'6','a' :'5','/' :'4','0' :'3',
            '|' :'2','o' :'1','_' :'0' ,'%' :'?','.' :',','`' :'.','^' :'~',
            'ε' :' ','Ψ' :'z','ω' :'y' ,'u' :'x','η' :'w','k' :'v','l' :'u',
            'Δ' :'t','α' :'s','$' :'r' ,'*' :'q','γ' :'p','}' :'o','Σ' :'n',
            'm' :'m','¥' :'l','ν' :'k' ,'Q' :'j','π' :'i','ϕ' :'h','G' :'g',
            'σ' :'f','δ' :'e','d' :'d' ,'β' :'c','+' :'b','z' :'a'}

denc_dict2={'a' :'9','4' :'8','k' :'7' ,'0' :'6','l' :'5','-' :'4','3' :'3',
            '?' :'2','v' :'1','z' :'0' ,'p' :'?','r' :',','g' :'.','^' :'~',
            'n' :' ','6' :'z','w' :'y' ,'9' :'x','s' :'w','f' :'v','o' :'u',
            'i' :'t','m' :'s','1' :'r' ,'h' :'q','2' :'p','t' :'o','%' :'n',
            '{' :'m','c' :'l','x' :'k' ,'8' :'j','y' :'i','j' :'h','7' :'g',
            'e' :'f','b' :'e','d' :'d' ,'u' :'c','q' :'b','5' :'a'}


denc_dict3={'Π' :'9','Λ' :'8','Ξ' :'7' ,'β' :'6','Θ' :'5','-' :'4','ω' :'3',
            '?' :'2','v' :'1','α' :'0' ,'ε' :'?','π' :',','ζ' :'.','|' :'~',
            'Σ' :' ','θ' :'z','η' :'y' ,'9' :'x','s' :'w','f' :'v','Ω' :'u',
            'Ψ' :'t','τ' :'s','φ' :'r' ,'μ' :'q','ν' :'p','ρ' :'o','}' :'n',
            '{' :'m','υ' :'l','ι' :'k' ,'ξ' :'j','y' :'i','σ' :'h','ψ' :'g',
            'Φ' :'f','κ' :'e','λ' :'d' ,'ο' :'c','δ' :'b','γ' :'a'}

# CHECKING FOR EXISTING VAULT FILE. IF FILE DOES NOT EXISTS IT WOULD GET CREATED
try:

    y = open('vault.dat','rb')

except FileNotFoundError:
    
    # empty list is dumped in the file, allowing multi-user 'vaults' to be created
    y = open('vault.dat','wb')
    pickle.dump([],y)
    y.close()
    print('\nNew Vault File Successfully Created')

# SHUFFLE RAW DATA BASED ON PASSWORD
def reOrder(mode, data, master):
    pswrd = master
    len_pswrd = len(pswrd)
    Inp = list(data)
    len_inp = len(Inp)

    if mode == "shuffle" or mode == "S":

        # dividing the text into cells, and ensuring that they are complete 
        if (len_inp%10) !=0:
            Inp += (10-(len_inp%10)) * '~'

        asc = ''   

        for Chr in pswrd:
            asc = str(ord(Chr))
            # using the unique ASCII values of the characters to generate random list indexes
            for n in range(0,len_pswrd):                      
                el1 =int(max(asc))+int(min(asc))+ n           
                el2 = int(max(asc)) - int(min(asc)) + n//2
                # interchanging of letters    
                if el1<= 9 and el2 <= 9:
                    Inp[el1],Inp[el2] = Inp[el2],Inp[el1]

        return(Inp)
    
    # reversing the shuffle() algorithm 
    if mode == "unshuffle" or mode == "U":
        Rpswrd= pswrd[::-1]

        Id = Inp.pop(0)

        asc= ''  
        for Chr in Rpswrd:
            asc= str(ord(Chr))
            
            # navigating through the password in the opposite manner
            for n in range(len_pswrd-1,-1,-1):                
                el1=int(max(asc))+int(min(asc))+ n            
                el2= int(max(asc)) - int(min(asc)) + n//2
                
                # putting characters back into order
                if el1<= 9 and el2 <= 9:
                    Inp[el1],Inp[el2] = Inp[el2],Inp[el1]

        return(Inp,Id)

# REPLACE SHUFFLED DATA WITH OTHER CHARACTERS
def substitution(mode, data, master):
    if mode == "encrypt" or mode == "E":
        KEYS = {1:'W', 2:'S', 3:'H', 4:'W', 5:'S', 6:'H'}
        KEYS_2 = {1:enc_dict1, 2:enc_dict2, 3:enc_dict3, 4:enc_dict1, 5:enc_dict2, 6:enc_dict3}

        # to randomly select any one of the Substitution Dictionaries
        key_Id= random.randint(1,6)          
        req_key= KEYS_2[key_Id]

        list_inp = data

        # converting the jumbled list of characters into string
        string_inp = ''
        for el1 in list_inp:
            string_inp += el1.lower()

        # replacing characters
        encrypted_string=''
        for el2 in string_inp:
            if el2 in req_key:
                encrypted_string += req_key[el2]
            else:
                encrypted_string += el2  

        # placing key identifier
        encrypted_string = KEYS[key_Id] + encrypted_string 

        return(encrypted_string)
    
    if mode == "decrypt" or mode == "D":
        # to navigate through the Id to the decrypting lists
        Decryption_KEYS = {'W':denc_dict1, 'S':denc_dict2, 'H':denc_dict3}

        decrypted_list, identifier = data
        req_decryptionkey = Decryption_KEYS[identifier]

        # converting the list into a string along with substituting the characters
        decrypted_string = ''
        for Chr in decrypted_list:

            if Chr in req_decryptionkey:
                decrypted_string += req_decryptionkey[Chr]

            else:
                decrypted_string += Chr

        # remove tildes(" ~ ") placed for cell completion from decrypted output
        pos = -1
        o = list(decrypted_string)
        while True:
            if o[pos] == "~" or o[pos] == "":
                o[pos] = ""
            else:
                out = ""
                for j in o:
                    out += j
                break
            pos -= 1
        return(out)


# VAULT MANAGEMENT FUNCTIONS
# storage format =>[Id,Verification key(Encrypted),data(in the form of dictionary)]
# data format => {TITLE:text}

# FOR INITIALISING THE VAULT FOR STORING DATA 
def vaultinitialise(Id,mp):
    path = "vault.dat"
    with open(path, "rb") as vlt:
        vaultData = pickle.load(vlt)

    # verification key, allowing only the user access in their vault,without storing the Master Password 
    verif_key = substitution('E',reOrder('S','verified', mp),mp)

    lst=[Id,verif_key,{}]
    vaultData.append(lst)

    with open(path, "wb") as vlt:
        pickle.dump(vaultData, vlt)
        print('\nNew Vault Added Successfully')

# TO READ THE STORED TEXT FROM THE VAULT
def readFromVault(Id,mp):
    dt = ''
    output = ''
    path = "vault.dat"
    with open(path, "rb") as vlt:
        vaultData = pickle.load(vlt)
    
    data={}
    found=False
    valid_mp=False
    for lst in vaultData:
        if lst[0] == Id:
            found=True
            # Verifying the Master Password using the verification key
            if substitution('D',reOrder('U', lst[1], mp),mp) == 'verified':
                valid_mp=True
                data = lst[2]
    
    if found==True and valid_mp==True:
        for i in data:
            print(i)

        ch= input('> ')  # for choosing the required title, through their index numbers

        for i in data:
            if i[1]==ch:
                dt=data[i]
                dt = dt.split('\n')
                for el in dt:
                    el = el.replace('\n','')
                    if el != '':
                        #decrypting the required text
                        output += substitution("D", reOrder("U", el, mp), mp) + '\n'

        return(output,found,valid_mp)

    else:
        return(output,found,valid_mp)

#TO ADD THE TEXT TO THE VAULT
def addToVault(inp,Id,mp):
    path = "vault.dat"
    with open(path, "rb") as vlt:
        vaultData = pickle.load(vlt)
    
    title = input("\nTITLE: ")
    fav = input("Mark as Favorite? (Y/N): ")
    if fav in "Yy":
        fav = '*'   

    else:
        fav= ' ' 

    n=0
    found=False
    valid_mp=False
    finalData=[]
    data={}
    for lst in vaultData:
        if lst[0] == Id:
            found=True
            
            # Verifying the Master Password using the verification key
            if substitution('D',reOrder('U',lst[1], mp),mp)=='verified':
                data = lst[2]
                n = len(data)+1
                n = str(n) + '-'
                # adding the titles to the dictionary after putting their index numbers
                data[fav+str(n)+title] = inp
                lst[2] = data                 # putting the modified dictionary in the vault list 
                finalData.append(lst)
                valid_mp = True
        else:
            finalData.append(lst)

    if found == True and valid_mp == True:
        with open(path, "wb") as vlt:
            pickle.dump(finalData, vlt)
            print('\nDATA ADDED')
    
    return(found,valid_mp)

# TO DELETE CERTAIN TITLES FROM THE VAULT 
def deleteVaultEntries(Id,mp):
    print()
    path = "vault.dat"
    with open(path, "rb") as vlt:
        vaultData = pickle.load(vlt)
    
    data={}
    n=0     # local variable to help identify the title through its index
    found=False
    valid_mp=False
    for lst in vaultData:
        n+=1
        if lst[0]==Id:
            found=True
            # Verifying the Master Password using the verification key
            if substitution('D',reOrder('U',lst[1],mp),mp)=='verified':
                valid_mp=True
                data=lst[2]
                break

     
    if found==True and valid_mp==True:
        for i in data:
            print(i)

        ch= input('> ')
        num = 0
        el1 = ''
        data1 = {}
        for i in data:
            if i[1]==ch:
                del data[i]
                
                # reassigning the index numbers to the other titles
                for el in data:
                    num += 1
                    el1 = el[0] + str(num) + el[2:]
                    data1[el1] = data[el]

                lst[2] = data1
                vaultData[n-1] = lst # adding the corrected list to the vault list               
                with open(path, "wb") as vlt:
                    pickle.dump(vaultData, vlt)
                print("\nEntry Deleted")
                break
        else:
            print('INVALID TITLE NUMBER SELECTED, PLEASE TRY AGAIN')

    else:
        print('Invalid Id or Master Password,\nPlease Try Again.')

# TO DELETE THE WHOLE VAULT LIST OF THE SPECIFIC ID
def deleteVault(Id,mp):
    print()
    path = "vault.dat"
    with open(path, "rb") as vlt:
        vaultData = pickle.load(vlt)
    
    n=0
    found=False
    valid_mp=False
    for lst in vaultData:
        n+=1
        if lst[0]==Id:
            found=True
            # Verifying the Master Password using the verification key
            if substitution('D',reOrder('U',lst[1],mp),mp)=='verified':
                valid_mp=True
                break
    # final confirmation
    perm = ''
    if found==True and valid_mp==True:
        string = 'YOU ARE SURE YOU WANT TO DELETE THE VAULT WITH VAULT ID: '+Id+' (y/n)? '
        perm=input(string)
    
    else:
        print('Invalid Id or Master Password,\nPlease Try Again.' )

    if perm in 'Yy':
        try:
            #deleting the vault list of the given Id from the main vault
            del(vaultData[n-1])
            with open(path, "wb") as vlt:
                pickle.dump(vaultData, vlt)
                        
            print("\nVault Deleted")
        except IndexError:
            pass

# MAINLOOP
mainMenu = """
 ____      __     __          _ _   
|  _ \\ _   \\ \\   / /_ _ _   _| | |_ 
| |_) | | | \\ \\ / / _` | | | | | __|
|  __/| |_| |\\ V / (_| | |_| | | |_ 
|_|    \\__, | \\_/ \\__,_|\\__,_|_|\\__|
       |___/                        

1 - ENCRYPT
2 - DECRYPT
3 - INITIALISING VAULT
4 - DELETING EXISTING DATA
5 - EXIT
"""
while True:
    print("\n" + mainMenu)
    choice = int(input("> "))

    # FOR ENCRYPTING THE TEXT
    # AND STORING IT IN THE VAULT(OPTIONAL)
    if choice == 1:
        output = ''
        dt = ''
        output_list = []
        mp1 = ''
        while True:
            print('\nENCRYPTION MODE')
            ch = int(input("\n1 - ENTER TEXT MANUALLY\n2 - READ FROM FILE\n3 - EXIT MODE\n> "))
            print()
            if ch == 1:
                # to multiline take input           
                c = input("Multiline text?(y/n):  ")
                if c in "Yy":
                    lst=[]
                    print('Taking Multiline Input.\nWrite \'-END-\' As The Last Input To Mark The End Of Text.' )
                    line=''
                    while True:
                        line = input('>>')
                        if line == '-END-':
                            break
                        lst.append(line)

                    mp = input('ENTER THE MASTER PASSWORD: ')
                    mp1 = mp                    
                    
                    for line in lst:
                        line = line.replace('\n','')  # to allow the encryption algorithm to work properly
                        output +=  substitution("E", reOrder("S", line, mp), mp) + '\n'
                else:
                    dt = input("\nTEXT: ")
                    mp = input("\nMASTER PASSWORD: ")
                    mp1 = mp
                    output = substitution("E", reOrder("S", dt, mp), mp)

            elif ch == 2:
                fn = input("PATH TO TEXT FILE: ")
                f = open(fn, 'r')
                dt = f.readlines()
                f.close()
                mp = input("\nMASTER PASSWORD: ")
                mp1 = mp
                for el in dt:
                    el1 = el.replace('\n','')
                    output += substitution("E", reOrder("S", el1, mp), mp) + '\n'

            elif ch == 3:
                break

            else:
                print('INVALID OPTION.\nPLEASE TRY AGAIN')
                pass                

            # options after output is generated
            print('OUTPUT: ',output)
            ch = int(input('\nOUTPUT GENERATED\n1 - ADD TO VALUT\n2 - CANCEL\n> '))
            # adding to vault
            if ch == 1:
                count = 0
                outp = ''
                while count <2: # to ensure security, only one retry is allowed
                    outp = ''
                    count += 1    
                    Id = input('\nID: ')    
                    mp = input('\nVAULT MASTER PASSWORD: ')             
                    
                    # to check if the used password is the same as the vault's Master Password
                    # if not then the code is decrypted and then encrypted using the vault's Master Password
                    if mp == mp1:
                        found,valid_mp = addToVault(output,Id,mp)

                    else:
                        output_list = output.split('\n')
                        for el in output_list:
                            el = el.replace('\n','')
                            if el != '':
                                el = substitution("D", reOrder("U", el, mp1), mp1)
                                outp += substitution("E", reOrder("S", el, mp), mp) + '\n'

                        found,valid_mp = addToVault(outp,Id,mp)

                    if count == 2:
                        print('INVALID ID or MASTER PASSWORD.\nTRY AGAIN LATER.')
                        break
                    
                    # to ensure that only authentic users get access to the vault
                    if found == False or valid_mp == False:
                        perm = input('Invalid ID or MASTER PASSWORD. Do you want to try again?(y/n): ')
                        if perm in 'Nn':
                            break
                    
                    if found == True or valid_mp == True:
                        break

            else:
                pass
    
    # FOR DECRYPTING THE TEXT
    # FOR READING FROM THE VAULT(OPTIONAL)
    elif choice == 2:
        output = ''
        output_list = []
        while True:
            print('\nDECRYPTION MODE')
            ch = int(input("\n1 - ENTER ENCRYPTED TEXT MANUALLY\n2 - READ FROM VALUT\n3 - EXIT MODE\n> "))
            if ch == 1:
                # to take multiline input
                c = input("Multiline text? (y/n) ")
                if c in "Yy":
                    lst=[]
                    print('Taking Multiline Input.\nWrite \'-END-\' As The Last Input To Mark The End Of File.' )
                    line=''
                    while True:
                        line=input('>>')
                        if line == '-END-':
                            break
                        line=line[:-2]
                        lst.append(line)
                        mp = input("\nMASTER PASSWORD: ")
                    
                    for line in lst:
                        el1 = el.replace('\n','')
                        output +=  substitution("E", reOrder("S", line, mp), mp) + '\n'
                        output_list += [substitution("E", reOrder("S", line, mp), mp) + '\n']

                else:
                    dt = input("\nTEXT: ")
                    mp = input("MASTER PASSWORD: ")
                    output = substitution("D", reOrder("U", dt, mp), mp)

            elif ch == 2:
                Id = input('ENTER ID: ')
                mp = input("MASTER PASSWORD: ")       
                output,found,valid_mp = readFromVault(Id,mp)
                output_list = output.split('\n')
                
                if found == False or valid_mp == False:
                    print('Invalid ID or MASTER PASSWORD.\nPlease Try Again.')
                    continue

            elif ch == 3:
                break

            else:
                print('INVALID OPTION.\nPLEASE TRY AGAIN')
                pass                
                    
            # options after output is generated
            output.replace("~", "")
            print("\n" + output)
            ch = int(input('\nOUTPUT GENERATED\n1 - SAVE TO FILE\n2 - CANCEL\n> '))
            
            if ch == 1:
                n = 0
                # putting newline characters after all the list elements,
                # as writelines does not put them by default
                for el in output_list:
                    output_list[n] = el + '\n'
                    n += 1
                    
                print("\nNote: iF file doesn't exist, it will be created.")
                fn = input("PATH TO FILE: ")
                f = open(fn, 'a')
                f.writelines(output_list)
                f.close()
                print("OUTPUT HAS BEEN WRITTEN TO FILE.")

            else:
                pass
    
    elif choice == 3:
        Id = input('Enter an ID name: ')
        mp = input('Choose a Master Password\n\
(Stronger the password, stronger is the Encryption.\n\
Still it is Mandatory TO REMEMBER THE MASTER PASSWORD,\n\
as there is NO WAY TO recover your data without it.)\n>> ')
        vaultinitialise(Id,mp)

    elif choice == 4:
        ch = int(input("\n1 - Delete Vault Entries\n2 - Delete Vault\n>> "))

        if ch == 1:
            Id = input('ENTER THE ID: ')
            mp = input('ENTER THE MASTER PASSWORD: ')
            deleteVaultEntries(Id,mp)

        elif ch == 2:
            Id = input('ENTER THE ID: ')
            mp = input('ENTER THE MASTER PASSWORD: ')
            deleteVault(Id,mp)
        
        else:
            print('INVALID OPTION SELECTED.\nEXITING')

    elif choice == 5:
        break

    else:
        print('INVALID OPTION.\nPLEASE TRY AGAIN')
        pass

