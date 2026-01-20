# Bean Plant Disease Knowledge Base in Python

from dataclasses import dataclass, field
from typing import List, Dict

# -------------------------------
# Define Symptoms
# -------------------------------
@dataclass(frozen=True)
class Symptom:
    name: str

# Create symptom instances
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

# -------------------------------
# Define Diseases
# -------------------------------
@dataclass
class Disease:
    name: str
    category: str
    symptoms: List[Symptom] = field(default_factory=list)

# -------------------------------
# Instantiate Diseases
# -------------------------------

# Fungal Diseases
anthracnose = Disease(
    name="Anthracnose",
    category="Fungal",
    symptoms=[brown_leaf_spots, stem_cankers, pod_rot]
)

angular_leaf_spot = Disease(
    name="Angular Leaf Spot",
    category="Fungal",
    symptoms=[angular_leaf_spots, leaf_drop]
)

rust = Disease(
    name="Rust",
    category="Fungal",
    symptoms=[rust_pustules, yellowing_leaves, leaf_drop]
)

powdery_mildew = Disease(
    name="Powdery Mildew",
    category="Fungal",
    symptoms=[powdery_coating, stunted_growth]
)

white_mold_disease = Disease(
    name="White Mold",
    category="Fungal",
    symptoms=[white_fungal_growth, flower_drop]
)

gray_mold_disease = Disease(
    name="Gray Mold",
    category="Fungal",
    symptoms=[gray_mold]
)

fusarium_wilt = Disease(
    name="Fusarium Wilt",
    category="Fungal",
    symptoms=[wilting, yellowing_leaves, root_rot]
)

pythium_root_rot = Disease(
    name="Pythium Root Rot",
    category="Fungal",
    symptoms=[root_rot]
)

rhizoctonia_root_rot = Disease(
    name="Rhizoctonia Root Rot",
    category="Fungal",
    symptoms=[root_rot]
)

charcoal_rot = Disease(
    name="Charcoal Rot",
    category="Fungal",
    symptoms=[stunted_growth, root_rot]
)

cercospora_leaf_spot = Disease(
    name="Cercospora Leaf Spot",
    category="Fungal",
    symptoms=[brown_leaf_spots]
)

# Bacterial Diseases
common_bacterial_blight = Disease(
    name="Common Bacterial Blight",
    category="Bacterial",
    symptoms=[water_soaked_lesions, yellowing_leaves, pod_discoloration]
)

halo_blight = Disease(
    name="Halo Blight",
    category="Bacterial",
    symptoms=[brown_leaf_spots, interveinal_chlorosis]
)

bacterial_soft_rot = Disease(
    name="Bacterial Soft Rot",
    category="Bacterial",
    symptoms=[pod_rot]
)

bacterial_pod_rot = Disease(
    name="Bacterial Pod Rot",
    category="Bacterial",
    symptoms=[pod_rot]
)

# Viral Diseases
bean_common_mosaic_virus = Disease(
    name="Bean Common Mosaic Virus",
    category="Viral",
    symptoms=[leaf_mosaic, leaf_curling, stunted_growth]
)

bean_yellow_mosaic_virus = Disease(
    name="Bean Yellow Mosaic Virus",
    category="Viral",
    symptoms=[leaf_mosaic, yellowing_leaves]
)

cucumber_mosaic_virus = Disease(
    name="Cucumber Mosaic Virus",
    category="Viral",
    symptoms=[leaf_mosaic, malformed_pods]
)

bean_golden_yellow_mosaic_virus = Disease(
    name="Bean Golden Yellow Mosaic Virus",
    category="Viral",
    symptoms=[yellowing_leaves, stunted_growth]
)

# Nematode Diseases
root_knot_nematode = Disease(
    name="Root Knot Nematode",
    category="Nematode",
    symptoms=[root_galls, stunted_growth]
)

lesion_nematode = Disease(
    name="Lesion Nematode",
    category="Nematode",
    symptoms=[root_rot]
)

# Abiotic/Nutritional Disorders
nitrogen_deficiency = Disease(
    name="Nitrogen Deficiency",
    category="Nutritional",
    symptoms=[yellowing_leaves, stunted_growth]
)

potassium_deficiency = Disease(
    name="Potassium Deficiency",
    category="Nutritional",
    symptoms=[scorched_leaf_edges, brittle_leaves]
)

iron_deficiency = Disease(
    name="Iron Deficiency",
    category="Nutritional",
    symptoms=[interveinal_chlorosis]
)

water_stress = Disease(
    name="Water Stress",
    category="Abiotic",
    symptoms=[wilting, leaf_drop]
)

# -------------------------------
# Aggregate all diseases
# -------------------------------
ALL_DISEASES: List[Disease] = [
    anthracnose,
    angular_leaf_spot,
    rust,
    powdery_mildew,
    white_mold_disease,
    gray_mold_disease,
    fusarium_wilt,
    pythium_root_rot,
    rhizoctonia_root_rot,
    charcoal_rot,
    cercospora_leaf_spot,
    common_bacterial_blight,
    halo_blight,
    bacterial_soft_rot,
    bacterial_pod_rot,
    bean_common_mosaic_virus,
    bean_yellow_mosaic_virus,
    cucumber_mosaic_virus,
    bean_golden_yellow_mosaic_virus,
    root_knot_nematode,
    lesion_nematode,
    nitrogen_deficiency,
    potassium_deficiency,
    iron_deficiency,
    water_stress
]

# -------------------------------
# Helper functions
# -------------------------------

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
# Example usage
# -------------------------------
if __name__ == "__main__":
    print("Symptoms of Anthracnose:", get_symptoms("Anthracnose"))
    print("Diseases causing wilting:", get_diseases_with_symptom("wilting"))
