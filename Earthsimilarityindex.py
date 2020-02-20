#Student number: 1800 6118
import math #Imports the math module
import numpy as np #Imports the numpy module as np
import matplotlib.pyplot as plt

def ev(R,M): #Defines the function ev which which uses R, radius, and M, the mass to calculate the escape velocity
    G = 6.674e-11 #Creates a variable called G which is the universal gravitation constant
    V = np.sqrt((2*G*M)/R) #Calculates the escape velocity and saves the value as the variable V
    return V #Returns V

def Density(R,M): #Defines a function Density which uses R, radius, and M, the mass to calculate the desnity
    V = math.pi * 4/3 * R**3 #Assuming the planets are spherical, the volume of the planets are calculated and saves it as the variable V
    D = M/V #Calculates the density and saves the value as the variable D
    return D #Returns D

def ESI(R,M,T): #Creates a variable ESI for the planets in our solar system. Uses values of radius, R, Mass,R , and Temperature, T. 
	M0 = 5.972e24 #Variables for mass of Earth
	R0 = 6378 * 1000 #Variable for radius of Earth
	D0 = Density(R0,M0) #Calculates the density of Earth and saves the variable as D0
	V0 = ev(R0, M0) #Calculates the escape velocity of Earth

	ST0 = 288 #Creates a variable for the surface temperature of Earth

	Earth = np.array([R0, D0, V0, ST0]) #Creates an array for the values of Earth

	V = ev(R,M) #Calculates the escape velocity given radius and mass
	D = Density(R,M) #Calculates the density given radius and mass

	values = np.array([R, D, V, T])#Stores radius, density, escape velocity and temperature in an array 
	w = np.array([0.57, 1.07, 0.7, 5.58])#Creates an array of weights 
	n = len(values)#Stores the number of values as n 
	
	
	esi = np.prod((1-abs((values - Earth)/(values + Earth)))**(w/n))#Calculates ESI for the calculated and given values and saves it as esi
	return esi#returns esi

#Test ESI for planets in the solar system:

print('\n')
print('____________________________________________________________________________________________')
#Neptune:
MN = 1.0241e26
RN = 2462.2e4
STN = (273.15-200) #https://www.nasa.gov/centers/jpl/news/neptune-20070918.html
ESIN = ESI(RN,MN,STN)
print('The Earth similarity index of Neptune is ' + "{0:.2f}".format(ESIN))
print('\n')

#Jupiter:
MJ = 1.89813e27
RJ = 69911e3
STJ = -145 + 273.15 #https://www.nasa.gov/audience/forstudents/5-8/features/nasa-knows/what-is-jupiter-58.html
ESIJ = ESI(RJ,MJ,STJ)
print('The Earth similarity index of Jupiter is ' + "{0:.2f}".format(ESIJ))
print('\n')

#Saturn:
MS = 568319000000000000000000000
RS = 58232e3
STS = 88 #https://attic.gsfc.nasa.gov/huygensgcms/Saturn.htm
ESIS = ESI(RS,MS,STS)
print('The Earth similarity index of Saturn is ' + "{0:.2f}".format(ESIS))
print('\n')

#Uranus:
MU = 86810300000000000000000000
RU = 25362e3
STU = 49 #q
ESIU = ESI(RU,MU,STU)
print('The Earth similarity index of Uranus is ' + "{0:.2f}".format(ESIU))
print('\n')

#Mars:
MM = 6.39e23
RM = 3389.5e3
STM = 195
ESIM = ESI(RM,MM,STM)
print('The Earth similarity index of Mars is ' + "{0:.2f}".format(ESIM))
print('\n')

#Venus:
MV = 4867320000000000000000000
RV = 6051.8e3
STV = 462 + 273.15
ESIV = ESI(RV,MV,STV)
print('The Earth similarity index of Venus is ' + "{0:.2f}".format(ESIV))
print('\n')

#Mercury:
Mm = 330104000000000000000000
Rm = 2439.7e3
STm = ((430 - 180)/2) + 273.15 
ESIm = ESI(Rm, Mm, STm)
print('The Earth similarity index of Mercury is ' + "{0:.2f}".format(ESIm))
print('\n')

#https://solarsystem.nasa.gov/planet-compare/
#https://ssd.jpl.nasa.gov/
		

data = open('C:\\Users\\user\\Documents\\Talat\\Work\\School\\Uni\\Programming\\Project\\Data.dat', 'r')#Opens the data file and reads the content
Name = ([]) #Creates an empty list called 'Name'
Mj = np.array([])#Creates arrays for all of the parameters in the data file
Rj = np.array([])
Dj = np.array([])
T = np.array([])
print('\n' * 5)
print(data)
for theline in data:#Loop of every line in the data file 
	part = theline.split()#Splits the columns of the data file
	Name = np.append(Name,part[0])#Appends the name and paramters to the empty arrays and lists
	Mj = np.append(Mj,float(part[1]))
	Rj = np.append(Rj,float(part[2]))
	Dj = np.append(Dj,float(part[3]))
	T = np.append(T,float(part[4]))

