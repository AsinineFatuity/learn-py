import cmath,math
print("Enter the value of the load in kW")
load=int(input())*1000
print("percentage of machine 1: ")
percentage_1=int(input())
percentage_2=100-percentage_1
#defining constants to be used in the program
current_machine_1=150
power_factor=0.8
sin_power_factor=0.6
three_phase_voltage=6600
line_to_line=three_phase_voltage//math.sqrt(3)
impedance_1=0.5+1j
impedance_2=0.4+1.2j
per_phase_voltage=6600*math.sqrt(3)
power_formula=math.sqrt(3)*three_phase_voltage
load_machine_1= (percentage_1*load)/100
load_machine_2= (percentage_2*load)/100
rad_to_degree=(180/math.pi)
#calculating the parameters for machine 1:
phi_1=(math.acos(load_machine_1/(power_formula*current_machine_1)))
cos_phi_1=math.cos(phi_1)
sin_phi_1=math.sin(phi_1)
total_current=load/(per_phase_voltage*power_factor)# based on lagging pf
complex_total_current=total_current*(complex(power_factor,sin_power_factor))
complex_current_1=current_machine_1*(complex(cos_phi_1,sin_phi_1))
#calculating parameters for machine 2:
complex_current_2=complex_total_current-complex_current_1
phi_2=cmath.phase(complex_current_2)
#calculating Ea:
emf_1=line_to_line+(complex_current_1*impedance_1)
line_emf_1=math.sqrt(3)*abs(emf_1)
load_angle_1=cmath.atan((cmath.phase(emf_1)))
#calculating Eb:
emf_2=line_to_line+(complex_current_2*impedance_2)
line_emf_2=math.sqrt(3)*abs(emf_2)
load_angle_2=cmath.atan((cmath.phase(emf_2)))
#displaying all the parameters:
print("phi_machine_1: "+str(phi_1*rad_to_degree))
print("phi_machine_2: "+str(phi_2*rad_to_degree))
print("total_current: "+str(total_current))
print("complex_total_current: "+str(complex_total_current))
print("complex_current_1: "+str(complex_current_1))
print("complex_current_2: "+str(complex_current_2))
print("line_voltage_machine_1: "+str(line_emf_1))
print("load_angle_machine_1: "+str(load_angle_1*rad_to_degree))
print("line_voltage_machine_2: "+str(line_emf_2))
print("load_angle_machine_2: "+str(load_angle_2*rad_to_degree))



