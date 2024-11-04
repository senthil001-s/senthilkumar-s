const form document.getElementById("signin-form"); 
form.addEventListener("submit", (event) => 1
event.preventDefault();
fetch("/api/signin", (method: "POST", headers: ["Content-Type": "application/json", ).
body: JSON.stringify({} 
email: form.elements.email.value,
password: form.elements.password.value, 1).
})
.then((response) => response.json())
.then((data) => 1
alert(data?.message || data?.detail);
))
catch((error) => console.error(error));
10:
</script>
</body>
</html>