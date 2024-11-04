<!DOCTYPE html>
<html>
<head>
<title>
</title>
</head>
<body>
<h1> welcome to the home page </h1>
</body>
</html> '''

<!DOCTYPE html>
<html>
<head>
<title>Login Page</title>
</head>
<body>
<h1>Login</h1>
<form id="loginForm">
<input type="text" id="username" placeholder="Username" />
<input type="password" id="password" placeholder="Password" />
<button type="submit">Login</button>
</form>
<p id="message"></p>
<script>
document
.getElementById("loginForm")
.addEventListener("submit", function (event) {
event.preventDefault();
const username = document.getElementById("username").value;
const password = document.getElementById("password").value;

fetch("/login", { method: "POST",
body: JSON.stringify({ username, password }),
headers: { "Content-Type": "application/json",
}, })
.then((response) => response.json())
.then((data) => {
if (data.success) {
window.location.href = "/home?token=" + data?.token;
} else {
document.getElementById("message").textContent = "Invalid credentials"; }
}); });
</script>
</body>
</html>