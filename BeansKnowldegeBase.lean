/-
  Bean Plant Disease Knowledge Base
  Lean 4
  Purpose: Formal representation of diseases and symptoms in beans
-/

namespace BeanKB

/--------------------------------------------------
  SYMPTOMS
--------------------------------------------------/

inductive Symptom
| yellowing_leaves
| interveinal_chlorosis
| brown_leaf_spots
| angular_leaf_spots
| water_soaked_lesions
| leaf_mosaic
| leaf_curling
| leaf_drop
| wilting
| stunted_growth
| root_rot
| root_galls
| stem_cankers
| stem_lesions
| white_fungal_growth
| gray_mold
| powdery_coating
| rust_pustules
| pod_rot
| pod_discoloration
| poor_germination
| seed_rot
| flower_drop
| scorched_leaf_edges
| necrotic_veins
| brittle_leaves
| malformed_pods
deriving DecidableEq, Repr

/--------------------------------------------------
  DISEASES
--------------------------------------------------/

inductive Disease
-- Fungal diseases
| anthracnose
| angular_leaf_spot
| rust
| powdery_mildew
| white_mold
| gray_mold_disease
| fusarium_wilt
| pythium_root_rot
| rhizoctonia_root_rot
| charcoal_rot
| cercospora_leaf_spot

-- Bacterial diseases
| common_bacterial_blight
| halo_blight
| bacterial_soft_rot
| bacterial_pod_rot

-- Viral diseases
| bean_common_mosaic_virus
| bean_yellow_mosaic_virus
| cucumber_mosaic_virus
| bean_golden_yellow_mosaic_virus

-- Nematodes
| root_knot_nematode
| lesion_nematode

-- Abiotic / nutritional
| nitrogen_deficiency
| potassium_deficiency
| iron_deficiency
| water_stress
deriving DecidableEq, Repr

/--------------------------------------------------
  RELATION: DISEASE → SYMPTOM
--------------------------------------------------/

structure Causes (d : Disease) (s : Symptom) : Prop

/--------------------------------------------------
  FACTS: FUNGAL DISEASES
--------------------------------------------------/

-- Anthracnose
axiom anthracnose_leaf_spots :
  Causes Disease.anthracnose Symptom.brown_leaf_spots

axiom anthracnose_stem_cankers :
  Causes Disease.anthracnose Symptom.stem_cankers

axiom anthracnose_pod_rot :
  Causes Disease.anthracnose Symptom.pod_rot

-- Angular Leaf Spot
axiom als_angular_spots :
  Causes Disease.angular_leaf_spot Symptom.angular_leaf_spots

axiom als_leaf_drop :
  Causes Disease.angular_leaf_spot Symptom.leaf_drop

-- Rust
axiom rust_pustules_present :
  Causes Disease.rust Symptom.rust_pustules

axiom rust_yellowing :
  Causes Disease.rust Symptom.yellowing_leaves

-- Powdery Mildew
axiom powdery_mildew_coating :
  Causes Disease.powdery_mildew Symptom.powdery_coating

axiom powdery_mildew_stunting :
  Causes Disease.powdery_mildew Symptom.stunted_growth

-- White Mold
axiom white_mold_growth :
  Causes Disease.white_mold Symptom.white_fungal_growth

axiom white_mold_flower_drop :
  Causes Disease.white_mold Symptom.flower_drop

-- Gray Mold
axiom gray_mold_symptom :
  Causes Disease.gray_mold_disease Symptom.gray_mold

-- Fusarium Wilt
axiom fusarium_wilting :
  Causes Disease.fusarium_wilt Symptom.wilting

axiom fusarium_yellowing :
  Causes Disease.fusarium_wilt Symptom.yellowing_leaves

axiom fusarium_root_rot :
  Causes Disease.fusarium_wilt Symptom.root_rot

-- Root Rot Diseases
axiom pythium_root_rot_symptom :
  Causes Disease.pythium_root_rot Symptom.root_rot

axiom rhizoctonia_root_rot_symptom :
  Causes Disease.rhizoctonia_root_rot Symptom.root_rot

-- Charcoal Rot
axiom charcoal_rot_stunting :
  Causes Disease.charcoal_rot Symptom.stunted_growth

