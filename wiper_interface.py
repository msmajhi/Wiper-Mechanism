# wiper_interface.py

from wiper_mechanism import WiperMechanism
from wiper_animation import WiperAnimation

def display_wiper_output(omega, motor_bar_length, coupler_bar_length, output_bar_length, base_bar_length):
    # Initialize mechanism with user input
    mechanism = WiperMechanism(
        omega=omega,
        motor_bar_length=motor_bar_length,
        coupler_bar_length=coupler_bar_length,
        output_bar_length=output_bar_length,
        base_bar_length=base_bar_length
    )

    # Calculate mechanism output
    result = mechanism.calculate_mechanism(theta=0)  # Adjust theta as needed

    print(f"Wiper Simulation Output:")
    print(f"Delta Angle (δ): {result['delta_angle']}º")
    print(f"Wiper Bar Length: {result['wiper_length']} m")
    print(f"Area Wiped: {result['area_wiped']:.2f} m²")
    print(f"Speed: {result['speed']:.2f} m/s")
    print(f"|Net Acceleration|: {result['tangential_acceleration']:.2f} m/s²")
    print(f"|ac| (Centripetal): {result['centripetal_acceleration']:.2f} m/s²")
    print(f"|at| (Tangential): {result['tangential_acceleration']:.2f} m/s²")

    # Animate mechanism
    animation = WiperAnimation(mechanism)
    animation.animate_mechanism()
