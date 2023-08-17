import sqlite3
import pandas as pd
from sqlalchemy import Column, Integer, Float, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
# Define table presidential_polls_2016
class PresidentialPolls2016(Base):
    __tablename__ = 'presidential_polls_2016'
    id = Column(Integer, primary_key=True)
    cycle = Column(Integer)
    branch = Column(String)
    type = Column(String)
    matchup = Column(String)
    forecastdate = Column(Date)  
    state = Column(String)
    startdate = Column(Date)
    enddate = Column(Date)
    pollster = Column(String)
    grade = Column(String)
    samplesize = Column(Float)
    population = Column(String)
    poll_wt = Column(Float)
    rawpoll_clinton = Column(Float)
    rawpoll_trump = Column(Float)
    rawpoll_johnson = Column(Float)
    rawpoll_mcmullin = Column(Float)
    adjpoll_clinton = Column(Float)
    adjpoll_trump = Column(Float)
    adjpoll_johnson = Column(Float)
    adjpoll_mcmullin = Column(Float)
    multiversions = Column(String)
    url = Column(String)
    poll_id = Column(Integer)
    question_id = Column(Integer)
    createddate = Column(String)
    timestamp = Column(String)

# Define the other table classes (FavorabilityPollsRV2019 and FavorabilityPolls2023) in a similar manner

class FavorabilityPollsRV2019(Base):
    __tablename__ = 'favorability_polls_rv_2019'
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)
    pollster_id = Column(Integer)
    pollster = Column(String)
    sponsors = Column(String)
    sample_size = Column(Float)
    population = Column(String)
    methodology = Column(String)
    url = Column(String)
    politician = Column(String)
    favorable = Column(Float)
    unfavorable = Column(Float)
    very_favorable = Column(Float)
    somewhat_favorable = Column(Float)
    somewhat_unfavorable = Column(Float)
    very_unfavorable = Column(Float)

class FavorabilityPolls2023(Base):
    __tablename__ = 'favorability_polls_2023'
    id = Column(Integer, primary_key=True)
    poll_id = Column(Integer)
    pollster_id = Column(Integer)
    pollster = Column(String)
    sponsor_ids = Column(String)
    sponsors = Column(String)
    display_name = Column(String)
    pollster_rating_id = Column(Integer)
    pollster_rating_name = Column(String)
    fte_grade = Column(String)
    methodology = Column(String)
    state = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    sponsor_candidate_id = Column(String)
    sponsor_candidate = Column(String)
    sponsor_candidate_party = Column(String)
    question_id = Column(Integer)
    sample_size = Column(Integer)
    population = Column(String)
    subpopulation = Column(String)
    population_full = Column(String)
    tracking = Column(String)
    created_at = Column(String)
    notes = Column(String)
    url = Column(String)
    source = Column(String)
    internal = Column(String)
    partisan = Column(String)
    imputed_sample_size = Column(Integer)
    politician_id = Column(String)
    politician = Column(String)
    favorable = Column(Integer)
    unfavorable = Column(Integer)
    alternate_answers = Column(Integer)
    very_favorable = Column(Integer)
    somewhat_favorable = Column(Integer)
    somewhat_unfavorable = Column(Integer)
    very_unfavorable = Column(Integer)

class SQLiteManager:
    def __init__(self, database_path):
        self.database_path = database_path
        self.engine = create_engine(f"sqlite:///{self.database_path}")
        self.session = sessionmaker(bind=self.engine)()

    def create_database(self):
        Base.metadata.create_all(self.engine)

    def create_table(self):
        pass  # Table creation is handled by the mapped class definition

    def import_csv_to_table(self, csv_path, table_name):
        csv_data = pd.read_csv(csv_path)
        csv_data.to_sql(table_name, self.engine, if_exists='append', index=False)

    def execute_query(self, query):
        self.session.execute(query)
        self.session.commit()

    def close_connection(self):
        self.session.close()

# Creating database in the desired path
database_path = "../../database/Elections_db.sqlite"
manager = SQLiteManager(database_path)
manager.create_database()

# Import data for each table
presidential_polls_csv = "../../data/data-raw/csv_raw/presidential_polls_2016.csv"
favorability_polls_rv_2019_csv = "../../data/data-raw/csv_raw/favorability_polls_rv_2019.csv"
favorability_polls_2023_csv = "../../data/data-raw/csv_raw/favorability_polls_2023.csv"

manager.import_csv_to_table(presidential_polls_csv, "presidential_polls_2016")
manager.import_csv_to_table(favorability_polls_rv_2019_csv, "favorability_polls_rv_2019")
manager.import_csv_to_table(favorability_polls_2023_csv, "favorability_polls_2023")

manager.close_connection()
