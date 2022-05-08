def battery_is_ok(temperature, soc, charge_rate):
    #print ((check_tepmerature(temperature) and check_soc(soc)) and check_charge_rate(charge_rate))
    if(check_tepmerature(temperature) and check_soc(soc) and check_charge_rate(charge_rate)):
        return True
    else:
        return False 

def check_tepmerature(temperature):
    if ( 0 >temperature or temperature> 45):
        print('Temperature is out of range!')
        return False
    else:
        print("Temp is in range")
        return True
      
def check_soc(soc):
    if ( 20 > soc or soc > 80):
        print('State of Charge is out of range!')
        return False
    else:
        print("SOC in Range")
        return True
        
def check_charge_rate(charge_rate):
    if charge_rate >0.8:
        print('Charge rate is out of range!')
        return False
    else:
        print("Charge range in Range")
        return True      

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
