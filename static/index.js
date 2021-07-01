const allRanges = document.querySelectorAll(".range-wrap");
let x =0
allRanges.forEach(wrap => {
  const range = wrap.querySelector(".range");
  const bubble = wrap.querySelector(".bubble");
  const engine = wrap.querySelector(".engine")
  range.addEventListener("input", () => {
    setBubble(range, bubble);
  });
   engine.range=range;
   engine.bubble=bubble;
    engine.addEventListener('change', updateValue);

  setBubble(range, bubble);
  
});

function setBubble(range, bubble) {
  const val = range.value;
  const min = range.min ? range.min : 0;
  const max = range.max ? range.max : 100;
  const newVal = Number(((val - min) * 100) / (max - min));
  let nextSibling = bubble.nextElementSibling;
  x=nextSibling.name;
  enginevalue=document.getElementById('enginevalue'+x)
  enginevalue.value=val;
  bubble.innerHTML = val;
  // Sorta magic numbers based on size of the native UI thumb
  bubble.style.left = `calc(${newVal}% + (${8 - newVal * 0.15}px))`;
}


function updateValue(e) {
  var range=e.currentTarget.range;
  range.value=e.currentTarget.value;
  const bubble=e.currentTarget.bubble;
  setBubble(range,bubble);
}

document.getElementById('engine_form').onsubmit = function (e) {
  e.preventDefault();

  fetch('/engines/create', {
      method: 'POST',
      body: JSON.stringify({
          'name': document.getElementById('enginevalue1').value
      }),
      headers: {
          'Content-Type': 'application/json'
      }
  })
  .then(function (response) {
      return response.json();
  })}