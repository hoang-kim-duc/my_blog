function toggleOfSideBar() {
    var sb = document.getElementsByClassName("sidebar")[0];
    if (sb.style.display == "none") {
        sb.style.display = "block";
    } else {
        sb.style.display = "none";
    }
}