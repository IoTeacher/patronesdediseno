


// A la hora de seleccionar la interfaz
var GUI:String = "clara"; // u "oscura";

// A la hora de crear un botón
if(GUI == "clara"){
new BotonClaro();
}else if(GUI == "oscura"){
new BotonOscuro();
}

// A la hora de crear una ventana
if(GUI == "clara"){
new VentanaClara();
}else if(GUI == "oscura"){
new VentanaOscura();
}

// A la hora de seleccionar la interfaz
var GUI:InterfazGrafica = new InterfazClara(); // o new InterfazOscura();

// A la hora de crear un botón
GUI.crearBoton();

// A la hora de crear una ventana
GUI.crearVentana()
