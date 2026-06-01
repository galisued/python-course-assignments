import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Import your existing, tested business logic!
from material_filter_PV import fetch_materials_data, filter_solar_candidates

# --- Page Setup ---
st.set_page_config(page_title="PV Material Screener", page_icon="☀️", layout="wide")

st.title("☀️ Photovoltaic Material Screener")
st.markdown("""
This tool queries the Materials Project database to discover stable material candidates 
for photovoltaics or photocatalysis based on user-defined elements and band gap constraints.
""")

# --- Sidebar Controls ---
st.sidebar.header("Search Parameters")

# It's good practice to hide API keys in web apps!
api_key = st.sidebar.text_input("Materials Project API Key", type="password")

# Get elements as a comma-separated string, then convert to a list
elements_str = st.sidebar.text_input("Elements (comma separated)", value="Ti, O")
elements = [e.strip() for e in elements_str.split(",") if e.strip()]

min_bg = st.sidebar.number_input("Min Band Gap (eV)", value=1.5, step=0.1)
max_bg = st.sidebar.number_input("Max Band Gap (eV)", value=3.0, step=0.1)

# --- Main App Logic ---
if st.sidebar.button("Search Candidates"):
    if not api_key:
        st.sidebar.error("Please provide an API key to continue.")
    elif not elements:
        st.sidebar.error("Please provide at least one element.")
    else:
        # Use a spinner to show the app is working while waiting for the API
        with st.spinner(f"Querying Materials Project for {', '.join(elements)}..."):
            try:
                # 1. Fetch raw data using your business logic
                raw_df = fetch_materials_data(api_key, elements)
                
                if raw_df.empty:
                    st.warning("No materials found containing those elements.")
                else:
                    # 2. Filter data using your tested business logic
                    candidates = filter_solar_candidates(raw_df, min_bg, max_bg)
                    
                    if candidates.empty:
                        st.warning("No thermodynamically stable candidates found within that band gap range.")
                    else:
                        st.success(f"Successfully found {len(candidates)} promising candidates!")
                        
                        # --- REMOVED COLUMN LAYOUT --- 
                        
                        # 1. Show the table first
                        st.subheader("Top Candidates Data")
                        # By passing 'candidates' directly, it shows all columns from the database
                        st.dataframe(
                            candidates, 
                            use_container_width=True,
                            hide_index=True
                        )
                        
                        # Add a visual divider line
                        st.divider() 
                            
                        # 2. Show the graph underneath
                        st.subheader("Stability vs. Band Gap")
                        
                        # Made the graph slightly wider (10, 6) since it now spans the whole page
                        fig, ax = plt.subplots(figsize=(10, 6)) 
                        scatter = ax.scatter(
                            candidates['Band_Gap_eV'], 
                            candidates['Formation_Energy'], 
                            c=candidates['Energy_Above_Hull'],
                            cmap='viridis', 
                            alpha=0.8, 
                            edgecolors='w', 
                            s=100
                        )
                        
                        cbar = fig.colorbar(scatter, ax=ax)
                        cbar.set_label('Energy Above Hull (eV/atom)')
                        
                        ax.set_title(f"Material Screener: {'-'.join(elements)} Compounds")
                        ax.set_xlabel('Band Gap (eV)')
                        ax.set_ylabel('Formation Energy (eV/atom)')
                        ax.grid(True, linestyle='--', alpha=0.6)
                        
                        st.pyplot(fig)
                            
            except Exception as e:
                st.error(f"An error occurred: {e}")