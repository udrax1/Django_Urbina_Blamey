//reloj
function mueveReloj(){
  momentoActual = new Date()
  hora = momentoActual.getHours()
  minuto = momentoActual.getMinutes()
  segundo = momentoActual.getSeconds()
  horaImprimible = hora + " : " + minuto + " : " + segundo
  document.form_reloj.reloj.value = horaImprimible
  
  setTimeout("mueveReloj()",1000)
}
function mailpage(){
  mail_str ="mailto:mypetsfriends@hotmail.com?subject=Asunto: ";
  mail_str +="&body= Saludos, My Pets Friends escribo para...";
 
  location.href= mail_str;
  }

