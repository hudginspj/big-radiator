import math
#denom=4181.3*100
#nom=2*math.pi*au**2*sigma*323**4
#print(nom)
#water=nom/denom

def mass_flux(radius,sig,sph,t,deltat):
    powers=power(radius,t,sig)
    denom=sph*deltat
    mass_fl=powers/denom
    return mass_fl
def power(radius,t,sig):
    nom=2*math.pi*radius**2*sig*t**4
    return nom 

ly=9.4e15
au=1.5e11
#denom=4181.3*100
sigma= 5.67037e-8
waters_spefic_heat=4181.3
waters_T=323
w_delta_T=373-273
l_del=6-0
t_l=6
l_sup_con=297*6

auleadmass=mass_flux(au,sigma,l_sup_con,t_l,l_del)
lyleadmass=mass_flux(ly,sigma,l_sup_con,t_l,l_del)
tenlyleadmass=mass_flux(10*ly,sigma,l_sup_con,t_l,l_del)
twentylyleadmass=mass_flux(20*ly,sigma,l_sup_con,t_l,l_del)
thritylyleadmass=mass_flux(30*ly,sigma,l_sup_con,t_l,l_del)
fiftylyleadmass=mass_flux(50*ly,sigma,l_sup_con,t_l,l_del)
hunredlyleadmass=mass_flux(100*ly,sigma,l_sup_con,t_l,l_del)
twohunredlyleadmass=mass_flux(200*ly,sigma,l_sup_con,t_l,l_del)
thosandlyleadmass=mass_flux(1000*ly,sigma,l_sup_con,t_l,l_del)
fivethosandlyleadmass=mass_flux(5000*ly,sigma,l_sup_con,t_l,l_del)

lightyearmass=mass_flux(ly,sigma,waters_spefic_heat,waters_T,w_delta_T)
aumass=mass_flux(au,sigma,waters_spefic_heat,waters_T,w_delta_T)

tenlightyearmass=mass_flux(10*ly,sigma,waters_spefic_heat,waters_T,w_delta_T)
twentylightyearmass=mass_flux(20*ly,sigma,waters_spefic_heat,waters_T,w_delta_T)
print(aumass)
print(lightyearmass)
print(tenlightyearmass)
print(5000*ly)
print(twentylightyearmass)
print(auleadmass)
print(lyleadmass)
print( "ten", tenlyleadmass)
print( twentylyleadmass)
print(thritylyleadmass)
print(fiftylyleadmass)
print("hundred" , hunredlyleadmass)
print(thosandlyleadmass)
print (power(5000*ly,t_l,sigma))
print(fivethosandlyleadmass)
