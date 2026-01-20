Bean Plant Disease Knowledge Base
Overview

The Bean Plant Disease Knowledge Base is an interactive tool designed to help farmers, agronomists, and plant enthusiasts identify possible diseases in bean plants based on observed symptoms. Built using Python and Streamlit, the application allows users to select symptoms and instantly get a list of potential diseases, their category, and related symptoms.
This tool integrates a comprehensive knowledge base of fungal, bacterial, viral, nematode, nutritional, and abiotic disorders affecting bean plants.

Features
Interactive symptom selection: Select one or multiple symptoms observed in bean plants.
Disease diagnosis: Receive a list of possible diseases matching the selected symptoms
Category display: View whether the disease is Fungal, Bacterial, Viral, Nematode, Nutritional, or Abiotic.
Symptom details: Check all symptoms associated with each disease.
Helper functions: Query the knowledge base to get diseases by symptom or symptoms by disease.
Example queries: Test the knowledge base using pre-defined queries for learning or demonstration.

Technologies Used
Python 3.x
Streamlit – for creating the interactive web interface
Dataclasses – for defining symptoms and diseases in a structured manner

Knowledge Base Structure
Symptom Class – Each symptom has a unique name.
Disease Class – Each disease contains:
name – Disease name
category – Disease type (Fungal, Bacterial, Viral, etc.)
symptoms – List of associated Symptom objects

Usage
Select one or more symptoms from the multi-select dropdown.
Click the Diagnose button.
The app will display possible diseases with:
Name
Category
Associated symptoms
Optional: Expand the Example Queries section to see sample outputs from the knowledge base.

Example
Selected Symptoms: wilting, yellowing_leaves
Possible Diseases:
Fusarium Wilt (Fungal) – wilting, yellowing_leaves, root_rot
Bean Golden Yellow Mosaic Virus (Viral) – yellowing_leaves, stunted_growth
Nitrogen Deficiency (Nutritional) – yellowing_leaves, stunted_growth


