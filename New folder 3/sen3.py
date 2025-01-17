<!DOCTYPE html>
<html>
<head>
<title>User singin</title>
<style>
body {
font-family: Arial, sans-serif;
background-color: #f4f4f4;
}
.container {
max-width: 500px;
margin: 0 auto;
padding: 20px;
background-color: #fff;
border-radius: 5px;
box-shadow: 0 2px 5px #ccc;
}
h2 {
text-align: center;
color: #333;
}
.form-group {
margin: 10px 0;
}
label {
font-weight: bold;
}
input[type="email"],
input[type="password"] {
width: 100%;
padding: 10px;
margin-top: 5px;
margin-bottom: 20px;
border: 1px solid #ccc;
border-radius: 3px;
}
.btn {
background-color: #333;
color: #fff;
padding: 10px 15px;
border: none;
border-radius: 3px;
cursor: pointer;
}
</style>
</head>
<body>
<div class="container">
<h2>User Login</h2>
<form id="signin-form" method="post">
<div class="form-group">
<label for="email">email</label>
<input type="email" id="email" name="email" required />
</div>
<div class="form-group">
<label for="password">Password</label>
<input type="password" id="password" name="password" required />
</div>
<div>
<button class="btn" type="submit">Sing in</button>
<a style="cursor: pointer;" href="/signup">create new account?</a>
<br />
<a style="cursor: pointer;" href="/password-reset">forgot password?</a>
</div>
</form>
</div>
<script>