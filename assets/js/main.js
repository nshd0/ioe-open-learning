// Minimal JS: skip-link focus fix and simple mobile nav toggle
document.addEventListener('DOMContentLoaded',function(){
  var skip=document.querySelector('.skip-link');
  if(skip){skip.addEventListener('click',function(){var t=document.getElementById('main'); if(t) t.tabIndex=-1,t.focus();})}
  var btn=document.querySelector('.nav-toggle');
  var nav=document.querySelector('.site-nav');
  if(btn&&nav){btn.addEventListener('click',function(){var open=this.getAttribute('aria-expanded')==='true';this.setAttribute('aria-expanded',(!open).toString());nav.style.display = open ? '' : 'block';});}
});
