def fach_eingeben(faecher):
    name = input("Name des Fachs: ").strip()
    note = float(input("Note: ").strip())
    ects = int(input("ECTS: ").strip())
    faecher.append({"name": name, "note": note, "ects": ects})
    print("Fach gespeichert.")

def fach_suchen(faecher):
    suche = input("Nach welchem Fach suchen Sie? ").strip().lower()
    return [f for f in faecher if f["name"].lower() == suche]