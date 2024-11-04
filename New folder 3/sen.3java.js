const form = document. get Element By Id("sign in-form"); form. add Event
Listener("submit", (event) => {
event. prevent Default();
fetch("/api/signin", {
method: "POST",
headers: {
"Content-Type": "application/json",
},
body: JSON.stringify({
email: form.elements.email. value,
password: form.elements. password. Value,
}),
})
.then((response) => response.json())
.then((data) => {
alert(data?.message || data?.detail);
})
.catch((error) => console.error(error));
});
</script>
</body>
</html>