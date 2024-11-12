# wiper_animation.py

import matplotlib.pyplot as plt
import numpy as np
from wiper_mechanism import WiperMechanism

class WiperAnimation:
    def __init__(self, mechanism: WiperMechanism):
        self.mechanism = mechanism

    def animate_mechanism(self):
        # Initialize plot
        fig, ax = plt.subplots()
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)

        line, = ax.plot([], [], 'o-', lw=2)

        def update(theta):
            mech_data = self.mechanism.calculate_mechanism(theta)
            # Example mechanism movement, modify to fit actual kinematic results
            x = [0, self.mechanism.motor_bar_length * np.cos(theta)]
            y = [0, self.mechanism.motor_bar_length * np.sin(theta)]
            line.set_data(x, y)
            return line,

        ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 128), blit=True)
        plt.show()
