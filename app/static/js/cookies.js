// Cookie Consent Logic
document.addEventListener("DOMContentLoaded", function () {
    // Check if the user has already accepted cookies
    if (!localStorage.getItem("cookiesAccepted")) {
        document.getElementById("cookieConsent").style.display = "block";
    }

    // Handle accept button click
    document.getElementById("acceptCookies").addEventListener("click", function () {
        localStorage.setItem("cookiesAccepted", "true");
        document.getElementById("cookieConsent").style.display = "none";
    });
});
