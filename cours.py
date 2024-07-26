
# ___________________________input et output_________________________

# pour les variables c comme js 
nom = input("enter your name : ")
print(nom)
age = int (input("enter your age : ")) 
#int pour preciser que le type est un entier
print(age)

#_____________________ les conditions____________________________________

if age >= 10 : 
    print("admit")
elif age < 10 and age > 7:
    print("ratt")
else :
    print("non")


# __________________________les boucles et les chaines de caractères___________________

    
# on peut determiner d'ou en veux commencer jusqu a quoi example range (5,10)
for x in range(10) :
        print(x)
fruits = ["orange","banan","pomme"]
fruits.append("banan")
fruits.sort()
print(fruits)
for i in fruits :
     print(i)
# i=0
# while i < len(fruits) :
#      print(fruits[i])
#      i=i+1
# _________________________________ strings____________________________

nom = input("donner votre nom :")
print(len(nom))
nom = nom.upper()                 
print(nom)
# de meme pour lower la fonction capitalize() pour faire la majuscule dans la 1er lettre
# la syntaxe des fonction string est string.methode 
# la fonction endswith c pour voir est ce que une input termine par une lettre precise elle envoie true or false
position = nom.find("a")
# _____________________ the functions___________________

def nomdelafonction(a,b):
     return a+ b
somme = nomdelafonction(2,4)
print(somme)
# pour ajouter un element a mon tableau


# sort pour trier le tableau pop push pour le reste c les meme fonctions de js
 
#  ______________________________________________sets_________________________________
# c la meme chose que les tableaux la diff c au nv de fonctionnement
#  exemle add il n'ajout pas un element qui exist deja dans le tableau

MySets = {"banan","orange","kiwi"}
MySets.add("orange")
print(MySets)
print(len(MySets))
# clean c pour supprimer le set remov c pour supprimmer un element


# _____________________________tuple__________________________________
# on peut pas mannupiler les tuples
MyTuple = ("banan","orange","kiwi")
print(MyTuple)


# __________________________________dictionnary___________________________

Mydictionary = {
     "nom" :"badr",
     "age": 14,
     "note" : 14
}
Mydictionary["pays"]="maroc"
print(Mydictionary)
# Mydictionary["nom"]="achraf" c pour modifier le nom

# pour virifier est ce que un champ existe ::

if "note" in Mydictionary :
     print("la ville existe")


# _____________________files__________________________________________
# open("^myFIle.txt","r")

f = open("myFile.txt","w")
f.write("bonjour dans le nv fichier")
f.close()
c = open("myFile.txt","r")
print(c.read())