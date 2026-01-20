/-
  Knowledge Base:
  Bean Plant Diseases and Symptoms
  Lean 4 compatible
-/

namespace BeanKnowledgeBase

/-- Symptoms observed in bean plants -/
inductive Symptom
| yellow_leaves
| brown_spots
| water_soaked_lesions
| leaf_mosaic
| leaf_curling
| wilting
| stunted_growth
| root_galls
| stem_cankers
| white_fungal_growth
| rust_pustules
| leaf_drop
| necrotic_veins
| pod_rot
| poor_germination
| powdery_coating
| interveinal_chlorosis
| scorched_leaf_edges
| flower_drop
| soft_rot
deriving DecidableEq, Repr

/-- Diseases affecting bean plants -/
inductive Disease
| anthracnose
| angular_leaf_spot
| common_bacterial_blight
| halo_blight
| bean_common_mosaic_virus
| rust
| powdery_mildew
| fusarium_wilt
| root_knot_nematode
| white_mold
| damping_off
| charcoal_rot
| cercospora_leaf_spot
| bacterial_soft_rot
| iron_deficiency
| potassium_deficiency
| water_stress
deriving DecidableEq, Repr

/--
  Relation stating that a disease causes a symptom
-/
structure Causes (d : Disease) (s : Symptom) : Prop

/-
  ===== FACTS (AXIOMS) =====
  Each axiom represents established agricultural knowledge
-/

/-- Anthracnose symptoms -/
axiom anthracnose_brown_spots :
  Causes Disease.anthracnose Symptom.brown_spots

axiom anthracnose_stem_cankers :
  Causes Disease.anthracnose Symptom.stem_cankers

axiom anthracnose_pod_rot :
  Causes Disease.anthracnose Symptom.pod_rot

/-- Angular Leaf Spot symptoms -/
axiom angular_leaf_spot_brown_spots :
  Causes Disease.angular_leaf_spot Symptom.brown_spots

axiom angular_leaf_spot_leaf_drop :
  Causes Disease.angular_leaf_spot Symptom.leaf_drop

/-- Common Bacterial Blight symptoms -/
axiom cbb_water_soaked :
  Causes Disease.common_bacterial_blight Symptom.water_soaked_lesions

axiom cbb_yellow_leaves :
  Causes Disease.common_bacterial_blight Symptom.yellow_leaves

/-- Halo Blight symptoms -/
axiom halo_blight_leaf_spots :
  Causes Disease.halo_blight Symptom.brown_spots

axiom halo_blight_yellowing :
  Causes Disease.halo_blight Symptom.yellow_leaves

/-- Bean Common Mosaic Virus symptoms -/
axiom bcmv_mosaic :
  Causes Disease.bean_common_mosaic_virus Symptom.leaf_mosaic

axiom bcmv_leaf_curl :
  Causes Disease.bean_common_mosaic_virus Symptom.leaf_curling

axiom bcmv_stunting :
  Causes Disease.bean_common_mosaic_virus Symptom.stunted_growth

/-- Rust symptoms -/
axiom rust_pustules_present :
  Causes Disease.rust Symptom.rust_pustules

axiom rust_leaf_drop :
  Causes Disease.rust Symptom.leaf_drop

/-- Powdery Mildew symptoms -/
axiom powdery_mildew_white_coating :
  Causes Disease.powdery_mildew Symptom.powdery_coating

/-- Fusarium Wilt symptoms -/
axiom fusarium_wilt_wilting :
  Causes Disease.fusarium_wilt Symptom.wilting

axiom fusarium_wilt_yellowing :
  Causes Disease.fusarium_wilt Symptom.yellow_leaves

/-- Root Knot Nematode symptoms -/
axiom rkn_root_galls :
  Causes Disease.root_knot_nematode Symptom.root_galls

axiom rkn_stunting :
  Causes Disease.root_knot_nematode Symptom.stunted_growth

/-- White Mold symptoms -/
axiom white_mold_fungal_growth :
  Causes Disease.white_mold Symptom.white_fungal_growth

axiom white_mold_flower_drop :
  Causes Disease.white_mold Symptom.flower_drop

/-- Damping-Off symptoms -/
axiom damping_off_soft_rot :
  Causes Disease.damping_off Symptom.soft_rot

axiom damping_off_poor_germination :
  Causes Disease.damping_off Symptom.poor_germination

/-- Nutrient Deficiency symptoms -/
axiom iron_deficiency_chlorosis :
  Causes Disease.iron_deficiency Symptom.interveinal_chlorosis

axiom potassium_deficiency_scorching :
  Causes Disease.potassium_deficiency Symptom.scorched_leaf_edges

/-- Water Stress symptoms -/
axiom water_stress_wilting :
  Causes Disease.water_stress Symptom.wilting

axiom water_stress_leaf_drop :
  Causes Disease.water_stress Symptom.leaf_drop

end BeanKnowledgeBase
