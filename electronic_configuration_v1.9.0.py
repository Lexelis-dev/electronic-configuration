#initiation
element_symbol=['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Ti','Pb','Bi','Po','At','Rn','Fr','Ra','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Nh','Fl','Mc','Lv','Ts','Og']
element_name=['Hydrogen','Helium','Lithium','Beryllium','Boron','Carbon','Nitrogen','Oxygen','Fluorine','Neon','Sodium','Magnesium','Aluminium','Silicon','Phosphorus','Sulfur','Chlorine','Argon','Potassium','Calcium','Scandium','Titanium','Vanadium','Chromium','Manganese','Iron','Cobalt','Nickel','Copper','Zinc','Gallium','Germanium','Arsenic','Selenium','Bromine','Krypton','Rubbidium','Strontium','Yttrium','Zirconium','Niobium','Molybdenum','Technetium','Ruthenium','Rhodium','Palladium','Silver','Cadmium','Indium','Tin','Antimony','Temmerium','Iodine','Xenon','Caesium','Barium,','Lanthanum','Cerium','Praseodymium','Neodymium','Promethium','Samarium','Europium','Gadolinium','Terbium','Dysprosium','Holmium','Erbium','Thulium','Ytterbium','Lutetium','Hafnium','Tantalum','Tungsten','Rhenium','Osmium','Iridium','Platinum','Gold','Mercury','Thallium','Lead','Bismuth','Polonium','Astatine','Radon','Francium','Radium','Actinium','Thorium','Protactinium','Uranium','Neptunium','Plutonium','Americium','Curium','Berkelium','Califormium','Einsteinium','Fermium','Mendelevium','Nobelium','Lawrencium','Rutherfordium','Dubnium','Seaborgium','Bohrium','Hassium','Meitnerium','Damstadtium','Roentgenium','Copernicium','Nihonium','Flerovium','Moscovium','Livermorium','Tennessine','Oganesson']
noble_gases=[2,10,18,36,54,86] 
default_shell=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,6,6,6,7,7]
default_subshell=[0,0,1,0,1,2,0,1,2,3,0,1,2,3,0,1,2,0,1]
subshell_name=['s','p','d','f']
default_electrons=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
order=[1,2,3,4,5,7,6,8,11,9,12,15,10,13,16,18,14,17,19]
exceptions=[24,29,41,42,44,45,46,47,57,58,64,78,79,89,90,91,92,93,96]
excepted_electrons=[[2,2,6,2,6,5,1],[2,2,6,2,6,10,1],[2,2,6,2,6,10,2,6,4,0,1],[2,2,6,2,6,10,2,6,5,0,1],[2,2,6,2,6,10,2,6,7,0,1],[2,2,6,2,6,10,2,6,8,0,1],[2,2,6,2,6,10,2,6,10],[2,2,6,2,6,10,2,6,10,0,1],[2,2,6,2,6,10,2,6,10,0,2,6,1,0,2],[2,2,6,2,6,10,2,6,10,1,2,6,1,0,2],[2,2,6,2,6,10,2,6,10,7,2,6,1,0,2],[2,2,6,2,6,10,2,6,10,14,2,6,9,0,1],[2,2,6,2,6,10,2,6,10,14,2,6,10,0,1],[2,2,6,2,6,10,2,6,10,14,2,6,10,0,2,6,1,2],[2,2,6,2,6,10,2,6,10,14,2,6,10,0,2,6,2,2],[2,2,6,2,6,10,2,6,10,14,2,6,10,2,2,6,1,2],[2,2,6,2,6,10,2,6,10,14,2,6,10,3,2,6,1,2],[2,2,6,2,6,10,2,6,10,14,2,6,10,4,2,6,1,2],[2,2,6,2,6,10,2,6,10,14,2,6,10,7,2,6,1,2]]

