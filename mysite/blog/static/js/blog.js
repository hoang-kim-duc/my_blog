function toggleOfSideBar() {
    var sb = document.getElementsByClassName("sidebar")[0];
    var a = document.getElementsByClassName("show");
    if (a.length == 0) {
        sb.style.display = "block";
    } else {
        sb.style.display = "none";
    }
}