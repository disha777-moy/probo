
from flask import Flask, request, render_template_string
import csv
from datetime import datetime

app = Flask(__name__)

# Website design
style = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Poppins:wght@300;400;600;700&display=swap');

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    background: #080808;
    color: white;
    font-family: 'Poppins', sans-serif;
    text-align: center;
}

header {
    padding: 25px;
    color: #ff3030;
    font-family: 'Anton', Impact, sans-serif;
    font-size: 65px;
    letter-spacing: 8px;
    text-shadow: 3px 3px 0 #700000, 0 0 25px #ff0000;
}

.container {
    max-width: 600px;
    margin: 50px auto;
    padding: 35px;
    background: #171717;
    border: 1px solid #9e1717;
    border-radius: 15px;
    box-shadow: 0 0 25px #4d0000;
}

h1 {
    color: #ff3030;
    font-size: 35px;
}

p {
    color: #cccccc;
}

input, textarea {
    width: 100%;
    padding: 14px;
    margin: 12px 0;
    background: #292929;
    border: 1px solid #555;
    border-radius: 7px;
    color: white;
    font-size: 15px;
    font-family: Poppins, sans-serif;
}

textarea {
    height: 120px;
    resize: vertical;
}

button, .btn {
    display: inline-block;
    background: #d71920;
    color: white;
    padding: 14px 30px;
    border: none;
    border-radius: 7px;
    font-size: 17px;
    font-weight: bold;
    cursor: pointer;
    text-decoration: none;
    margin-top: 15px;
}

button:hover, .btn:hover {
    background: #ff3030;
    box-shadow: 0 0 15px red;
}

footer {
    color: #888;
    margin-top: 50px;
    padding: 20px;
}

</style>
"""

# PAGE 1: Welcome page
home = """
<!DOCTYPE html>
<html>
<head>
<title>PROBODIX</title>
{{ style|safe }}
</head>
<body>

<header>PROBODIX</header>

<div class="container">
    <h1>WELCOME TO PROBODIX</h1>

    <p>Your Printer. Our Responsibility.</p>

    <p>Printer Repair | Toner | Ink | Accessories</p>

    <a href="/repair" class="btn">REQUEST PRINTER REPAIR</a>
</div>

<footer>© 2026 PROBODIX</footer>

</body>
</html>
"""

# PAGE 2: Repair request form
repair = """
<!DOCTYPE html>
<html>
<head>
<title>Repair Request - PROBODIX</title>
{{ style|safe }}
</head>
<body>

<header>PROBODIX</header>

<div class="container">

    <h1>PRINTER REPAIR REQUEST</h1>

    <p>Tell us about your printer problem.</p>

    <form action="/success" method="POST">

        <input type="text"
        name="customer"
        placeholder="Customer Name"
        required>

        <input type="tel"
        name="phone"
        placeholder="Phone Number"
        pattern="[0-9+() -]{7,20}"
        required>

        <input type="text"
        name="printer"
        placeholder="Printer Model (HP, Canon, Epson...)"
        required>

        <textarea name="problem"
        placeholder="Describe your printer problem..."
        required></textarea>

        <button type="submit">SUBMIT REQUEST</button>

    </form>

</div>

<footer>PROBODIX - We are here to help!</footer>

</body>
</html>
"""

# PAGE 3: Confirmation page
success = """
<!DOCTYPE html>
<html>
<head>
<title>Thank You - PROBODIX</title>
{{ style|safe }}
</head>
<body>

<header>PROBODIX</header>

<div class="container">

    <h1>REQUEST RECEIVED!</h1>

    <h2 style="color:#ff3030;">
        No worries!
    </h2>

    <p style="font-size:22px;">
        PROBODIX will take care!
    </p>

    <p>Thank you for trusting us.</p>

    <a href="/exit" class="btn">EXIT WEBSITE</a>

</div>

<footer>© 2026 PROBODIX</footer>

</body>
</html>
"""

# PAGE 4: Exit page
exit_page = """
<!DOCTYPE html>
<html>
<head>
<title>Goodbye - PROBODIX</title>
{{ style|safe }}
</head>
<body>
<header>PROBODIX</header>
<div class="container">
    <h1>THANK YOU!</h1>
    <p>Thank you for visiting PROBODIX.</p>
    <p>You can now close this browser tab.</p>
</div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(home, style=style)


@app.route("/repair")
def repair_page():
    return render_template_string(repair, style=style)


@app.route("/success", methods=["POST"])
def submit_request():

    customer = request.form["customer"]
    phone = request.form["phone"]
    printer = request.form["printer"]
    problem = request.form["problem"]

    # Save customer requests in a CSV file
    with open("repair_requests.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            customer,
            phone,
            printer,
            problem
        ])

    return render_template_string(success, style=style)


@app.route("/exit")
def exit_website():
    return render_template_string(exit_page, style=style)


if __name__ == "__main__":
    app.run(debug=True)