def generating(remaining):
    generated_electrons=default_electrons.copy()
    for i in range(0,19):
        current_subshell=default_subshell[order[i]-1]
        if remaining!=0:
            if remaining>2*(2*current_subshell+1):
                generated_electrons[order[i]-1]=(2*(2*current_subshell+1))
                remaining-=2*(2*current_subshell+1)
                last_rank=i
                
            else:
                generated_electrons[order[i]-1]=(remaining)
                remaining=0
                last_rank=i
            
        else:
            generated_electrons[order[i]-1]=0
    return generated_electrons,last_rank
            
            
#input
inputed=input("Select your desired element :\n")
try:
    searched=int(inputed)
except ValueError:
    searched=[]
    for i in range(0,len(inputed)):
        if (ord(inputed[i]) in range(65,91))and i!=0:
            searched.append(chr(ord(inputed[i])+32))
        elif (ord(inputed[i]) in range(97,123))and i==0:
            searched.append(chr(ord(inputed[i])-32))
        else :
            searched.append(inputed[i])
    searched="".join(searched)
    if searched in element_symbol:
        searched=element_symbol.index(searched)+1
    elif searched in element_name:
        searched=element_name.index(searched)+1

#generating the configuration

if searched in (exceptions):
    searched_electrons=excepted_electrons[exceptions.index(searched)]
    for i in range(0,19-len(excepted_electrons[exceptions.index(searched)])):
        searched_electrons.append(0)
    
else:
    searched_electrons=generating(searched)[0]
    
            
#printing the result
print("\nThe electronic configuration of the element",searched,element_symbol[searched-1],element_name[searched-1],"is :")
for i in range(0,19):
    if searched_electrons[i]!=0:
        print(str(default_shell[i])+str(subshell_name[default_subshell[i]])+str(searched_electrons[i]),end=" ")
if searched>2:
    #simplifying the configuration
    for i in range(0,6):
        if searched > noble_gases[i]:
            last_noble=(noble_gases[i])
            last_noble_electrons=generating(noble_gases[i])[0]
    
    simplified_searched_electrons=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(0,19):
        simplified_searched_electrons[i]=searched_electrons[i]-last_noble_electrons[i]

    #  printing the simplified result
    print("\n["+str(element_symbol[last_noble-1])+"]",end=" ")
    for i in range(0,19):
        if simplified_searched_electrons[i]!=0:
            print(str(default_shell[i])+str(subshell_name[default_subshell[i]])+str(simplified_searched_electrons[i]),end=" ")

#printing by level
leveled_configuration=[]
print("\n\nBy levels :")
for i in reversed(range(0,19)):
    if searched_electrons[i]!=0:
        leveled_configuration.insert(0,(str(default_shell[i])+str(subshell_name[default_subshell[i]])+str(searched_electrons[i])))
        if default_shell[i]!=default_shell[i-1]:
            print(*leveled_configuration)
            leveled_configuration=[]

#Position of the element
if searched==1:
    furthest_electrons=[default_shell[0],default_subshell[0],searched_electrons[0]]
    print("\nIt's located in the 1st row and the 1st element of this row.")
    print("It's in the s block.")
elif searched==2:
    furthest_electrons=[default_shell[0],default_subshell[0],searched_electrons[0]]
    print("\nIt's located in the 1st row and the 2nd element of this row.")
    print("It's in the s block.")
else:
    if searched in (exceptions):
        expected_electrons=generating(searched)[0]
        last_filled_electron=default_subshell[order[generating(searched)[1]]-1]
        position_in_row=0
        position_in_block=expected_electrons[order[generating(searched)[1]]-1]
        for i in range(0,19):
            if expected_electrons[i]!=0:
                furthest_electrons=[default_shell[i],default_subshell[i],expected_electrons[i]]
            position_in_row+=simplified_searched_electrons[i]
        print("\nIt's located in the "+str(furthest_electrons[0])+"th row and the "+str(position_in_row)+"th element of this row.")
        print("It's in the "+str(position_in_block)+"th column from the "+str(subshell_name[last_filled_electron])+" block.")

    else:
        last_filled_electron=default_subshell[order[generating(searched)[1]]-1]
        position_in_row=0
        position_in_block=searched_electrons[order[generating(searched)[1]]-1]
        for i in range(0,19):
            if searched_electrons[i]!=0:
                furthest_electrons=[default_shell[i],default_subshell[i],searched_electrons[i]]
            position_in_row+=simplified_searched_electrons[i]
        print("\nIt's located in the "+str(furthest_electrons[0])+"th row and the "+str(position_in_row)+"th element of this row.")
        print("It's in the "+str(position_in_block)+"th column from the "+str(subshell_name[last_filled_electron])+" block.")

