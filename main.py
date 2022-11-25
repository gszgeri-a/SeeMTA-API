from fastapi import FastAPI
from fastapi.params import Body
from fastapi.templating import Jinja2Templates
import requests
from bs4 import BeautifulSoup

app = FastAPI()
@app.get("/")
def main():
    page = requests.get("https://stats.see-game.com/")
    soup = BeautifulSoup(page.content, "html.parser")
    players = soup.find(class_="col-sm right").get_text(strip=True)
    return str(players).replace("online: ", "")
