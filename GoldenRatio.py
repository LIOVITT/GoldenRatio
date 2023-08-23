import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import cos, sin
import random
from PIL import Image


# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


#Base values

x = [0]
y = [0]

r = [0]

u = [1,1]

n = 1000

k = -3

pheta = (1 + 5 ** 0.5)/2


teta = [0]



# Create a sphere
theta, phi = np.mgrid[0:2.0*np.pi:100j,np.pi*1.1:np.pi/3:100j]
x = np.sin(phi) * np.cos(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(phi)



# Plot the sphere
ax.plot_surface(x, y, z, color='b', alpha=0.15)

#Make radius and teta angle values
for i in range(n):
    r.append((1/120)*(pheta**((2 * teta[i-1])/np.pi)))
    teta.append((np.pi/180)*(i+1))

teta = np.array(teta)




# Create a line on the surface of the sphere
line_phi = np.linspace(np.pi, np.pi/2, n+1)


n_d = 12
o_d = 6

view_p = 0


color = '000000'

c_n = [0,0,0,0,0,0]

for i in range(n_d):
    #Change coordinates to line
    line_y = np.sin(line_phi) * r * np.sin(teta)
    line_z = np.sin(line_phi) * r * np.cos(teta)
    line_x = (1-line_y**2-line_z**2)**(0.5)

    #Changes x, y, and z values to sphere coordinates
    alpha_0 = (np.pi/(n_d/2))*i
    line_x_d = np.cos(alpha_0) * line_x - np.sin(alpha_0) * line_y
    line_y_d = np.sin(alpha_0) * line_x + np.cos(alpha_0) * line_y
    line_z_d = line_z

    #Create random color
    for j in range(6):
       c_n[j] = random.randint(0, 15)

       c_n[j] = hex(c_n[j])
       c_n[j] = str(c_n[j]).replace('0x', '')

    color = "',".join(c_n)
    color = color.replace("',", '')


    # Plot the line
    ax.plot(line_x_d, line_y_d, line_z_d, color='#' + color)

    #Create photo to gif animation
    ax.view_init(30, (360 / n_d) * i)
    plt.savefig("photo_" + str(i) + ".png")

    for i_p in range(o_d):
        view_p = view_p + (360/n_d)/o_d
        ax.view_init(30, view_p)
        plt.savefig("photo_" + str(i) + "_" + str(i_p) + ".png")

# Set plot labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('')


# Show the plot
#plt.show()








