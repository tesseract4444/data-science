function passwordStrength(){
  let pw = document.getElementById('password').value;
  let nam1 = document.getElementById('vorname').value;
  let nam2 = document.getElementById('nachname').value;
  let err = document.getElementById('errors');

  if (pw === 'passwort' || pw ==='Passwort' || pw==='12345678'){
    err.textContent = 'Zu einfach';
  }else if (pw === nam1 || pw === nam2) {
    err.textContent = 'Niemals den eigenen Namen als Passwort verwenden!!!';
  } else if (pw.length < 8){
    err.textContent = 'Zu kurz';
  }
  else {
    err.textContent = 'Passwort Ok'
  }
}
