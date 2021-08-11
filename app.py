from website import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True) # everytime a change is made, automatically will rerun the flask server