M = Mj * MJ#Converts the parameters from jupiter units to SI units
R = Rj * RJ 
D = Dj * Density(RJ, MJ)#Calculates the density 
V = ev(R, M)#Calculates the escape velocity

def esiR(R):#Calculates the similarity of the radius
	w = 0.57
	n = 4
	RE = 6371 * 1000
	Resi = (1-abs((R - RE)/(R + RE)))**(w/n)
	return Resi

def esiD(D):#Function that calculates the similarity in the density
	w = 1.07
	n = 4
	RE = 6371 * 1000
	ME = 5.97219e24
	De = Density(RE, ME)
	Desi = (1-abs((D - De)/(D + De)))**(w/n)
	return Desi

def esiV(V):#Function that calculates the similarity in the escape velocity
	w = 0.7
	n = 4
	ME = 5.97219e24
	RE = 6371 * 1000
	Ve = ev(RE, ME)
	Vesi = (1-abs((V - Ve)/(V + Ve)))**(w/n)
	return Vesi
	
def esiT(T):#Function that calculates the similarity in the effective temperature (surface temperature)
	w = 5.58
	n = 4
	STe = 288
	Tesi = (1-abs((T - STe)/(T + STe)))**(w/n)
	return Tesi
	
def ESI2(V, R, D, T):#Function that calculates the ESI from similarity values of each parameter
	ESI = esiR(R) * esiD(D) * esiT(T) * esiV(V)#Calls each similarity function and multiplies them 
	return ESI
	
ESI = ESI2(V, R, D, T)#Calls the final ESI function with the given parameters 
closest = Name[np.argmax(ESI)]#Finds the index of the maximum value and indexes the name 
print('____________________________________________________________________________________________')#Prints the parameters of the highest ESI planet
print('\n' + 'The planet that is most similar to Earth is ' + closest + ' with a ESI of ' + "{0:.2f}".format(np.max(ESI)) + '\n')
print('Radius (m): ' + "{0:.2f}".format(R[np.argmax(ESI)]))
print('Density (kg/m^3): ' + "{0:.2f}".format(D[np.argmax(ESI)]))
print('Escape Velocity (m/s): ' + "{0:.2f}".format(V[np.argmax(ESI)])) 
print('Surface Temp (K): ' + "{0:.2f}".format(T[np.argmax(ESI)]))
print('\n')


fig = plt.figure()#Creates a new plot figure
fig.subplots_adjust(hspace = 1)#Sets the space of 

ax = fig.add_subplot(111)#Adds subplots
ax1 = fig.add_subplot(411)#Arranges subplots
ax2 = fig.add_subplot(412)
ax3 = fig.add_subplot(413)
ax4 = fig.add_subplot(414)

ax.spines['top'].set_color('None')
ax.spines['bottom'].set_color('None')
ax.spines['left'].set_color('None')
ax.spines['right'].set_color('None')
ax.tick_params(labelcolor='w', top='False', bottom='False', left='False', right='False')


ax1.scatter(T, esiT(T), c = 'k')#Creates a scatter plot of the similarity of Temperature and Temperature
ax1.set_xlabel('Temperature')

ax2.scatter(V, esiV(V), c = 'k')#Creates a scatter plot of the similarity of escape velocity and escape velocity
ax2.set_xlabel('Escape Velocity')

ax3.scatter(R, esiR(R), c = 'k')#Creates a scatter plot of the similarity of radius and radius
ax3.set_xlabel('Radius')

ax4.scatter(D, esiD(D), c = 'k')#Creates a scatter plot of the similarity of density and density
ax4.set_xlabel('Density')

ax.set_ylabel('ESI Values')#Sets the main y label as 'ESI Values'
ax.set_title('Similarity of Parameter vs Parameter')

plt.show()#Shows the subplots


TotESI = [np.sum(esiT(T)), np.sum(esiV(V)), np.sum(esiR(R)), np.sum(esiD(D))]#Adds the arrays of similarity for each parameter
Values = ['Temperature [K]', 'Escape Velocity [m/s]', 'Radius [m]', 'Density [Kg/m^3]']#Sets the labels for each parameter

plt.bar(Values,TotESI,0.5,align='center',color = 'black')#Creates a bar chart of total similarity for each parameter
plt.xlabel('Parameters')#Adds label for the x axis
plt.ylabel('Total ESI')#Adds label for y axis
plt.title('Bar chart of the total similairity of each parameter')
plt.show()#Shows the bar chart

SortedESI = np.sort(ESI)#Sorts the ESI smallest to highest
top1 = np.where(ESI == SortedESI[-1])#Find the index of the highest 5 ESI values
top2 = np.where(ESI == SortedESI[-2])
top3 = np.where(ESI == SortedESI[-3])
top4 = np.where(ESI == SortedESI[-4])
top5 = np.where(ESI == SortedESI[-5])
print('____________________________________________________________________________________________')
print('The 5 planets which are most similar to Earth are: ')#Prints the names of top 5 highest ESI planets 
print('\n')
print(Name[top1])
print('\n')
print(Name[top2])
print('\n')
print(Name[top3])
print('\n')
print(Name[top4])
print('\n')
print(Name[top5])
