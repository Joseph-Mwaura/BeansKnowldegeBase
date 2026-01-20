# final_streamlit_app.py
import streamlit as st
from dataclasses import dataclass, field
from typing import List

# -------------------------------
# Symptom and Disease Classes
# -------------------------------
@dataclass(frozen=True)
class Symptom:
    name: str

@dataclass
class Disease:
    name: str
    category: str
    symptoms: List[Symptom] = field(default_factory=list)

# -------------------------------
# Define Symptoms
# -------------------------------
yellowing_leaves = Symptom("yellowing_leaves")
interveinal_chlorosis = Symptom("interveinal_chlorosis")
brown_leaf_spots = Symptom("brown_leaf_spots")
angular_leaf_spots = Symptom("angular_leaf_spots")
water_soaked_lesions = Symptom("water_soaked_lesions")
leaf_mosaic = Symptom("leaf_mosaic")
leaf_curling = Symptom("leaf_curling")
leaf_drop = Symptom("leaf_drop")
wilting = Symptom("wilting")
stunted_growth = Symptom("stunted_growth")
root_rot = Symptom("root_rot")
root_galls = Symptom("root_galls")
stem_cankers = Symptom("stem_cankers")
stem_lesions = Symptom("stem_lesions")
white_fungal_growth = Symptom("white_fungal_growth")
gray_mold = Symptom("gray_mold")
powdery_coating = Symptom("powdery_coating")
rust_pustules = Symptom("rust_pustules")
pod_rot = Symptom("pod_rot")
pod_discoloration = Symptom("pod_discoloration")
poor_germination = Symptom("poor_germination")
seed_rot = Symptom("seed_rot")
flower_drop = Symptom("flower_drop")
scorched_leaf_edges = Symptom("scorched_leaf_edges")
necrotic_veins = Symptom("necrotic_veins")
brittle_leaves = Symptom("brittle_leaves")
malformed_pods = Symptom("malformed_pods")

ALL_SYMPTOMS = [
    yellowing_leaves, interveinal_chlorosis, brown_leaf_spots,
    angular_leaf_spots, water_soaked_lesions, leaf_mosaic,
    leaf_curling, leaf_drop, wilting, stunted_growth, root_rot,
    root_galls, stem_cankers, stem_lesions, white_fungal_growth,
    gray_mold, powdery_coating, rust_pustules, pod_rot,
    pod_discoloration, poor_germination, seed_rot, flower_drop,
    scorched_leaf_edges, necrotic_veins, brittle_leaves, malformed_pods
]

# -------------------------------
# Define Diseases
# -------------------------------
ALL_DISEASES = [
    # Fungal
    Disease("Anthracnose", "Fungal", [brown_leaf_spots, stem_cankers, pod_rot]),
    Disease("Angular Leaf Spot", "Fungal", [angular_leaf_spots, leaf_drop]),
    Disease("Rust", "Fungal", [rust_pustules, yellowing_leaves, leaf_drop]),
    Disease("Powdery Mildew", "Fungal", [powdery_coating, stunted_growth]),
    Disease("White Mold", "Fungal", [white_fungal_growth, flower_drop]),
    Disease("Gray Mold", "Fungal", [gray_mold]),
    Disease("Fusarium Wilt", "Fungal", [wilting, yellowing_leaves, root_rot]),
    Disease("Pythium Root Rot", "Fungal", [root_rot]),
    Disease("Rhizoctonia Root Rot", "Fungal", [root_rot]),
    Disease("Charcoal Rot", "Fungal", [stunted_growth, root_rot]),
    Disease("Cercospora Leaf Spot", "Fungal", [brown_leaf_spots]),
    # Bacterial
    Disease("Common Bacterial Blight", "Bacterial", [water_soaked_lesions, yellowing_leaves, pod_discoloration]),
    Disease("Halo Blight", "Bacterial", [brown_leaf_spots, interveinal_chlorosis]),
    Disease("Bacterial Soft Rot", "Bacterial", [pod_rot]),
    Disease("Bacterial Pod Rot", "Bacterial", [pod_rot]),
    # Viral
    Disease("Bean Common Mosaic Virus", "Viral", [leaf_mosaic, leaf_curling, stunted_growth]),
    Disease("Bean Yellow Mosaic Virus", "Viral", [leaf_mosaic, yellowing_leaves]),
    Disease("Cucumber Mosaic Virus", "Viral", [leaf_mosaic, malformed_pods]),
    Disease("Bean Golden Yellow Mosaic Virus", "Viral", [yellowing_leaves, stunted_growth]),
    # Nematode
    Disease("Root Knot Nematode", "Nematode", [root_galls, stunted_growth]),
    Disease("Lesion Nematode", "Nematode", [root_rot]),
    # Nutritional / Abiotic
    Disease("Nitrogen Deficiency", "Nutritional", [yellowing_leaves, stunted_growth]),
    Disease("Potassium Deficiency", "Nutritional", [scorched_leaf_edges, brittle_leaves]),
    Disease("Iron Deficiency", "Nutritional", [interveinal_chlorosis]),
    Disease("Water Stress", "Abiotic", [wilting, leaf_drop])
]

# -------------------------------
# Helper functions
# -------------------------------
def diagnose(symptoms_selected: List[str]) -> List[Disease]:
    """Return diseases that have at least one matching symptom"""
    results = []
    for disease in ALL_DISEASES:
        disease_symptom_names = [s.name for s in disease.symptoms]
        if any(s in disease_symptom_names for s in symptoms_selected):
            results.append(disease)
    return results

def get_symptoms(disease_name: str) -> List[str]:
    """Return symptoms of a disease by name"""
    for d in ALL_DISEASES:
        if d.name.lower() == disease_name.lower():
            return [s.name for s in d.symptoms]
    return []

def get_diseases_with_symptom(symptom_name: str) -> List[str]:
    """Return diseases that cause a given symptom"""
    result = []
    for d in ALL_DISEASES:
        for s in d.symptoms:
            if s.name.lower() == symptom_name.lower():
                result.append(d.name)
    return result

# -------------------------------
# Streamlit App
# -------------------------------
st.set_page_config(page_title="Bean Disease Diagnostic Tool", page_icon="🌱")

st.title("🌱 Bean Plant Disease Diagnostic Tool")
st.write(
    "Select the symptoms you observe in your bean plant. "
    "This tool will suggest possible diseases."
)

# Multi-select symptoms
symptom_options = [s.name for s in ALL_SYMPTOMS]
selected_symptoms = st.multiselect("Select observed symptoms:", symptom_options)

if st.button("Diagnose"):
    if not selected_symptoms:
        st.warning("Please select at least one symptom!")
    else:
        matched_diseases = diagnose(selected_symptoms)
        if matched_diseases:
            st.success(f"Found {len(matched_diseases)} possible disease(s):")
            for disease in matched_diseases:
                st.write(f"**{disease.name}** ({disease.category})")
                st.write("Symptoms:", ", ".join([s.name for s in disease.symptoms]))
                st.write("---")
        else:
            st.info("No diseases matched the selected symptoms. Please review your selection.")

# Optional: Example usage section (from second file)
with st.expander("Example Queries"):
    st.write("Symptoms of Anthracnose:", ", ".join(get_symptoms("Anthracnose")))
    st.write("Diseases causing wilting:", ", ".join(get_diseases_with_symptom("wilting")))
