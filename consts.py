
feature_names = [
'ID',
'Unnamed:0'
"Caloric Value",
"Fat",
"Saturated Fats",
"Monounsaturated Fats",
"Polyunsaturated Fats",
"Carbohydrates",
"Sugars",
"Protein",
"Dietary Fiber",
"Cholesterol",
"Sodium",
"Water",
"Vitamin A",
"Vitamin B1",
"Vitamin B11",
"Vitamin B12",
"Vitamin B2",
"Vitamin B3",
"Vitamin B5",
"Vitamin B6",
"Vitamin C",
"Vitamin D",
"Vitamin E",
"Vitamin K",
"Calcium",
"Copper",
"Iron",
"Magnesium",
"Manganese",
"Phosphorus",
"Potassium",
"Selenium",
"Zinc",
"Nutrition Density"
]

thresholds = {

    "Caloric_Value":        ("<", 200, 2),
    "Fat":                  ("<", 10, 3),
    "Saturated_Fats":       ("<", 3, 4),


    "Monounsaturated_Fats": (">", 1.5, 1),
    "Polyunsaturated_Fats": (">", 0.8, 1),


    "Carbohydrates":        ("<", 30, 2),
    "Sugars":               ("<", 10, 4),

    "Protein":              (">", 6, 3),
    "Dietary_Fiber":        (">", 4, 3),


    "Cholesterol":          ("<", 75, 2),
    "Sodium":               ("<", 300, 3),

    "Nutrition_Density":    (">", 150, 2)
}