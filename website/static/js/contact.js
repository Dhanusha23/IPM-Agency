
function sendToWhatsapp() {
    var name = document.getElementById("name").value;
    var phoneNumber = document.getElementById("phoneNumber").value;
    var email = document.getElementById("email").value;
    var message = document.getElementById("message").value;

    var phoneNumber = "9747563572"; // Replace with your WhatsApp number

    var url = "https://wa.me/" + phoneNumber + "?text="
    + "Name: " + encodeURIComponent(name) + "%0a"
    + "Phone Number: " + encodeURIComponent(phoneNumber) + "%0a"
    + "Email: " + encodeURIComponent(email) + "%0a"
    + "Message: " + encodeURIComponent(message);

    window.open(url, '_blank').focus();
}