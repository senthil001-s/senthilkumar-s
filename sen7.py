<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>FastAPI with WebSocket and REST API</title>
</head>
<body>
<h1>FastAPI with WebSocket and REST API</h1>
<div id="data-container">
<h2>Stored Data:</h2>
<ul id="data_list"></ul>
</div>
<h2>Write Data:</h2>
<input type="text" id="data-input" placeholder="Enter data" />
<button onclick="writeToWebSocket()">Write to WebSocket</button>
<button onclick="writeToAPI()">Write to REST API</button>
<script>
const dataContainer = document.getElementById("data-container");
const ws = new WebSocket("ws://localhost:8000/ws");
const data_list = document.getElementById("data_list");
window.onload = () => {
fetch("/api/data")
.then((res) => res.json())
.then((res) => {
res?.message?.map((re) => {
data_list.innerHTML += `
<li>${re}</li> `;
});
});
};
ws.onmessage = function (event) {
dataContainer.innerHTML = <p>${event.data}</p>; };
function writeToWebSocket() {
const inputElement = document.getElementById("data-input");
const data = inputElement.value;
ws.send(data);
inputElement.value = "";
}
function writeToAPI() {
const inputElement = document.getElementById("data-input");
const data = inputElement.value;
fetch("/api/data?data=" + data, {
method: "POST",
})
.then((response) => response.json())
.then((data) => {
console.log(data.message);
inputElement.value = "";
}); }
</script>
</body>
</html>