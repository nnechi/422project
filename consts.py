
feature_names = [
"ID", #0
"Unnamed: 0", #1
"Caloric Value", #2
"Fat", #3
"Saturated Fats", #4
"Monounsaturated Fats", #5
"Polyunsaturated Fats", #6
"Carbohydrates", #7
"Sugars", #8
"Protein", #9
"Dietary Fiber", #10
"Cholesterol", #11
"Sodium", #12
"Water", #13
"Vitamin A", #14
"Vitamin B1", #15
"Vitamin B11", #16
"Vitamin B12", #17
"Vitamin B2", #18
"Vitamin B3", #19
"Vitamin B5", #20
"Vitamin B6", #21
"Vitamin C", #22
"Vitamin D", #23
"Vitamin E", #24
"Vitamin K", #25
"Calcium", #26
"Copper", #27
"Iron", #28
"Magnesium", #29
"Manganese", #30
"Phosphorus", #31
"Potassium", #32
"Selenium", #33
"Zinc" #34
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
}