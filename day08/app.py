import streamlit as st
import pandas as pd
import plotly.express as px

# Importing your ORIGINAL, untouched business logic!
from material_filter_PV import fetch_materials_data, filter_solar_candidates

st.set_page_config(page_title="PV Material Screener", page_icon="☀️", layout="wide")

st.title("☀️ Photovoltaic Material Screener")
st.markdown("""
This tool queries the Materials Project database to discover stable material candidates 
for photovoltaics or photocatalysis based on user-defined elements and band gap constraints.
""")

st.sidebar.header("Search Parameters")
api_key = st.sidebar.text_input("Materials Project API Key", type="password")

elements_str = st.sidebar.text_input("Elements (comma separated)", value="Ti, O")
elements = [e.strip() for e in elements_str.split(",") if e.strip()]

min_bg = st.sidebar.number_input("Min Band Gap (eV)", value=1.5, step=0.1)
max_bg = st.sidebar.number_input("Max Band Gap (eV)", value=3.0, step=0.1)

if st.sidebar.button("Search Candidates", type="primary"):
    if not api_key:
        st.sidebar.error("Please provide an API key to continue.")
    elif not elements:
        st.sidebar.error("Please provide at least one element.")
    else:
        with st.spinner(f"Querying Materials Project for {', '.join(elements)}..."):
            try:
                raw_df = fetch_materials_data(api_key, elements)
                
                if raw_df.empty:
                    st.warning("No materials found containing those elements.")
                else:
                    # Using the ORIGINAL 3 arguments
                    candidates = filter_solar_candidates(raw_df, min_bg, max_bg)
                    
                    if candidates.empty:
                        st.warning("No thermodynamically stable candidates found within that band gap range.")
                    else:
                        candidates = candidates.round({
                            'Band_Gap_eV': 3,
                            'Formation_Energy': 3,
                            'Energy_Above_Hull': 3
                        })
                        
                        st.metric(label="Promising Candidates Found", value=len(candidates))
                        st.divider()
                        
                        st.subheader("Top Candidates Data")
                        st.dataframe(
                            candidates, 
                            use_container_width=True,
                            hide_index=True
                        )
                        
                        st.divider()
                        
                        st.subheader("Stability vs. Band Gap")
                        fig = px.scatter(
                            candidates,
                            x='Band_Gap_eV',
                            y='Formation_Energy',
                            color='Energy_Above_Hull',
                            hover_data=['Formula'], 
                            labels={
                                'Band_Gap_eV': 'Band Gap (eV)',
                                'Formation_Energy': 'Formation Energy (eV/atom)',
                                'Energy_Above_Hull': 'Energy Above Hull'
                            },
                            color_continuous_scale='Viridis',
                            title=f"Stability vs. Band Gap for {'-'.join(elements)}"
                        )
                        
                        fig.update_traces(marker=dict(size=10, line=dict(width=1, color='DarkSlateGrey')))
                        
                        st.plotly_chart(fig, use_container_width=True)
                            
            except Exception as e:
                st.error(f"An error occurred: {e}")