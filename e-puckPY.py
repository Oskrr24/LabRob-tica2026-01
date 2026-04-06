from controller import Robot

def run_robot():
    # Inicializar el robot 
    robot = Robot()
    timestep = int(robot.getBasicTimeStep())
    
    # Configurar motores 
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    
    # Variables de control 
    base_speed = 4.0
    time_step_straight = 3.2  # Segundos avanzando
    time_step_turn = 0.99481  # Tiempo para girar 90°
    time_step_S=3.2 #Tiempo para formar la S
        
        
    while robot.step(timestep) != -1:
        current_time = robot.getTime()
        
        # --- EXPERIMENTOS BÁSICOS ---
        # 1. Recto: vl=2, vr=2 | 
        #2. Curva: vl=2, vr=1 | 
        #3. Rotación: vl=1, vr=-1 
        vl = 2.0
        vr = 2.0

        # --- DESAFÍO: CUADRADO AUTOMÁTICO ---
        # Esta lógica alterna entre avanzar y girar cada ciclo de tiempo, descomentar para usar
        #cycle_time = current_time % (time_step_straight + time_step_turn)
        #if cycle_time < time_step_straight:
            #vl, vr = base_speed, base_speed   # Avanzar recto 
        #else:
            #vl, vr = base_speed, -base_speed  # Girar 90° (Rotación) 
        
        # --- FUNCIÓN DE S (VARIACIÓN ARMÓNICA) ---
        # Usamos una función seno para alternar la velocidad entre ruedas 
        #cycle_time = current_time % (time_step_straight + time_step_S)
        #desviacion = 0.5
        #if cycle_time < time_step_straight:
            #Avanzar a la derecha (vl > vr)
            #vl = base_speed + desviacion
            #vr = base_speed - desviacion
        #else: 
            #Avanzar a la izquierda (vl < vr)
            #vl = base_speed - desviacion
            #vr = base_speed + desviacion

        # Asignar velocidades a los actuadores 
        left_motor.setVelocity(vl)
        right_motor.setVelocity(vr)

if __name__ == "__main__":
    run_robot()