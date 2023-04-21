from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Connect to the MySQL database
db = mysql.connector.connect(
  host="mysql",
  user="root",
  password="password",
)

# Create the database if it doesn't exist
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS votes")

# Connect to the votes database
db = mysql.connector.connect(
  host="mysql",
  user="root",
  password="password",
  database="votes"
)
cursor = db.cursor()

# Define the index route to display the voting form
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Increment the vote count for the selected language
        language = request.form['language']
        cursor.execute(f"UPDATE vote_counts SET count = count + 1 WHERE language = '{language}'")
        db.commit()
    # Retrieve the vote counts from the database
    cursor.execute("SELECT language, count FROM vote_counts")
    rows = cursor.fetchall()
    vote_counts = {}
    for row in rows:
        vote_counts[row[0]] = row[1]
    # Render the index template with the vote counts
    return render_template('index.html', vote_counts=vote_counts)

if __name__ == '__main__':
    # Create the vote_counts table if it doesn't exist
    cursor.execute("CREATE TABLE IF NOT EXISTS vote_counts (language VARCHAR(255), count INT)")
    # Initialize the vote counts to zero if they don't exist
    cursor.execute("INSERT IGNORE INTO vote_counts (language, count) VALUES ('Python', 0), ('Shell', 0)")
    db.commit()
    # Start the web server
    app.run()
