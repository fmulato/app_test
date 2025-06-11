# 🧠 Student Query Web App

This is a simple web application developed using **Flask** and **SQLite**, designed to display student data stored in a local database. 
It was deployed and tested using **Replit** and **Render**, enabling access over a public network.

## 🌐 Overview

The application allows users to:
- Click a button on the homepage
- Trigger a query to the `students` table in a SQLite database
- Display the results in a formatted HTML table

## 🛠️ Technologies Used

- Python (Flask)
- HTML (Jinja2 templating)
- SQLite
- Bootstrap 5 (CDN)
- Replit / Render (deployment)

- ## Deployment
- The deployment of this application was tested on Replit and Render, two cloud platforms that allow hosting and accessing web applications over the public internet. These platforms were used to make the application accessible outside the local machine, simulating a production-like environment for testing.
- A QR code was generated to provide quick and easy access to the deployed application. This allows users to scan the code using their mobile devices and immediately open the app in their browser, facilitating testing and demonstration over a public network.

  ![Link](qrcode_its_test_render.png)
---

## 🔄 App Flow Diagram

```text
         +------------+
         |  User      |
         |  (Browser) |
         +------------+
               |
               v
     +---------------------+
     |   Flask App Route   |  <-- app.py (@app.route)
     |        "/"          |
     +---------------------+
               |
        [POST Request]
               |
               v
     +----------------------+
     |   get_data()         |  <-- Connects to SQLite DB
     |   SELECT * FROM ...  |
     +----------------------+
               |
         [Returns Data]
               |
               v
     +----------------------+
     | Render HTML Template |
     |  (index.html) with   |
     |      student data    |
     +----------------------+
               |
               v
         +------------+
         |  User sees |
         |   table    |
         +------------+

