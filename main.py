from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template for rendering with Bootstrap
template = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>ReverseString.com</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #f8f9fa;
        }
        .container {
            margin-top: 50px;
        }
        .card {
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .card-header {
            background-color: #007bff;
            color: white;
            font-size: 24px;
            text-align: center;
        }
        .card-body {
            padding: 30px;
        }
        .btn-primary {
            background-color: #007bff;
            border: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <div class="card-header">
                ReverseString.com
            </div>
            <div class="card-body">
                <h5 class="card-title">Welcome to Reverse String Magic!</h5>
                <form method="post" action="/reverse">
                    <div class="form-group">
                        <input type="text" class="form-control" name="input_string" placeholder="Enter a string">
                    </div>
                    <button type="submit" class="btn btn-primary">Reverse</button>
                </form>
                {% if reversed_string is not none %}
                <div class="alert alert-success mt-3" role="alert">
                    Reversed String: {{ reversed_string }}
                </div>
                {% endif %}
            </div>
        </div>
    </div>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(template, reversed_string=None)


@app.route("/reverse", methods=["POST"])
def reverse_string():
    input_string = request.form["input_string"]
    reversed_string = input_string[::-1]
    return render_template_string(template, reversed_string=reversed_string)


if __name__ == "__main__":
    app.run(debug=True)
