from transitions import Machine

#robot durumu temsili için class
class Robot:
    pass

#robot nesnesi
robot= Robot()

#states

states = ['Idle','Moving','Paused']

#durumdan duruma geçiş

transitions = [
    {'trigger' : 'start', 'source' : 'Idle','dest': 'Moving'},
    {'trigger' : 'pause', 'source' : 'Moving', 'dest': 'Paused'},
    {'trigger' : 'resume', 'source' : 'Paused', 'dest': 'Moving'},
    {'trigger' : 'stop', 'source' : 'Moving', 'dest': 'Idle'},
]

#state machine olusturma
machine = Machine(model=robot,states=states,transitions=transitions,initial='Idle')

print(f"Baslangic durumu: {robot.state}")

#robot hareket ediyor
robot.start()
print(f"Durum : {robot.state}")

# Robotu duraklatıyoruz
robot.pause()
print(f"Durum: {robot.state}")  # 'Paused'

# Robotu tekrar hareket ettiriyoruz
robot.resume()
print(f"Durum: {robot.state}")  # 'Moving'

# Robotu durduruyoruz
robot.stop()
print(f"Durum: {robot.state}")  # 'Idle'