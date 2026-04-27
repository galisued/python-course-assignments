import customtkinter as ctk
from bragg_module import calculate_d_spacing

# Set the modern appearance mode and color theme
ctk.set_appearance_mode("System")  # Automatically matches your Mac's Dark/Light mode
ctk.set_default_color_theme("blue") 

def perform_calculation():
    try:
        # Get and parse wavelength
        wl_str = entry_wl.get().strip()
        wavelength = float(wl_str) if wl_str else 1.5406
        
        # Get and parse 2theta
        two_theta = float(entry_2theta.get())
        
        # Call shared library
        theta_degrees, d_spacing = calculate_d_spacing(wavelength, two_theta)
        
        # Update UI with success (Green text)
        result_text = f"Calculated θ: {theta_degrees:.4f}°\nResult d-spacing: {d_spacing:.4f} Å"
        result_label.configure(text=result_text, text_color="#2FA572")
        
    except ValueError:
        # Update UI with error (Red text)
        result_label.configure(text="Error: Please enter valid numbers.", text_color="#EF4444")

# Setup main window
root = ctk.CTk()
root.title("Bragg's Law Calculator")
root.geometry("350x350")
root.resizable(False, False) # Prevents the window from being resized

# Create a padded frame inside the window
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Title Label
title_label = ctk.CTkLabel(master=frame, text="Bragg's Law", font=ctk.CTkFont(size=24, weight="bold"))
title_label.pack(pady=(15, 20))

# Wavelength Input
# default is usually 1.5406 Å
entry_wl = ctk.CTkEntry(master=frame, placeholder_text="Wavelength (Å) [default is usually 1.5406 Å]", width=280)
entry_wl.pack(pady=10)

# 2Theta Input
entry_2theta = ctk.CTkEntry(master=frame, placeholder_text="2θ Angle (Degrees)", width=220)
entry_2theta.pack(pady=10)

# Calculate Button
calc_btn = ctk.CTkButton(master=frame, text="Calculate d-spacing", command=perform_calculation)
calc_btn.pack(pady=20)

# Results Display
result_label = ctk.CTkLabel(master=frame, text="Results will appear here.", font=ctk.CTkFont(size=16))
result_label.pack(pady=(5, 10))

root.mainloop()