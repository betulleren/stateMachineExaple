from transitions import Machine

class LineFollower:
    def __init__(self):
        # Durumları doğru şekilde tanımla
        self.machine = Machine(model=self, states=['on_line', 'left_of_line', 'right_of_line'], initial='on_line')

        # Geçişleri doğru şekilde tanımla
        self.machine.add_transition('move_forward', 'on_line', 'on_line', after='perform_move_forward')
        self.machine.add_transition('turn_right', 'left_of_line', 'on_line', after='perform_turn_right')
        self.machine.add_transition('turn_left', 'right_of_line', 'on_line', after='perform_turn_left')
        self.machine.add_transition('move_left', 'on_line', 'left_of_line', after='perform_move_left')
        self.machine.add_transition('move_right', 'on_line', 'right_of_line', after='perform_move_right')

    # Durum geçişi sonrası yapılacak işlemler
    def perform_move_forward(self):
        print("Çizgi üzerinde. İleri gidiyor...")

    def perform_turn_right(self):
        print("Çizgiden sola kaydı. Sağa dön...")

    def perform_turn_left(self):
        print("Çizgiden sağa kaydı. Sola dön...")

    def perform_move_left(self):
        print("Çizgiden sola kaydım. Sola dönüyorum...")

    def perform_move_right(self):
        print("Çizgiden sağa kaydım. Sağa dönüyorum...")

    # Sensör verisi simülasyonu
    def read_sensors(self):
        # Sensör verisi simülasyonu (örnek veri)
        return 'on_line'  # Burada 'on_line', 'left', veya 'right' döndürülebilir

    # Durum geçişlerini güncelleme
    def update(self):
        sensor_data = self.read_sensors()
        print(f"Sensör verisi: {sensor_data}")
        
        if sensor_data == 'on_line':
            self.move_forward()
        elif sensor_data == 'left':
            self.turn_right()
        elif sensor_data == 'right':
            self.turn_left()

# Ana program
def main():
    line_follower = LineFollower()
    
    # 10 adımda aracı test et
    for _ in range(10):
        line_follower.update()

if __name__ == "__main__":
    main()