#Finding the screening constant
screening_constant=0
if searched==2:
    screening_constant=0.31
else:
    for i in reversed(range(0,19)):
        if searched_electrons[i]!=0:
            if default_subshell[i]==0:
                if searched_electrons[i]!=1 and searched_electrons[i]!=0:
                    screening_constant+=(searched_electrons[i]-1)*0.35
                for i in reversed(range(0,i)):
                    if default_shell[i]==furthest_electrons[0]-1:
                        screening_constant+=searched_electrons[i]*0.85
                    else:
                        screening_constant+=searched_electrons[i]
                break
        
            elif default_subshell[i]==1:
                if searched_electrons[i]!=1 and searched_electrons[i]!=0:
                    screening_constant+=(searched_electrons[i]-1)*0.35
                for i in reversed(range(0,i)):
                    if default_shell[i]==furthest_electrons[0]:
                        screening_constant+=searched_electrons[i]*0.35
                    elif default_shell[i]==furthest_electrons[0]-1:
                        screening_constant+=searched_electrons[i]*0.85
                    else:
                        screening_constant+=searched_electrons[i]
                break
                
            elif default_subshell[i] in (2,3):
                if searched_electrons[i]!=1:
                    screening_constant+=(searched_electrons[i]-1)*0.35
                for i in reversed(range(0,i)):
                    screening_constant+=searched_electrons[i]
                break
print("\nThe screening constant from Slater’s Rule is :\nσ= "+str(round(screening_constant,5)))

#Energy of ionisation
IE_1=13.6*(searched-screening_constant)**2/furthest_electrons[0]**2
print("\nThe first Ionization Inergy from the Bohr Model is :\n",round(IE_1,9),"eV")

#Ionising
ion_type=int(input("\nWhat is its oxidation state?\n"))
ion_electrons=ion_type
if ion_electrons<0:
    if searched-ion_type in (exceptions):
        ion=excepted_electrons[exceptions.index(searched-ion_type)]
        print("\nThe electronic configuration of the ion "+str(searched)+" "+str(element_symbol[searched-1])+" ("+str(ion_type)+") "+str(element_name[searched-1])+" is :")
        for i in range(0,19-len(excepted_electrons[exceptions.index(searched-ion_type)])):
            ion.append(0)
        for i in range(0,19):
            if ion[i]!=0:
                print(str(default_shell[i])+str(subshell_name[default_subshell[i]])+str(ion[i]),end=" ")
    else:
        ion=generating(searched-ion_electrons)[0]
        print("\nThe electronic configuration of the ion "+str(searched)+" "+str(element_symbol[searched-1])+" ("+str(ion_type)+") "+str(element_name[searched-1])+" is :")
        for i in range(0,19):
            if ion[i]!=0:
                print(str(default_shell[i])+str(subshell_name[default_subshell[i]])+str(ion[i]),end=" ")
            
if ion_electrons>0:
    ion=searched_electrons
    for i in reversed(range(0,19)):
        if ion[i]!=0:
            if ion[i]>=ion_electrons:
                ion[i]=ion[i]-ion_electrons
                ion_electrons=0
            else:
                ion_electrons-=ion[i]
                ion[i]=0
    print("\nThe electronic configuration of the ion "+str(searched)+" "+str(element_symbol[searched-1])+" (+"+str(ion_type)+") "+str(element_name[searched-1])+" is :")
    for i in range(0,19):
        if ion[i]!=0:
            print(str(default_shell[i])+str(subshell_name[default_subshell[i]])+str(ion[i]),end=" ")

