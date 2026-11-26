from pyscript import document
from datetime import date

name = "Sasha Valenci"
birthday = date(2011, 1, 6)
hobbies = ["Traveling", "Cooking", "Sleeping"]
favorite_food = "Salmon Sashimi"

today = date.today()
age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

document.getElementById("creator-name").innerText = name
document.getElementById("age").innerText = f"{age} years old"
document.getElementById("birthday").innerText = f"{birthday:%B} {birthday.day}, {birthday.year}"
document.getElementById("food").innerText = favorite_food
document.getElementById("hobbies").innerHTML = "".join(f'<span class="badge badge-pink rounded-pill me-2 mb-2">{hobby}</span>' for hobby in hobbies)
