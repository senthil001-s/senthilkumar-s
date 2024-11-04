const form = document.getElementById("registration-form");
form.addEventListener("submit", (event) => {
event.preventDefault();
fetch("/api/signup", {
method: "POST",
headers: {"Content-Type": "application/json",},
body: JSON.stringify({
email: form.elements.email.value,
password: form.elements.password.value,
}),
})
.then((response) => response.json())
.then((data) => {alert(data?.message || data?.detail);}
.catch((error) => console.error(error));
});
</script>
</body>
</html>