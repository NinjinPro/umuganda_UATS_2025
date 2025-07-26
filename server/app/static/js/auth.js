const BASE_URL = 'http://localhost:5000';

function register() {
  const data = {
    username: document.getElementById('reg_username').value,
    email: document.getElementById('reg_email').value,
    phone: document.getElementById('reg_phone').value,
    password: document.getElementById('reg_password').value,
    role: document.getElementById('reg_role').value,
    village: document.getElementById('reg_village').value
  };

  fetch(`${BASE_URL}/auth/register`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data)
  })
  .then(res => res.json())
  .then(result => alert(`✅ Registered: ${JSON.stringify(result)}`))
  .catch(err => alert('❌ Error: ' + err));
}

function login() {
  const data = {
    email: document.getElementById('login_email').value,
    password: document.getElementById('login_password').value
  };

  fetch(`${BASE_URL}/auth/login`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data)
  })
  .then(res => res.json())
  .then(result => {
    if (result.access_token) {
      localStorage.setItem('token', result.access_token);
      alert('✅ Logged in successfully!');
    } else {
      alert('❌ Login failed!');
    }
  });
}

function getCurrentUser() {
  const token = localStorage.getItem('token');
  if (!token) {
    alert('⚠️ No token found. Please login first.');
    return;
  }

  fetch(`${BASE_URL}/auth/me`, {
    headers: {
      'Authorization': `Bearer ${token}`
    }
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById('user_info').innerText = JSON.stringify(data, null, 2);
  })
  .catch(err => alert('❌ Failed to fetch user info'));
}
