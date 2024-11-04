<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>FastAPI with WebSocket and REST API</title>
</head>
<body>
<h1>FastAPI with WebSocket and REST API</h1>
<div id="data-container"></div>
<script>
const dataContainer = document.getElementById("data-container");
const ws = new WebSocket("ws://localhost:8000/ws");
ws.onmessage = function (event) {
dataContainer.innerHTML = <p>${event.data}</p>;
};
function sendData() {
const inputElement = document.getElementById("data-input");
const data = inputElement.value;
ws.send(data); }
function getRESTAPI() {
fetch("/api/data", {
method: "GET", })
.then((response) => response.json())
.then((data) => {
alert(data?.data || data?.detail); })
.catch((error) => console.error(error)); }
</script>
<input
type="text"
id="data-input"
placeholder="Enter data"
onkeyup="sendData()" />
<button onclick="getRESTAPI()">get REST Api</button>
</body>
</html>