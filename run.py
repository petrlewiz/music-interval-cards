from app import create_app

#This file is only used to run the app locally and not for production use with Render

app = create_app()

if __name__ == "__main__":
    app.run(debug=False)