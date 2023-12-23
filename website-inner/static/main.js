/* Success Page */

function copyURL(event) {
    var div = event.currentTarget;
    var child = div.children[2];
    var copyText = child.innerText;
    navigator.clipboard.writeText(copyText);
 }