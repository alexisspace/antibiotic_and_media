# -*- coding: utf-8 -*-
"""
Created on Thu May 23 19:17:47 2019

@author: AORTEGA
"""

# Input all values in units of mg and mL, otherwise the results will be wrong
#----------------------------------------
# PART I: Antibiotic stock calculations
# Calculates the amount of water to add to a given mass of antibiotic to obtain
# a stock concentration
# See https://www.addgene.org/mol-bio-reference/#antibiotics
stock_concentration = 50.0      # units are (mg/mL); Given by manufacturer (Kanamycin is 50 mg/mL) (Ampicillin is 100 mg/mL)
antibiotic_mass = 500  # (mg); This is the amount of anbiotic mass you want to use
v_stock = antibiotic_mass/stock_concentration # Calculation of the required volume
print('\nPART I: stock concentration  -----------')
print('v_stock: {} mL of water; for an antibiotic_mass of {} mg'.format(v_stock, antibiotic_mass))

#----------------------------------------
# PART II: LB Agar plates calculations
# Calculates the amount o LB Agar mass to be added to a volume of water to fill
# a given number of plates (n_plates) of given volume (v_plate)
lb_agar_concentration = 40.0 # units are (mg/mL) this is provided by the agar manufacturer 
# See http://www.the-odin.com/lb-agar/
v_plate = 40.0 # units are (mL); Volume of each plate
n_plates = 2 # Number of plates desired
v_plates_total = n_plates*v_plate   # units are (mL) 
lb_agar_mass = lb_agar_concentration*v_plates_total # units are (mg); LB Agar mass required
print('\nPART II LB Agar plates -----------')
print('lb_agar_mass: {0} mg for {1} plates in {2} mL of water:'.format(lb_agar_mass, n_plates, v_plates_total))


#----------------------------------------
# PART III: Antibiotic in the stock concentration to be present in the LB Agar mix
# Calculates the necessary volume of antibiotic in the stock concentration to be 
# present the final volume v2 of LB Agar preparation
# NOTE: You can change the values of c1, c2, and v2 for an independet use of this PART III

# Formula for the amount of antibiotic (in stock concentration) required is
# c1*v1 = c2*v2
# The key for derivation of the last equation is that the amount of solute 
# does not change in the two solutions if water were to be added to the antibiotic

# c1 is the stock concentration for the antibiotic (defined in PART I)
# See https://www.addgene.org/mol-bio-reference/#antibiotics
c1 = stock_concentration  # units are (mg/mL); (Kanamycin is 50 mg/mL) (Ampicillin is 100 mg/mL)

# c2 is the final desired concentration (working concentration)
# See https://www.addgene.org/mol-bio-reference/#antibiotics
c2 = 0.05   # units are (mg/mL);  for Kanamycin is 50ug/mL; 100ug/mL for Ampicillin

# v2 is the final desired volume, in this case v_plates_total, the total volume
# of media calculated earlier
v2 = v_plates_total # units are (mL)

# v1 is the necessary volume of antibiotic in the stock concentration to be 
# present the final volume v2
v1 = (c2*v2)/c1
print('\nPART III Antibiotic in the Agar mix -----------')
print('Antibiotic volume of stock contentration: {} mL'.format(v1))
