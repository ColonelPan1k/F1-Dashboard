import fastapi
from fastapi.middleware.cors import CORSMiddleware

import data_access
import upcoming

app = fastapi.FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/upcoming")
async def upcoming_event():
    return {
        "event": upcoming.process_upcoming_event_data(),
        "next_event": upcoming.calculate_upcoming_sub_event(),
    }


@app.get("/standings/{year}/{race_name}")
async def get_standings(year: int, race_name: str):
    return data_access.get_season_standings(year, race_name)


@app.get("/season")
async def season():
    return data_access.get_season_schedule()


@app.get("/season-standings/{year}/{race_name}")
async def season_standings(year: int, race_name: str):
    return data_access.get_season_standings(year, race_name)


@app.get("/table/{year}")
async def season_table(year: int):
    return data_access.get_season_table(year)


@app.get("/race/{race_id}")
async def get_race_info(race_id: int):
    ...


if __name__ == "__main__":
    app()
