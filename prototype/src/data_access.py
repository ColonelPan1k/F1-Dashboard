from datetime import datetime

import sqlalchemy as sa

from db_engine import engine


def exec_qry(qry: str):
    with engine.begin() as conn:
        res = conn.execute(sa.text(qry)).all()

    return res


def get_season_schedule():
    qry = f"""
    SELECT * FROM db.races
    WHERE year = year(current_date())
    ORDER BY date ASC;
    """
    return exec_qry(qry)


def get_upcoming_event():
    qry = """
    SELECT * FROM db.races
    WHERE year = year(current_date())
    AND datediff(date, current_date()) >= 0
    LIMIT 1
    """
    return exec_qry(qry)


def get_race_results():
    qry = """
    SELECT
      db.races.name,
      grid,
      position
      points,
      forename,
      surname,
    from db.results
    join db.drivers
      on db.drivers.driverId = db.results.driverId
    join db.races.raceId = db.results.raceId
    where db.races.year = year(current_date())
    """
