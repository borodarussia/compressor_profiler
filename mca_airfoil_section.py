# построение сечения профиля

import numpy as np

# initial data
inlet_blade_angle = float(0.0)  # \beta_{1} (k_{1})
outlet_blade_angle = float(0.0)  # \beta_{2} (k_{2})
leading_edge_radius = float(0.0)
trailing_edge_radius = float(0.0)
chord = float(0.0)
relative_max_thickness = float(0.0)
max_thickness_position = float(0.0)
front_camber_angle = float(0.0)
radius_at_leading_edge = float(0.0)
radius_at_trailing_edge = float(0.0)
number_of_blade = int(0)
section_restagger_angle = float(0.0)
blade_restagger_angle = float(0.0)
blade_restagger_axial_axis = float(0.0)
theta_displacement = float(0.0)
axial_displacement = float(0.0)
blade_type = str("")
blade_axis_position_in_flowpath = float(0.0)

# calculation
# camberline

total_camber_angle = inlet_blade_angle - outlet_blade_angle  # \fi_{т}
back_camber_angle = total_camber_angle - front_camber_angle  # \fi_{sb}
camber_ratio = front_camber_angle / total_camber_angle  #\fi_{ss} / \fi_{т}

leading_edge_spacing = radius_at_leading_edge * np.pi * 2 / number_of_blade

supersonic_chord = leading_edge_spacing * np.sin(np.radians(
    inlet_blade_angle) - np.radians(front_camber_angle) / 2)

subsonic_chord = np.sqrt(np.power(supersonic_chord, 2) *
                         np.power(np.cos(np.radians(front_camber_angle) / 2 +
                                         np.radians(back_camber_angle) / 2), 2)
                         + np.power(chord, 2)
                         - np.power(supersonic_chord, 2)) - supersonic_chord * np.cos(np.radians(front_camber_angle) / 2 + np.radians(back_camber_angle) / 2)

if camber_ratio != 0.5:
    supersonic_radius = supersonic_chord / (2 * np.sin(np.radians(front_camber_angle) / 2))
    subsonic_radius = subsonic_chord / (2 * np.sin(np.radians(back_camber_angle) / 2))
elif camber_ratio == 0.5:
    supersonic_radius = chord / (2 * np.sin(np.radians(total_camber_angle) / 2))
    subsonic_radius = supersonic_radius
