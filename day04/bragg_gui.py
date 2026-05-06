import customtkinter as ctk
from bragg_module import calculate_d_spacing, calculate_lattice_parameter

# Set the modern appearance mode and color theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue") 

def perform_calculation():
    try:
        # Get and parse wavelength
        wl_str = entry_wl.get().strip()
        wavelength = float(wl_str) if wl_str else 1.5406
        
        # Get and parse 2theta
        two_theta = float(entry_2theta.get())
        
        # VALIDATION CHECK
        if wavelength <= 0 or two_theta <= 0:
            result_label.configure(text="Error: Values must be greater than zero.", text_color="red")
            return 
        
        # Calculate d-spacing
        theta_degrees, d_spacing = calculate_d_spacing(wavelength, two_theta)
        result_text = f"Calculated θ: {theta_degrees:.2f}°\nResult d-spacing: {d_spacing:.4f} Å"
        
        # NEW: Try to get h, k, l for the Lattice Parameter
        h_str = entry_h.get().strip()
        k_str = entry_k.get().strip()
        l_str = entry_l.get().strip()
        
        # Only calculate 'a' if they actually typed numbers into all three boxes
        if h_str and k_str and l_str:
            h = int(h_str)
            k = int(k_str)
            l = int(l_str)
            a = calculate_lattice_parameter(d_spacing, h, k, l)
            result_text += f"\nLattice parameter 'a': {a:.4f} Å"
            
        # Update UI with success
        result_label.configure(text=result_text, text_color="green")
        
    except ValueError:
        # Update UI with error
        result_label.configure(text="Error: Please enter valid numbers.", text_color="red")

# Setup main window
root = ctk.CTk()
root.title("Bragg's Law Calculator")
root.geometry("400x450") # Made the window slightly taller to fit the new boxes!
root.resizable(True, True)

# Create a padded frame inside the window
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Title Label
title_label = ctk.CTkLabel(master=frame, text="Bragg's Law", font=ctk.CTkFont(size=24, weight="bold"))
title_label.pack(pady=(15, 10))

# Wavelength Input
entry_wl = ctk.CTkEntry(master=frame, placeholder_text="Wavelength (Å) [default is 1.5406]", width=280)
entry_wl.pack(pady=5)

# 2Theta Input
entry_2theta = ctk.CTkEntry(master=frame, placeholder_text="2θ Angle (Degrees)", width=280)
entry_2theta.pack(pady=5)

# --- NEW: H, K, L Inputs ---
hkl_label = ctk.CTkLabel(master=frame, text="Optional: Miller Indices (to find 'a')", font=ctk.CTkFont(size=14))
hkl_label.pack(pady=(15, 0))

# Create a mini invisible frame just to hold the h, k, l boxes next to each other
hkl_frame = ctk.CTkFrame(master=frame, fg_color="transparent")
hkl_frame.pack(pady=5)

entry_h = ctk.CTkEntry(master=hkl_frame, placeholder_text="h", width=60)
entry_h.pack(side="left", padx=5)

entry_k = ctk.CTkEntry(master=hkl_frame, placeholder_text="k", width=60)
entry_k.pack(side="left", padx=5)

entry_l = ctk.CTkEntry(master=hkl_frame, placeholder_text="l", width=60)
entry_l.pack(side="left", padx=5)
# ---------------------------

# Calculate Button
calc_btn = ctk.CTkButton(master=frame, text="Calculate", command=perform_calculation)
calc_btn.pack(pady=20)

# Results Display
result_label = ctk.CTkLabel(master=frame, text="Results will appear here.", font=ctk.CTkFont(size=16))
result_label.pack(pady=(0, 10))

root.mainloop()