axiom charcoal_rot_root_rot :
  Causes Disease.charcoal_rot Symptom.root_rot

-- Cercospora Leaf Spot
axiom cercospora_leaf_spots :
  Causes Disease.cercospora_leaf_spot Symptom.brown_leaf_spots

/--------------------------------------------------
  FACTS: BACTERIAL DISEASES
--------------------------------------------------/

-- Common Bacterial Blight
axiom cbb_water_soaked :
  Causes Disease.common_bacterial_blight Symptom.water_soaked_lesions

axiom cbb_leaf_yellowing :
  Causes Disease.common_bacterial_blight Symptom.yellowing_leaves

axiom cbb_pod_discoloration :
  Causes Disease.common_bacterial_blight Symptom.pod_discoloration

-- Halo Blight
axiom halo_blight_spots :
  Causes Disease.halo_blight Symptom.brown_leaf_spots

axiom halo_blight_chlorosis :
  Causes Disease.halo_blight Symptom.interveinal_chlorosis

-- Bacterial Soft Rot
axiom bacterial_soft_rot_symptom :
  Causes Disease.bacterial_soft_rot Symptom.pod_rot

-- Bacterial Pod Rot
axiom bacterial_pod_rot_symptom :
  Causes Disease.bacterial_pod_rot Symptom.pod_rot

/--------------------------------------------------
  FACTS: VIRAL DISEASES
--------------------------------------------------/

-- Bean Common Mosaic Virus
axiom bcmv_mosaic :
  Causes Disease.bean_common_mosaic_virus Symptom.leaf_mosaic

axiom bcmv_leaf_curl :
  Causes Disease.bean_common_mosaic_virus Symptom.leaf_curling

axiom bcmv_stunting :
  Causes Disease.bean_common_mosaic_virus Symptom.stunted_growth

-- Bean Yellow Mosaic Virus
axiom bymv_mosaic :
  Causes Disease.bean_yellow_mosaic_virus Symptom.leaf_mosaic

axiom bymv_yellowing :
  Causes Disease.bean_yellow_mosaic_virus Symptom.yellowing_leaves

-- Cucumber Mosaic Virus
axiom cmv_mosaic :
  Causes Disease.cucumber_mosaic_virus Symptom.leaf_mosaic

axiom cmv_malformed_pods :
  Causes Disease.cucumber_mosaic_virus Symptom.malformed_pods

-- Bean Golden Yellow Mosaic Virus
axiom bgymv_yellowing :
  Causes Disease.bean_golden_yellow_mosaic_virus Symptom.yellowing_leaves

axiom bgymv_stunting :
  Causes Disease.bean_golden_yellow_mosaic_virus Symptom.stunted_growth

/--------------------------------------------------
  FACTS: NEMATODES
--------------------------------------------------/

-- Root Knot Nematode
axiom rkn_root_galls :
  Causes Disease.root_knot_nematode Symptom.root_galls

axiom rkn_stunting :
  Causes Disease.root_knot_nematode Symptom.stunted_growth

-- Lesion Nematode
axiom lesion_nematode_root_damage :
  Causes Disease.lesion_nematode Symptom.root_rot

/--------------------------------------------------
  FACTS: ABIOTIC / NUTRITIONAL
--------------------------------------------------/

-- Nitrogen Deficiency
axiom nitrogen_yellowing :
  Causes Disease.nitrogen_deficiency Symptom.yellowing_leaves

axiom nitrogen_stunting :
  Causes Disease.nitrogen_deficiency Symptom.stunted_growth

-- Potassium Deficiency
axiom potassium_scorching :
  Causes Disease.potassium_deficiency Symptom.scorched_leaf_edges

axiom potassium_brittle :
  Causes Disease.potassium_deficiency Symptom.brittle_leaves

-- Iron Deficiency
axiom iron_chlorosis :
  Causes Disease.iron_deficiency Symptom.interveinal_chlorosis

-- Water Stress
axiom water_stress_wilting :
  Causes Disease.water_stress Symptom.wilting

axiom water_stress_leaf_drop :
  Causes Disease.water_stress Symptom.leaf_drop

end BeanKB
