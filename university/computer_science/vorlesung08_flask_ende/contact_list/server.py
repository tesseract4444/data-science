from typing import Optional, Union

from flask import Flask, render_template, Response, redirect, url_for, request

from contact import Contact

app = Flask(__name__)

# Liste in der alle Kontakte gespeichert werden. In einer echten Anwendung sollte hierfür eine Datenbank
# benutzt werden, siehe dann nächster Vorlesungsteil.
all_contacts = [
# [1, 'Vorname', 'Nachname', '123456', '555123', 'foo@bar.com']
    Contact(1, 'Vorname', 'Nachname', '123456', '555123', 'foo@bar.com'),
    Contact(2, 'Vorname2', 'Nachname2', '123456', '555123', 'foo@bar.com')
]
def insert_contact(firstname: str, lastname: str, mobile_phone: str, work_phone: str, email: str) -> int:
    # Erstellt einen neuen Kontakt mit der nächsten ID (höchste + 1) und gibt
    # die ID zurück
    newId = 0
    for contact in all_contacts:
        if contact.id > new_id:
            new_id = contact.id
    new_id += 1

    new_contact = Contact(new_id, firstname, lastname, mobile_phone, work_phone, email)
    all_contacts.append(new_contact)
    return new_id

    #Alt: new_id = max(contact.id for contact in all_contacts) + 1


@app.route('/')
def route_index() -> Response:
    # Zeigt die Startseite (index.html)
    return render_template('index.html', all_contacts=all_contacts)


@app.route('/contacts/<int:contact_id>')
def route_contact(contact_id: int) -> Union[Response, str]:
    # Zeigt den Kontakt mit der gegebenen ID an (contact.html)
    # Wenn kein Kontakt die ID hat, leite zurück auf die Startseite (route_index)
    for contact in all_contacts:
        if contact.id == contact_id: #.id ruft ID auf, _id ist die variable
            return render_template('contact.html', contact=contact)

    return redirect(url_for('route_index')) #falls kein Kontakt gefunden wird, automatische rückkehr zum start



@app.route('/contacts/createForm')
def route_create_contact_form() -> str:
    # Zeigt Formular zum Anlegen eines neuen Kontakts (newContactForm.html)
    # Das Formular soll seine Eingaben an route_create_contact schicken
    pass


@app.route('/contacts/create', methods=['POST'])
def route_create_contact() -> Response:
    # Empfängt Formulareingabe und erstellt daraus einen neuen Kontakt (mit insert_contact)
    # Zeigt danach die Detailansicht des Kontakts (route_contact)
    firstname = request.form.get('firstname', type=str) #gibt ganze formulardaten aus
    lastname = request.form.get('lastname', type=str)  # gibt ganze formulardaten aus
    mobile_phone = request.form.get('mobile_phone', type=str)  # gibt ganze formulardaten aus
    work_phone = request.form.get('work_phone', type=str)  # gibt ganze formulardaten aus
    email = request.form.get('email', type=str)  # gibt ganze formulardaten aus

    new_id = insert_contact(firstname, lastname, mobile_phone, work_phone, email)
    return redirect(url_for('route_contact', contact_id=new_id))

if __name__ == "__main__":
    app.debug = True
    app.run()
