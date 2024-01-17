from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['number']
        email = request.form['email']

        user_data = {
            'name': [name],
            'number': [number],
            'email': [email]
        }

        sub_df = pd.DataFrame(user_data, index=[0])

        try:
            # Read the CSV file only once here
            df = pd.read_csv('cafeLeads - leads.csv')
            updated_data = pd.concat([df, sub_df], ignore_index=True)
            updated_data.to_csv('cafeLeads - leads.csv', index=False)
            print(name, number, email)  # Indicate successful save
        except Exception as e:
            print(f"Error saving data: {e}")  # Log any errors

    return render_template('index.html')

@app.route('/password')
def render_password_page():
    return render_template('password.html')

if __name__ == '__main__':
    app.run(debug=True)
