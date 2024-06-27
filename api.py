from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/foodtrucks', methods=['GET'])
def get_foodtrucks():
    df = pd.read_csv('path/to/your/csv')
    foodtrucks = df.to_dict(orient='records')
    return jsonify(foodtrucks)

if __name__ == '__main__':
    app.run(debug=True)
