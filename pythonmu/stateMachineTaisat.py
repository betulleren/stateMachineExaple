from transitions import Machine

# Robot Arm sınıfı, state machine mantığını barındırır
class RobotArm:
    pass

# Durumlar (states) listesi
states = [
    'idle',                    # Boşta (Başlangıç durumu)
    'moving_to_target',        # Hedefe doğru hareket ediyor
    'grabbing_object',         # Nesneyi kavrıyor
    'moving_to_destination',   # Nesneyi hedef noktaya taşıyor
    'releasing_object',        # Nesneyi bırakıyor
    'returning_home'           # Başlangıç noktasına dönüyor
]

# Robot kol nesnesi oluşturuluyor
robot_arm = RobotArm()

# State machine tanımlanıyor
machine = Machine(model=robot_arm, states=states, initial='idle')

# Durum geçişleri (transitions) tanımlanıyor
machine.add_transition('set_target', 'idle', 'moving_to_target')  # "idle" -> "moving_to_target"
machine.add_transition('reach_target', 'moving_to_target', 'grabbing_object')  # "moving_to_target" -> "grabbing_object"
machine.add_transition('grab_object', 'grabbing_object', 'moving_to_destination')  # "grabbing_object" -> "moving_to_destination"
machine.add_transition('reach_destination', 'moving_to_destination', 'releasing_object')  # "moving_to_destination" -> "releasing_object"
machine.add_transition('release_object', 'releasing_object', 'returning_home')  # "releasing_object" -> "returning_home"
machine.add_transition('return_home', 'returning_home', 'idle')  # "returning_home" -> "idle"

# FSM Kullanımı
print("Başlangıç durumu:", robot_arm.state)  # İlk durum: "idle"

robot_arm.set_target()  # Durum: "idle" -> "moving_to_target"
print("Yeni durum:", robot_arm.state)

robot_arm.reach_target()  # Durum: "moving_to_target" -> "grabbing_object"
print("Yeni durum:", robot_arm.state)

robot_arm.grab_object()  # Durum: "grabbing_object" -> "moving_to_destination"
print("Yeni durum:", robot_arm.state)

robot_arm.reach_destination()  # Durum: "moving_to_destination" -> "releasing_object"
print("Yeni durum:", robot_arm.state)

robot_arm.release_object()  # Durum: "releasing_object" -> "returning_home"
print("Yeni durum:", robot_arm.state)

robot_arm.return_home()  # Durum: "returning_home" -> "idle"
print("Son durum:", robot_arm.state)
