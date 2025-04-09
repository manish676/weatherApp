<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Weather Comparison App - README</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      background-color: #f4f4f4;
      margin: 0;
      padding: 40px;
      color: #333;
    }

    h1, h2, h3 {
      color: #1a73e8;
    }

    .container {
      max-width: 900px;
      margin: auto;
      background: #fff;
      padding: 30px;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }

    code, pre {
      background: #eee;
      padding: 5px 10px;
      border-radius: 5px;
      display: block;
      white-space: pre-wrap;
    }

    ul {
      list-style-type: disc;
      padding-left: 20px;
    }

    .screenshot {
      text-align: center;
      margin: 20px 0;
    }

    .footer {
      margin-top: 40px;
      font-size: 14px;
      color: #777;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>🌤️ Weather Comparison App</h1>
    <p>
      A Django-based web application to compare the weather of different cities using the OpenWeatherMap API.
    </p>

    <h2>🚀 Features</h2>
    <ul>
      <li>Real-time weather comparison</li>
      <li>OpenWeatherMap API integration</li>
      <li>Displays temperature, condition, and icons</li>
      <li>Responsive UI with custom CSS</li>
    </ul>

    <h2>📸 Screenshot</h2>
    <div class="screenshot">
      <img src="screenshot.png" alt="App Screenshot" style="width:80%; max-width:600px; border-radius: 6px;">
    </div>

    <h2>🛠️ Tech Stack</h2>
    <ul>
      <li><strong>Backend:</strong> Django (Python)</li>
      <li><strong>Frontend:</strong> HTML, CSS</li>
      <li><strong>API:</strong> OpenWeatherMap</li>
      <li><strong>Database:</strong> SQLite3</li>
    </ul>

    <h2>📂 Project Structure</h2>
    <pre>
weatherProject/
├── weatherapp/
│   ├── static/css/style.css
│   ├── templates/
│   ├── views.py
│   ├── models.py
│   └── ...
├── weatherProject/
│   ├── settings.py
│   └── ...
├── db.sqlite3
└── API_KEY
    </pre>

    <h2>⚙️ Setup Instructions</h2>
    <ol>
      <li>Clone the repository:
        <pre>git clone https://github.com/your-username/weather-app.git</pre>
      </li>
      <li>Navigate to the project folder:
        <pre>cd weather-app</pre>
      </li>
      <li>Create and activate a virtual environment:
        <pre>
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
        </pre>
      </li>
      <li>Install the dependencies:
        <pre>pip install -r requirements.txt</pre>
      </li>
      <li>Run the development server:
        <pre>python manage.py runserver</pre>
      </li>
    </ol>

    <h2>📌 To-Do</h2>
    <ul>
      <li>Add city autocomplete suggestions</li>
      <li>Show 7-day forecast</li>
      <li>Improve mobile design</li>
    </ul>

    <h2>🙌 Author</h2>
    <p><strong>Manish</strong></p>

    <div class="footer">
      <p>MIT License - Free for personal and commercial use.</p>
    </div>
  </div>
</body>
</html>
