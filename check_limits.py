
def battery_is_ok(temperature, soc, charge_rate):
    check_tepmerature(temperature)
    check_soc(soc)
    check_charge_rate(charge_rate)

def check_tepmerature(temperature):
    if ( 0 >temperature > 45):
        print('Temperature is out of range!')
        return False
    else:
        return True
      
def check_soc(soc):
    if ( 20 > soc > 80):
        print('State of Charge is out of range!')
        return False
    else:
        return True
        
def check_charge_rate(charge_rate):
    if charge_rate >0.8:
        print('Charge rate is out of range!')
        return False
    else:
        return True
        

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
