<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500;600&display=swap');
 

body {  
  background: #f6f8fa;
  margin: 0;
  font-family: 'Quicksand', sans-serif;
}
.faq-container {    
  max-width: 800px;
  margin: 50px auto 0 auto;
  padding: 2rem;
}
.faq-container h2 {
  margin-bottom: 50px;
  font-size: 2.5rem;
  font-weight: 600;
  text-align: center;
  color: #364f6b;
}
details { 
  background-color: #f6f8fa;
  width: 100%;
  margin-bottom: 1rem;   
  border-radius: 8px;  
  border: 1px solid #d8e0e9;
  color: #364f6b;
  position: relative;  
}
details summary {  
  font-weight: 400;
  font-size: 1.25rem;
  padding: 1rem;
  cursor: pointer;
  list-style: none;
}
details p {
  padding: 1rem;
  margin: 0 1rem 1rem 1rem;
  background: #f6f8fa;
  border-left: 2px solid #364f6b;
}

details:hover,
details[open] {
  box-shadow: 5px 5px 15px #d9d9d9;
}

details[open] {
  background: #ffffff;
}

details[open] summary {
  font-weight: 600;
}

details summary::before {
  position: absolute;
    content: "👇";    
    font-size: 1.75rem;
    top: 10px;
    right: 16px;  
}

details[open] summary::before {
  -webkit-animation: rotate 0.6s ease-in-out both;
          animation: rotate-emoji 0.6s ease-in-out both;
}

@-webkit-keyframes rotate-emoji {
  0% {
    -webkit-transform: rotate(0);
            transform: rotate(0);
  }
  100% {
    -webkit-transform: rotate(180deg);
            transform: rotate(180deg);
  }
}
</style>

<div class="faq-container">
  <h2>Contenidos</h2>
  <details open>
    <summary>Ejerció 1 Bisección</summary>
    <p>El ejercicio era pasar el programa anteriormente realizado en c++ a python.</p>
    <img src="../images/01.png" align="center"/>
  </details>

  <details>
    <summary>Ejerció 2 Secret Number</summary>
    <p>El ejercicio trata sobre adivinar el número secreto que es aleatorio.</p>
    <img src="../images/02.png" align="center"/>
  </details>
  
  <details>
    <summary>Ejerció 3 Ticket</summary>
    <p>El ejercicio es sobre pedir cierta cantidad de dinero e mostrar cuantos boletos le alcanza al usuario, pero cada ticket que compras su precio aumenta.</p>
    <img src="../images/03.png" align="center"/>
  </details>
  
  <details>
    <summary>Ejerció 4 Bubbel Sort</summary>
    <p>Realizar el método de la burbuja.</p>
    <img src="../images/04.png" align="center"/>
  </details>
  
  <details>
    <summary>Ejerció 5 Palíndromo</summary>
    <p>Imprimir si una cadena o numero es palíndromo o no (se lee de la misma forma alreves).</p>
    <img src="../images/05.png" align="center"/>
  </details>

  <details>
    <summary>Ejerció 6 Matriz aleatoria</summary>
    <p>LLenar una matriz con numeros aleatorios de n tamaño y que no se repitan.</p>
    <img src="../images/06.png" align="center"/>
  </details>



</div>
