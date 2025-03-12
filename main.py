from dotenv import load_dotenv
from src.app import app   

load_dotenv()

app = app

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3000)