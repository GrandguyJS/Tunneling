/* Success Page */

function copyURL() {
    var copyText = document.getElementById("copyText");
    navigator.clipboard.writeText(copyText.innerText);
 }