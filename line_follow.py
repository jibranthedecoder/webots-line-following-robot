"""line_follow controller."""

from controller import Robot, Motor

def sat(u,high,low):
    """Saturates u between low and high values"""
    if high < low:
        return None
    else:
        return max(min(u,high),low)

def avg_update(n,xn,avg_old):
    """Update formula for average."""
    return 1/n*(xn + (n-1)*avg_old)

def std2_update(n, xn, avg_old, std2_old):
    """Update formula for standard deviation"""
    return (n-2)/(n-1)*std2_old + 1/n*(xn - avg_old)**2

avg_old = 0 #This is an initial value for average calculation
std2_old = 0 #for standard deviation calculation

# create the Robot instance
robot = Robot()

# get the time step of the current world
timestep = int(robot.getBasicTimeStep())

# ota käyttöön moottorit ja pohja-anturit
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

gs = []
for i in range(3):
    gs.append(robot.getDevice('gs' + str(i)))
    gs[-1].enable(timestep)

sensor_scale_factor = 0.01


# Maksimi- ja perusnopeus
max_speed = 6.28
base_speed = 5.6 #Muokkaa

SP =  450*sensor_scale_factor#setpoint
PV_old = 450*sensor_scale_factor

#PD-säätimen parametrit
Kp = 7.0 #P-osan vahvistus
Kd = 0.85#D-osan vahvistus

counter = 0 #Simulointiaskeleiden laskuri
# Main loop:
while robot.step(timestep) != -1:
    counter += 1
    #Lue pohjassa olevat anturit
    g = [gsensor.getValue() for gsensor in gs]
    
    PV = g[1]*sensor_scale_factor #Keskianturi, g[0] vasen, g[2] oikea
    dPV = PV - PV_old
    
    u = Kp*(SP - PV) - Kd*dPV
    
    PV_old = PV
    
    u_right = sat(-u/2 + base_speed, max_speed, -max_speed)   
    u_left = sat(u/2 + base_speed, max_speed, -max_speed)   
    
    if abs(u_right-u_left) < u: #Yritä pakottaa nopeusero säätimen laskemaan arvoon
        if u_right < u_left:
            u_right = max(-max_speed,u_left - u)
        if u_left < u_right:
            u_left = max(-max_speed,u_right - u)

    right_motor.setVelocity(u_right)
    left_motor.setVelocity(u_left)
    
    #Keskihajonnnan ja -arvon laskenta
    mu = avg_update(counter, u, avg_old)    
    if counter > 1:
        std2 = std2_update(counter, u, avg_old, std2_old)
        std2_old = std2     
        stdev = std2**0.5
        if counter%20 == 0:
            print("u sigma:",stdev)
            print("u mean:",mu)
            print(" ")
    avg_old = mu         


            
    
    