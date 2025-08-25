# analyzer.py
color_cultural_meanings = {
    "red": {
        "western": "passion, love, danger",
        "asian": "luck, prosperity, celebration",
        "middle_east": "danger, caution, mourning"
    },
    "white": {
        "western": "purity, peace, weddings",
        "asian": "mourning, death",
        "middle_east": "purity, peace"
    },
    "black": {
        "western": "mourning, elegance, power",
        "asian": "bad luck, evil",
        "middle_east": "mourning, evil"
    },
    "blue": {
        "western": "calm, trust, sadness",
        "asian": "immortality, healing",
        "middle_east": "protection, spirituality"
    },
    "green": {
        "western": "nature, growth, envy",
        "asian": "fertility, harmony",
        "middle_east": "luck, Islam, wealth"
    },
    "yellow": {
        "western": "happiness, energy, caution",
        "asian": "royalty, respect",
        "middle_east": "hospitality, warmth"
    },
    "purple": {
        "western": "royalty, luxury, mystery",
        "asian": "wealth, nobility",
        "middle_east": "spirituality, honor"
    },
    "orange": {
        "western": "energy, enthusiasm, warmth",
        "asian": "courage, love, happiness",
        "middle_east": "protection, endurance"
    },
    "pink": {
        "western": "love, femininity, softness",
        "asian": "marriage, trust",
        "middle_east": "tenderness, affection"
    },
    "gray": {
        "western": "neutrality, formality, boredom",
        "asian": "modesty, age",
        "middle_east": "mourning, humility"
    }
}

def analyze_text(text):
    text_lower = text.lower()
    found_colors = {}

    for color, cultures in color_cultural_meanings.items():
        if color in text_lower:
            explanations = []
            for region, meaning in cultures.items():
                explanation = f"In {region.capitalize()} culture, '{color}' is associated with {meaning}."
                explanations.append(explanation)
            found_colors[color] = explanations

    if not found_colors:
        return {"message": "No color found in text."}

    return {"colors_found": found_colors}