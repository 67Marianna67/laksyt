import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/kenttä/<icao>")
def hae_lentokentta(icao):
  yhteys = sqlite3.connect("lentokentat.db")
  kursori = yhteys.cursor()
  sql = "SELECT ident, name, municipality FROM airport WHERE ident = ?"
  kursori.execute(sql, (icao.upper(),))
  tulos = kursori.fetchone()

  yhteys.close()
  if tulos:
    vastaus = {"ICAO": tulos[0], "Name": tulos[1], "Municipality": tulos[2]}
    return jsonify(vastaus)
  else:
    return jsonify({"error": "Аэропорт не найден"}), 404


if __name__ == "__main__":
  app.run(host="127.0.0.1", port=3000)