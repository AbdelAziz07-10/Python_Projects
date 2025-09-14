from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

DATA = [
    ["Recipe Name", "Category", "Prep Time", "Servings", "Difficulty"],
    [
        "Chicken Biryani",
        "Main Course",
        "45 mins",
        "4",
        "Medium"
    ],
    [
        "Chocolate Cake",
        "Dessert", 
        "60 mins",
        "8",
        "Easy"
    ],
    [
        "Caesar Salad",
        "Appetizer",
        "15 mins", 
        "2",
        "Easy"
    ],
    [
        "Beef Stew",
        "Main Course",
        "120 mins",
        "6", 
        "Hard"
    ],
    [
        "Mango Lassi",
        "Beverage",
        "5 mins",
        "2",
        "Easy"
    ]
]

pdf = SimpleDocTemplate("recipes.pdf", pagesize=A4)
styles = getSampleStyleSheet()
title_style = styles["Heading1"]
title_style.alignment = 1
title = Paragraph("Recipe Collection", title_style)

style = TableStyle([
    ("BOX", (0, 0), (-1, -1), 1, colors.black),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("BACKGROUND", (0, 1), (-1, -1), colors.lightblue),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 12),
    ("FONTSIZE", (0, 1), (-1, -1), 10),
])

table = Table(DATA, style=style)
pdf.build([title, table])