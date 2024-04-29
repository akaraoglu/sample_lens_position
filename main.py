# MIT License
# Copyright (c) 2023 [Your name or your organization]
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# All measurements must be in the same units, millimeters, feet, or inches.			
# F 	lens focal length	
# N 	aperture f-stop
# c 	circle of confusion	
# S 	focus distance (subject)
# H 	hyperfocal distance	
# dof_n 	Near distance for acceptable sharpness		
# dof_f 	Far distance for acceptable sharpness		

# Functions for calculating focus distances using Gaussian formula
def get_hyperfocal_distance(F, N, c):
    """Calculate the hyperfocal distance given the focal length, aperture, and circle of confusion."""
    assert F > 0, "Focal length must be greater than zero."
    assert N > 0, "Aperture must be greater than zero."
    assert c > 0, "Circle of confusion must be greater than zero."
    return (F**2) / (N * c) + F

def get_dof_near(F, H, S):
    """Calculate the near depth of field limit."""
    assert S < H, "Subject distance must be smaller than the hyperfocal distance."
    assert S > F, "Subject distance must be greater than the focal length."
    return (S * (H - F)) / (H + S - 2 * F)

def get_dof_far(F, H, S):
    """Calculate the far depth of field limit."""
    assert S < H, "Subject distance must be smaller than the hyperfocal distance."
    assert S > F, "Subject distance must be greater than the focal length."
    return (S * (H - F)) / (H - S)

def get_focus_distance_from_dof(dof, F, H, is_near=True):
    """Calculate focus distance from depth of field limits."""
    assert dof < H, "Depth of field limit must be smaller than the hyperfocal distance."
    assert dof > F, "Depth of field limit must be greater than the focal length."
    if is_near:
        return (dof * (H - 2 * F)) / (H - F - dof)
    return (dof * (H - 2 * F)) / (H - F + dof)

def get_lens_distance_from_focus_distance(S, F):
    """Calculate the lens distance for a given focus distance."""
    assert S > F, "Focus distance must be greater than the focal length."
    return S * F / (S - F)

def print_optical_parameters(F, N, c, S_near_limit, H, lens_distance_near_limit, lens_distance_far_limit):
    """Print the optical parameters in a user-friendly format."""
    print("Optical Parameters:")
    print("-------------------")
    print(f"Focal Length (F): {F:.3f} mm")
    print(f"Aperture (N): f/{N:.1f}")
    print(f"Circle of Confusion (c): {c:.4f} mm")
    print(f"Practical Nearest Focus Distance (S_near_limit): {S_near_limit} mm")
    print(f"Hyperfocal Distance (H): {H:.2f} mm")
    print(f"Lens Distance at Nearest Focus Limit: {lens_distance_near_limit:.2f} mm")
    print(f"Lens Distance at Hyperfocal Distance: {lens_distance_far_limit:.2f} mm")

def focus_bracketing_all_in_focus_lens_positions(F, N, c, S_near_limit, S_far_limit, H):
    """
    Calculate and print all lens positions needed to keep the entire scene from S_near_limit to S_far_limit in focus.
    
    Parameters:
    - F (float): Focal length in mm
    - N (float): Aperture f-stop
    - c (float): Circle of confusion in mm
    - S_near_limit (int): Nearest focus distance in mm
    - S_far_limit (int): Farthest focus distance in mm
    - H (float): Hyperfocal distance in mm
    """
    # Start with the nearest limit and calculate initial far DoF limit
    focus_distance_curr = S_near_limit
    dof_f = get_dof_far(F, H, focus_distance_curr)
    focus_distance_curr = get_focus_distance_from_dof(dof_f, F, H, is_near=True)
    lens_distance_curr = get_lens_distance_from_focus_distance(focus_distance_curr, F)

    print("Initial lens settings:")
    print(f"Focus Distance: {focus_distance_curr:.1f} mm, Lens Distance: {lens_distance_curr:.4f} mm")

    count = 1
    while focus_distance_curr <= S_far_limit:
        dof_f = get_dof_far(F, H, focus_distance_curr)

        # Check if the entire range is covered
        if dof_f >= S_far_limit:
            print("Complete focus range achieved.")
            break

        # Calculate the next focus distance and corresponding lens distance
        focus_distance_next = get_focus_distance_from_dof(dof_f, F, H, is_near=True)
        # Preventing over-extension beyond hyperfocal distance
        if focus_distance_next > H:
            focus_distance_next = H-1

        lens_distance_next = get_lens_distance_from_focus_distance(focus_distance_next, F)
        
        print(f"Step {count}: Focus Distance: {focus_distance_next:.1f} mm, Lens Distance: {lens_distance_next:.4f} mm")

        # Update current values
        focus_distance_curr = focus_distance_next
        lens_distance_curr = lens_distance_next
        count += 1

# Main execution block
F = 3.992  # focal length in mm
N = 1.6    # aperture f-stop
c = 0.0011 # circle of confusion in mm
H = get_hyperfocal_distance(F, N, c)  # Theoretical furthest focus distance

S_near_limit = 250  # Practical nearest focus distance in mm
S_far_limit = H   # Practical farthest focus distance in mm

lens_distance_near_limit = get_lens_distance_from_focus_distance(S_near_limit, F)
lens_distance_far_limit = get_lens_distance_from_focus_distance(H, F)

print_optical_parameters(F, N, c, S_near_limit, H, lens_distance_near_limit, lens_distance_far_limit)
focus_bracketing_all_in_focus_lens_positions(F, N, c, S_near_limit, S_far_limit, H)
