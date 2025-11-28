#CONST PROC DO NOT EDIT 
thresholds = {
    # Nutrition value               # (operation, threshold value, points, penalty)
    "Fat_Density":                  ("<", 0.02, 2, 7),

    "Saturated_Fats_Density":       ("<", 0.01, 4, 2),

    "Monounsaturated_Fats_Density": (">", 0.01, 1, 1),
    "Polyunsaturated_Fats_Density": (">", 0.01, 1, 1),

    "Carbohydrates_Density":        ("<", 0.10, 2, 4),

    "Sugars_Density":               ("<", 0.05, 4, 4),

    "Protein_Density":              (">", 0.06, 3, 2),

    "Dietary_Fiber_Density":        (">", 0.015, 3, 2),

    "Cholesterol_Density":          ("<", 0.25, 2, 3),

    "Sodium_Density":               ("<", 0.002, 3, 3),

    "Total_Vitamin_Density":        (">", 0.30, 4, 6),
}