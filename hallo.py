from flask import Flask
app = Flask(__name__)

@app.route("/")
  def hello():
    return "Hello Nama Saya Rendi Priambodo dari mata kuliah komputasi awan 2019 IT Telkom Purwokerto"
    
if __name__== "__main__":
  app.run()
