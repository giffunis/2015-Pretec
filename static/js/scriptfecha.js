function obtenerFecha() {
    var d = new Date();
    var n = d.toLocaleString();
    alert(n);
    document.getElementById("id_fecha").innerHTML = n;
}
