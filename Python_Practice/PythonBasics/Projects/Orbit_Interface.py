import Orbital_Time_Period,Constants

Pi = Constants.PI
G = Constants.G
M = Constants.Mass_Earth

radius = int(input("Enter radius: "))
print(Orbital_Time_Period.Time_Period(Pi,G,M,radius))