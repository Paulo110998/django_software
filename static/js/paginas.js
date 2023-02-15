
   let menu = document.querySelector('#menu-btn');
   let navbar = document.querySelector('.navbar');
   
   menu.onclick = () =>{
       menu.classList.toggle('fa-times');
       navbar.classList.toggle('active');
   }
   
   window.onscroll = () =>{
       menu.classList.remove('fa-times');
       navbar.classList.remove('active');
   }
   
   ///////////////////////
   let loginForm = document.querySelector('.login-form')
   
   document.querySelector('#login-btn').onclick = () =>{
       loginForm.classList.toggle('active');
       navbar.classList.remove('active');
       searchForm.classList.remove('active');
   
       let menu = document.querySelector('#menu-btn');
   let navbar = document.querySelector('.navbar');
   
   menu.onclick = () =>{
       menu.classList.toggle('fa-times');
       navbar.classList.toggle('active');
   }
   
   window.onscroll = () =>{
       menu.classList.remove('fa-times');
       navbar.classList.remove('active');
   }
   }
   
