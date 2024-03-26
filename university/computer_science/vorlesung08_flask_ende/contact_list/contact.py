from dataclasses import dataclass
from typing import Optional, Tuple

# Dataclass für Kontakte.
# mit @dataclass können Klassen, die einfach Werte speichern sollen, leichter definiert werden
# Erstellen eines Kontakts mit `Contact(id, vorname, nachname, mobilnr, arbeitsnr, email)`
@dataclass() #@dataclass nicht in Klausur!!!
class Contact:
    id: int
    firstname: str
    lastname: str
    mobile_phone: Optional[str]
    work_phone: Optional[str]
    email: Optional[str]
