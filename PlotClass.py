import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d


# Surface Definitions
def calcR(angle, x=4, y=6):
    return np.sqrt((x * y) / (x * np.cos(angle) ** 2 + y * np.sin(angle) ** 2))


def stretch_mesh(r, theta):
    return [r[i] * calcR(theta[i][0]) for i in range(len(r))]


class Plot:

    def Waves(self, amplitude=.25, point_density=.05):
        lw = 5
        # Creates Mesh
        x = np.arange(-lw, lw, point_density)
        y = np.arange(-lw, lw, point_density)
        x, y = np.meshgrid(x, y)

        # Sets equation for surface
        z = amplitude * np.cos(x) * np.sin(y)

        # Limits
        plt.xlim(-lw, lw)
        plt.ylim(-lw, lw)
        ax.set_zlim(-.25, 1)

        # Sets title
        plt.title("A*cos(x)sin(y)", fontsize=10)
        plt.suptitle("Sine and Cosine Waves", fontsize=18)

        ax.plot_surface(x, y, z, cmap='plasma')
        plt.show()

    def Cone(self, a=1, b=1, point_density=.25):
        # Polar Mesh Grid
        r = np.linspace(-5, 5, int(100 * point_density))
        theta = np.linspace(0, 1 * np.pi, int(100 * point_density))
        r, theta = np.meshgrid(r, theta)
        # Transform to Cartesian
        x = r * np.sin(theta)
        y = r * np.cos(theta)

        # Sets equation for surface
        z = np.sqrt(a * x ** 2 + b * y ** 2)

        # Limits
        plt.xlim(-5, 5)
        plt.ylim(-5, 5)
        ax.set_zlim(0, 5)

        # Sets title
        plt.title("sqrt(ax^2 + by^2)", fontsize=10)
        plt.suptitle("Cone", fontsize=18)

        ax.plot_surface(x, y, z, cmap='plasma')
        plt.show()

    def Hyperboloid(self, a=1, b=1, c=1, point_density=.4):
        # Polar Mesh Grid
        r = np.linspace(-5, 5, int(100 * point_density))
        theta = np.linspace(0, 1 * np.pi, int(100 * point_density))
        r, theta = np.meshgrid(r, theta)

        # Transform to Cartesian
        x = r * np.sin(theta)
        y = r * np.cos(theta)

        # Sets equation for surface
        z = (c * np.sqrt((a ** 2) * (b ** 2 + y ** 2) + (b ** 2) * (x ** 2))) / (a * b) - 1

        # Limits
        plt.xlim(-5, 5)
        plt.ylim(-5, 5)
        ax.set_zlim(0, 5)

        # Sets title
        plt.title("(c * np.sqrt((a^2)(b^2 + y^2) + (b^2)(x^2))) / (ab) - 1", fontsize=10)
        plt.suptitle("Hyperboloid", fontsize=18)

        ax.plot_surface(x, y, z, cmap='magma')
        plt.show()

    def mobius(self, radius=5, point_density=.25):
        # Polar Mesh Grid
        r = np.linspace(-5, 5, int(100 * point_density))
        theta = np.linspace(0, 1 * np.pi, int(100 * point_density))
        r, theta = np.meshgrid(r, theta)

        # Transform to Cartesian
        x = r * np.sin(theta)
        y = r * np.cos(theta)
        R = radius

        # Sets equation for surface
        z = (R * x + x ** 2 + y ** 2 + np.sqrt(
            (R ** 2) * (x ** 2) + x ** 4 + 2 * R * x ** 3 + 2 * R * x * y ** 2 + (x ** 2) * y ** 2 + (y ** 2 * R ** 2)))

        # Limits
        plt.xlim(-R, R)
        plt.ylim(-R, R)
        ax.set_zlim(-25, 25)
        z = np.clip(z, -20, 20)

        # Sets title
        plt.title("sin(10(x^2+y^2))/10", fontsize=10)
        plt.suptitle("Ripple", fontsize=18)

        ax.plot_surface(x, y, z, cmap='magma')
        plt.show()

    def Ripple(self, point_density=1):
        # Creates Mesh
        x = np.arange(-1, 1, .01)
        y = np.arange(-1, 1, .01)
        x, y = np.meshgrid(x, y)

        # Sets equation for surface
        z = np.sin(10 * ((x ** 2) + (y ** 2))) / 10

        # Limits
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)
        ax.set_zlim(-.1, .5)

        # Sets title
        plt.title("sin(10(x^2+y^2))/10", fontsize=10)
        plt.suptitle("Ripple", fontsize=18)

        ax.plot_surface(x, y, z, cmap='plasma')
        plt.show()

    def Pyramid(self, point_density=1):
        # Creates Mesh
        x = np.arange(-1, 1, .05)
        y = np.arange(-1, 1, .05)
        x, y = np.meshgrid(x, y)

        # Sets equation for surface
        z = 1 - abs(x + y) - abs(y - x)

        # Limits
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)
        ax.set_zlim(-1, 1)

        # Sets title
        plt.title("1-abs(x+y)-abs(y-x)", fontsize=10)
        plt.suptitle("Pyramid", fontsize=18)

        ax.plot_surface(x, y, z, cmap='magma')
        plt.show()

    def Close(self):
        plt.close()


# Sets graph to 3d
ax = plt.axes(projection="3d")

# Creates Plot Object from Plot class
Plot = Plot()

# To view another graph, shape can be replaced with Waves, Pyramid, Ripple, Cone, Hyperboloid!
Plot.Ripple()

# Displays the Graph
plt.show()
