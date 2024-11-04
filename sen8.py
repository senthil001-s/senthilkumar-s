<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" type="text/css" href="styles.css" />
</head>
<body>
<h1>web notification code</h1>
<button id="showNotificationButton">Show Notification</button>
<script>
document.addEventListener("DOMContentLoaded", () => {
const showNotificationButton = document.getElementById("showNotificationButton"
);
if (!("Notification" in window)) {
console.log("This browser does not support system notifications.");
} else {
Notification.requestPermission().then((permission) => {
if (permission === "granted") {
showNotificationButton.addEventListener("click", () => {
showNotification(
"New Message",
"You have a new message from web browser."
); });
} });
}
function showNotification(title, message) {
const notification = new Notification(title, {
body: message,
});
notification.onclick = () => {
// Handle the notification click event (e.g., open a related page).
};
}
});
</script>
</body>
</html>