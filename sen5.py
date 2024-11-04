<html>
<head>
<title>FastAPI Demo</title>
<style>
body {
background-color: #f0f0f0;
text-align: center;
}
h1 {
color: #0074D9;
}
</style>
</head>
<body>
<h1>Hello, World!</h1>
<p>This is a FastAPI demo.</p>
</body>
</html> ""
return HTMLResponse(content=html_content)