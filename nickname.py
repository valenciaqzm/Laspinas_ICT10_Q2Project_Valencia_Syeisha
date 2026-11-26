from pyscript import document

nicknames = {
    "Sasha": "Sash",
    "Josua": "Jo",
    "Maria": "Mia",
    "Juan": "Juanito",
    "Alexander": "Alex",
    "Elizabeth": "Liz",
    "Katherine": "Kate",
    "Christopher": "Chris",
    "Jonathan": "Jon",
    "Samantha": "Sam"
}

def find_nickname(event):
    name = document.getElementById("name").value.strip().title()

    nickname = nicknames.get(name, "No nickname found")

    document.getElementById("result").innerHTML = f"""
    <b>Name:</b> {name}<br>
    <b>Nickname:</b> {nickname}
    """
