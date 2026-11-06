countries = [
    {"name": "Nigeria", "capital": "Abuja", "joined":1975, "status": "member" }, 
    {"name": "Benin", "capital": "Porto-Novo", "joined":1975, "status": "member"},
    {"name": "Cape-Verde", "capital": "Paria", "joined":1977, "status": "member"},
    {"name": "Côte d'Ivoire", "capital": "Yamoussoukro", "joined":1975, "status": "member"},
    {"name": "Gambia", "capital": "Banjul", "joined":1975, "status": "member"},
    {"name": "Ghana", "capital": "Accra", "joined":1975, "status": "member"},
    {"name": "Guniea", "capital": "Conakry", "joined":1975, "status": "member"},
    {"name": "Guniea-Bissau", "capital": "Bissau", "joined":1975, "status": "member"},
    {"name": "Liberia", "capital": "Monvoria", "joined":1975, "status": "member"},
    {"name": "Senegal", "capital": "Dakar", "joined":1975, "status": "member"},
    {"name": "Sierra Leone", "capital": "Freetown", "joined":1975, "status": "member"},
    {"name": "Togo", "capital": "Lome", "joined":1975, "status": "member"},
    {"name": "Mali", "capital": "Bamako", "joined":1975, "status": "withdrew (2025)"},
    {"name": "Burkina Faso", "capital": "Ouagadougou", "joined":1975, "status": "withdrew (2025)"},
    {"name": "Niger", "capital": "Niamey", "joined":1975, "status": "withdrew (2025)"},
    ]

treaties = [
    {"year": 1975, "name": "Treaty of Lagos", "note": "Created ECOWAS, with Nigeria as a founding member"},
    {"year": 1979, "name": "Protocol on Free Movement of Persons", "note": "Set out citizen's rights to move, reside and work across member states"},
    {"year": 1990, "name": "ECOMOG intervention in Liberia", "note": "ECOWAS's first mahor regional peace operation, with Nigeria as a leading contributor"},
    {"year": 1993, "name": "Revised ECOWAS treaty", "note": "Deepened integration and strengthened to community's institutions"},
    {"year": 1975, "name": "Protocol on Democracy and Good Governance", "note": "Committed members to democratic rule and consitutional order"},

]

def make_card(country):
    return f"""
    <div class="card">
        <h2>{country['name']}</h2>
        <p><strong>Capital:</strong>{country['capital']}</p>
        <p><strong>Joined Ecowas:</strong>{country['joined']}</p>
        <p><strong>Status:</strong>{country['status']}</p>
    </div>
    """
cards = "".join(make_card(c) for c in countries)

def make_treaty(t):
    return f"""
    <div class="treaty">
        <span class="year">{t['year']}</span>
        <div>
            <h3>{t['name']}</h3>
            <p>{t['note']}</p>
        </div>
    </div>
    """

timeline = "".join(make_treaty(t) for t in treaties)

def make_treaty(t):
    return """
    <div class="treaty">
        <span class ="year">{t['year']}</span>
    <div>
    """
treaty_items = "".join(make_treaty(t) for t in treaties)

page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Naija in the Region</title>
    <link rel="stylesheet" href="style.css">
<body>
    <header>
        <h1>Naija in the Region</h1>
        <p>ECOWAS member states and Nigeria's place among them</p>
        <p> Total countries listed: {len(countries)}</p>
    </header>
    <main class="grid">
        {cards}
    </main>
  <section class="timeline">
        <h2>Key Treaties and Milestones</h2>
        {timeline}
    </section>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(page)
print("index.html generated!")
