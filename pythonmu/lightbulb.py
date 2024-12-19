#this code for learning state machine and i'm just trying 
from transitions import Machine

class LightBulb:
    pass

# Ampul nesnesi oluştur
bulb = LightBulb()

# Durumlar ve geçişler tanımla
states = ['OFF', 'ON', 'FAULT']
transitions = [
    {'trigger': 'turn_on', 'source': 'OFF', 'dest': 'ON'},
    {'trigger': 'turn_off', 'source': 'ON', 'dest': 'OFF'},
    {'trigger': 'break_bulb', 'source': ['ON', 'OFF'], 'dest': 'FAULT'},
    {'trigger': 'replace_bulb', 'source': 'FAULT', 'dest': 'OFF'}
]

# State Machine'i oluştur
machine = Machine(model=bulb, states=states, transitions=transitions, initial='OFF')

# Durumları test et
print(bulb.state)  # OFF
bulb.turn_on()
print(bulb.state)  # ON
bulb.break_bulb()
print(bulb.state)  # FAULT
bulb.replace_bulb()
print(bulb.state)  # OFF
