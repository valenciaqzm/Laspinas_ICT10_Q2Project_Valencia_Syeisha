from pyscript import display, document

non_metals = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.0026),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.90),
    "Xe": ("Xenon", 54, 131.29),
    "Rn": ("Radon", 86, 222)
}

def check_element(e):
    document.getElementById('result').innerHTML = " "
    elements1 = document.getElementById('symbol').value.strip().title()

    details = non_metals.get(
        elements1,
        ("Element not found", "-", "-")
    )

    document.getElementById('result').innerHTML = f"""
    <b>Symbol:</b> {elements1}<br>
    <b>Element:</b> {details[0]}<br>
    <b>Atomic Number:</b> {details[1]}<br>
    <b>Atomic Mass:</b> {details[2]}
    """
