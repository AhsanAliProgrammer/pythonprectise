# #Prompt user for number
# number = int (input("Input a number"))
# #Print out the solution
# print (number + 3 * 2 - 4 - (number * 2) + 3)


# a=int(input('Enter temperature in celcius'))
# i=(a*1.8)+32
# print('Temperature in Fahrenheit is',i)


# a=int(input('Enter radius of circle : '))
# i=3.142*a*a
# print('area of circle is : ',i)

# a=input('Enter the favourate color : ')
# print(a*10)
# print(a+"                               "+a)
# print(a*10)


# a="\t.ulMy Name is Ahsan Aliill\t"
# print(a)
# print(a.lstrip("\t.ul"))
# print(a.rstrip("\till"))
# print(a.strip("\t.ulill"))

# start lab2

# dictionary={'First Name': 'ahsan','Last Name':'ali','age':21,'city':'karachi'}
# for a,b in dictionary.items():
#     print(a,':',b)


# buffet={'chicken biryani','chicken karahi','burgur','beef pulao','broast'}
# print('menu\n')
# for i in buffet:
#     print(i)
# buffet.append('beef biryani')


# Guest=['ahsan','adill','wajahat']
# for i in Guest:
#     print('your are invited for dinner',i)


# Guest=['ahsan','adill','wajahat']
# for i in Guest:
#     print('your are invited for dinner',i)

# Guest[2]=('ubaid')
# print('\nNew invitation list\n')
# for i in Guest:
#     print('you are invited for dinner',i)


E = int(input("Enter the voltage of the power source:"))
Rsource = int(input("enter the source resistance: "))
Pmax = 0
Rload = 0.1 * Rsource
print("\n{:10} {:10} {:15} {}" .format("Rload", "Vload", "Current", "Pload"))

while Rload <= 2 * Rsource:
    I = E/ (Rload + Rsource)
    Vload = E * Rload/ (Rsource + Rload)
    Pload = I * Vload
    if Pload > Pmax:
        Pmax = Pload
    print ("{:g} {:12g} {:13g}" .format(Rload, Vload, I ,Pload))
    Rload = Rload + (0.1 * Rsource)
    
print("\n",Pmax)

sf = 50.0/Pmax
while Rload <= 2 * Rsource:
    I = E/(Rload + Rsource)
    Vload = E * Rload/(Rsource + Rload)
    Pload = I * Vload
    print(Rload, "\t\t", int(Pload * sf) * "*")
    Rload = Rload + (0.1 * Rsource)