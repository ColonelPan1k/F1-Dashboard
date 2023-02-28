import sqlalchemy as sa

from db_engine import engine


def exec(qry: str, params={}):
    with engine.connect() as conn:
        res = conn.execute(sa.text(qry), params).all()

        return [r._asdict() for r in res]


def get_season_schedule():
    qry = """
    SELECT * FROM races
    WHERE year = year(current_date())
    ORDER BY date ASC;
    """
    return exec(qry)


def get_upcoming_event():
    qry = """
    SELECT * FROM races
    WHERE year = year(current_date())
    AND datediff(date, current_date()) >= 0
    LIMIT 1
    """
    return exec(qry)


def get_season_standings(year, race_name):
    qry = """
    SELECT
      surname,
      forename,
      f1db.constructors.name as constructor,
      coalesce(position, 'DNF') as pos,
      f1db.races.name as race_name
    FROM f1db.results
    JOIN f1db.drivers ON f1db.drivers.driverId = f1db.results.driverId
    JOIN f1db.races ON f1db.races.raceId = f1db.results.raceId
    JOIN f1db.constructors ON f1db.constructors.constructorId = f1db.results.constructorId
    WHERE year = :year
    AND f1db.races.name like :race_name
    """

    return exec(qry, dict(year=year, race_name=f"%{race_name}%"))


def get_season_table(year):
    qry = """
    SELECT
      surname,
      forename,
      sum(points) as total_points
    FROM f1db.results
    JOIN f1db.races ON f1db.races.raceId = f1db.results.raceId
    JOIN f1db.drivers ON f1db.drivers.driverId = f1db.results.driverId
    WHERE year = :year
    GROUP BY 1,2
    ORDER BY total_points DESC
    """

    return exec(qry, dict(year=year))


def get_race_info(race_id: int):
    qry = """
    SELECT
      *
    FROM f1db.races
    WHERE raceId = :race_id
    """

    return exec(qry, dict(race_id=race_id))
