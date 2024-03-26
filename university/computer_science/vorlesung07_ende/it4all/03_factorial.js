function fakultaet(){
  const number = document.getElementById('number').value;
  let fact = 1;
  for (let i = 1; i <= number; i++){
    fact = fact * i
  }
  document.getElementById("result").textContent = fact;
}
