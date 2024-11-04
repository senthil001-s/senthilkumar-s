<!DOCTYPE html>
<html>
<head>
<title>Subscription and Friends Manager</title>
<style>
body {
font-family: Arial, sans-serif;
margin: 20px;
}
h1 {
text-align: center;
}
h2 {
margin-top: 20px;
}
form {
margin: 10px;
}
button {
padding: 5px 10px;
background-color: #3498db;
color: #fff;
border: none;
cursor: pointer;
}
button:hover {
background-color: #2980b9;
}
</style>
</head>
<body>
<h1>Subscription Manager</h1>
<h2>Subscriptions</h2>
<div id="subscription-list"></div>
<h2>Friends</h2>
<div id="friend-list"></div>
<h2>Add Subscription</h2>
<form id="subscription-form">
<label for="user_id">User ID:</label>
<input type="number" id="user_id" name="user_id" required />
<label for="content">Content:</label>
<input type="text" id="content" name="content" required />
<button type="submit">Add</button>
</form>
<script>
const subscriptionForm = document.getElementById("subscription-form");
const subscriptionList = document.getElementById("subscription-list");
const friendList = document.getElementById("friend-list");
subscriptionForm.addEventListener("submit", async (e) => {
e.preventDefault();
const user_id = document.getElementById("user_id").value;
const content = document.getElementById("content").value;
const response = await fetch("/subscriptions/", {
method: "POST",
body: JSON.stringify({ user_id: user_id, content: content }),
headers: { "Content-Type": "application/json" },
});
const subscription = await response.json();
addSubscriptionToList(subscription);
});
async function displaySubscriptions() {
const response = await fetch("/subscriptions/");
const subscriptions = await response.json();
subscriptions.forEach(addSubscriptionToList);
}
function addSubscriptionToList(subscription) {
const listItem = document.createElement("div");
listItem.textContent = User ID: ${subscription.user_id}, Content: ${subscription.content};
subscriptionList.appendChild(listItem);
}
displaySubscriptions();
</script>
</body>
</html>