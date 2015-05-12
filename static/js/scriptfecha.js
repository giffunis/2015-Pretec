function obtenerFecha() {
    var d = new Date();
    var n = d.toLocaleString();
    document.getElementById("demo").innerHTML = n;
}
