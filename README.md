# umuganda_UATS_2025

# Project overview:
  This project is called UATS. It is being build for hundling umuganda local events.

# Tools used:
  Backend => Python + Flask
  REST and CRUD APIs => Flask REST APi for js fetch browser requests (these APIs are not yet integrated to the app but they work smoothly)
  Frontend => Flask + HTML, CSS and JS --> (will be developed using React in future)
  DB => Sqlite --> (will be migrated to PostGreSql in future)
  Other: Found in the "requirements.txt" file

# challenge addressed: 
To build an UATS system --> (Build and deploy a complete web app for Umuganda attendance and fines).
  - we tried building this thing using Flask

# How to setup this uats-2025 (locally windows 10)
 1. clone this repo.
 2. cd server
 3. python -u "run.py" or flask run
 4. head over to the favourite browser and paste the url yo got at the console (default : http://127.0.0.1:1001 )
 5. wait the system to load
 6. signup
 7. Enter every thing as propmted. Additionally, your password cant go below 5 charcters and your phone number cant exceed 10 characters. 
 8. And drill ! You are done.
 9. Every thing after the home page is more descriptive on the home page.
 10. Enjoy the digital Umuganda Attendance and Fines Tracking System.

# Seed user creaditials:
They are found in the file : "/testing_user_crediatils.txt"
These creaditials are randomly guessed, if they match as yours or a friend, just let know they are ok.

# The project skeleton is as below:
├── .gitignore
├── __init__.py
├── requirements.txt
├── server
│   ├── .env
│   ├── app
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── forms
│   │   │   └── user_forms.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── attendance.py
│   │   │   ├── chat.py
│   │   │   ├── custom_types.py
│   │   │   ├── fine.py
│   │   │   ├── notification.py
│   │   │   ├── payment.py
│   │   │   ├── sector.py
│   │   │   ├── umuganda.py
│   │   │   └── user.py
│   │   ├── routes
│   │   │   ├── __init__.py
│   │   │   ├── attendance_routes.py
│   │   │   ├── auth_routes.py
│   │   │   ├── dashboard_routes.py
│   │   │   ├── debug.py
│   │   │   ├── fine_routes.py
│   │   │   ├── main_routes.py
│   │   │   ├── payment_routes.py
│   │   │   ├── test_env.py
│   │   │   ├── test_home.py
│   │   │   ├── umuganda_routes.py
│   │   │   └── user_routes.py
│   │   ├── services
│   │   │   └── admin.py
│   │   ├── static
│   │   │   ├── css
│   │   │   │   ├── admin.css
│   │   │   │   ├── admin_v2.css
│   │   │   │   ├── auth.css
│   │   │   │   ├── base.css
│   │   │   │   ├── citizen_dashboard.css
│   │   │   │   ├── login.css
│   │   │   │   ├── signup.css
│   │   │   │   └── signup_sliding_effects.css
│   │   │   ├── img
│   │   │   │   ├── uats-preview-1.jpg
│   │   │   │   ├── uats-preview-3.jpg
│   │   │   │   └── uats-preview.jpg
│   │   │   └── js
│   │   │       ├── admin_create_umuganda.js
│   │   │       ├── admin_v2.js
│   │   │       ├── apiRequests.js
│   │   │       ├── auth.js
│   │   │       ├── citizen_dashboard.js
│   │   │       ├── flash.js
│   │   │       ├── mark_attendance.js
│   │   │       └── signup_sliding.js
│   │   └── templates
│   │       ├── app
│   │       │   ├── about.html
│   │       │   ├── contact.html
│   │       │   ├── help.html
│   │       │   └── terms.html
│   │       ├── base.html
│   │       ├── dashboard
│   │       │   ├── admin_v2.html
│   │       │   └── citizen_v2.html
│   │       ├── home.html
│   │       └── user_auth
│   │           ├── login.html
│   │           ├── signup.html
│   │           └── signup_back.html
│   ├── drop_all.py
│   ├── instance
│   │   └── uats.db
│   ├── run.py
│   ├── seed.py
│   └── utils
│       ├── __init__.py
│       └── mailing_utils.py
└── testing_user_crediatils.txt

