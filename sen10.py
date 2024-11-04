<!DOCTYPE html>
<html>
<head>
<title>Follow Users</title>
<style>
body {
font-family: Arial, sans-serif;
text-align: center;
background-color: #f2f2f2;
}
h1 {
color: #333; }
#userList 
{
max-width: 400px;
margin: 0 auto;
padding: 20px;
background-color: #fff;
border: 1px solid #ccc;
border-radius: 5px;
box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
display: flex;
flex-direction: column;
gap: 16px;
}
a {
cursor: pointer;
padding: 16px;
font-size: 20px;
color: #333;
text-decoration: none;
}
</style>
</head>
<body>
<h1 id="header">user :</h1>
<div>
<span id="followers">followers : </span>
<br />
<span id="following">following : </span>
</div>
<ul id="userList">
<!-- User data will be displayed here -->
</ul>
<script>
const header = document.getElementById("header");
const userList = document.getElementById("userList");
const followErs = document.getElementById("followers");
const followIng = document.getElementById("following");
let currentUser = "";
window.onload = () => {
currentUser =
window.location.search.slice(1).split("=")[0] == "user" &&
window.location.search.slice(1).split("=")[1];
header.innerHTML += currentUser;

fetchUsers();
};
// Fetch and display user data
function fetchUsers() {
fetch("/users")
.then((res) => res.json())
.then((res) => {
let userId = undefined;
Object.keys(res).forEach((i) => {
if (res[i].username == currentUser) {
userId = res[i]?.id;
followErs.innerHTML += res[i].followers.length;
followIng.innerHTML += res[i].following.length;
}
});
Object.keys(res).forEach((i) => {
if (res[i].username != currentUser) {
let followers = res[userId]?.following?.filter((a) => a == i);
userList.innerHTML += `
<a href="/?user=${res[i]?.username}">
<span>${res[i].username}</span>
${
followers?.length > 0
? followers.map(
(a) => <button onclick=UnfollowUser(${userId},${i})>unfollow</button>`
): <button onclick=followUser(${userId},${i})>follow</button>
}
</a> `;
} });
}); }

async function followUser(userId, followed_user_id) {
    const response = await fetch(/follow/${userId}/${followed_user_id}, {
    method: "POST",
    });
    if (response.ok) {
    alert("You are now following this user.");
    } else {
    alert("Failed to follow the user.");
    }
    window.location.reload(); }
    // Follow a user
    async function UnfollowUser(userId, followed_user_id) {
    const response = await fetch(
    /unfollow/${userId}/${followed_user_id},
    {
    method: "POST",
    }
    );
    if (response.ok) {
    alert("You are now following this user.");
    } else {
    alert("Failed to follow the user.");
    }
    window.location.reload();
    }
    </script>
    </body>
    </html>