let modal = document.getElementById("modal");
let modalWindow = document.getElementById("modal-window");
let btn = document.getElementById("modal-btn");

let modalShowStyle = "modal-container modal-show";
let modalCloseStyle = "modal-container modal-close";

btn.addEventListener('click', ()=>{
  modal.className = modalShowStyle;
});

modal.addEventListener('click', ()=>{
  modal.className = modalCloseStyle;
});

modalWindow.addEventListener('click', (e)=>{
  e.stopPropagation();
});