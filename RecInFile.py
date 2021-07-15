import random
alphabet = list("ъАеMfVCчОiХDpmЭ[фBe%`эшT6щГUIТИ wЬnц}ы2я3;Е9П,з?ЫуЧЪS:(rGyOпP]{o|юkЩaQБJ+/#1jаZЗлгьж@uД$s~ElНvF4ЙтЯсKмЛ5ёqWв=)X!хNЁ7дн8gЦYиУ*h\оКйМВ0бФcШdРHxкtрARLz.Сb-ЮЖ")      
class UserDialog():
    def MenuOfChoice():
         print("  1 - Encrypt\n  2 - Decrypt\n  3 - Finish")
         inpt = input()
         if inpt == "1":
              Modes.NumberOne()
              UserDialog.MenuOfChoice()
         elif inpt == "2":
              Modes.NumberTwo()
              UserDialog.MenuOfChoice()
         elif inpt == "3":
              print("Finish")
         else:
              UserDialog.MenuOfChoice()
    def EnterTxt():
        print("Enter text:")
        txt = input()
        return txt
    def GetFile():
        print("Enter filename:")
        filename = input()
        return filename
class FileDialog():
    def ReadTxt(file):
        filetxt  = open(file+'.txt','r')
        worktxt = filetxt.read()
        filetxt.close()
        return worktxt
    def WriteTxt(file, encrypttxt):
        filetxt  = open(file+'.txt','w')
        worktxt = filetxt.write(str(encrypttxt))
        filetxt.close()
class Encrypter():
    def RANDOMKEY():
        out =''.join(random.sample(alphabet,3))
        return out
    def SEARCHKEY(word):
        out =[]
        for t in range(3):
            out.insert(t*-1, word[len(word)-t-1])
        return(out)
    def Decrypt(word,key):
        out = ""
        wi = []
        ki = []
        for j in range(len(word)-3):
            wi.insert(j, alphabet.index(word[j]) )
        for i in range(len(key)):
            ki.insert(i, alphabet.index(key[i]) )
        for q in range(len(wi)):
            out += alphabet[((wi[q]-ki[q%3])+len(alphabet))%len(alphabet)]
        print(out)
    def Encrypt(word, key):
        out = ""
        wi = []
        ki = []
        for j in range(len(word)):
            wi.insert(j, alphabet.index(word[j]) )
        for i in range(len(key)):
            ki.insert(i, alphabet.index(key[i]) )
        for q in range(len(wi)):
            out += alphabet[(wi[q]+ki[q%3])%len(alphabet)]
        out += ''.join(key)
        return out
class Modes():
    def NumberOne():
        FileDialog.WriteTxt(UserDialog.GetFile(),Encrypter.Encrypt(UserDialog.EnterTxt(),Encrypter.RANDOMKEY()))
    def NumberTwo():
        word = FileDialog.ReadTxt(UserDialog.GetFile())
        Encrypter.Decrypt(word,Encrypter.SEARCHKEY(word))
UserDialog.MenuOfChoice()