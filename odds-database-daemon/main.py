from datetime import datetime

from dotenv import load_dotenv

import options as opts
import odds_api
import server_db


load_dotenv()


"""
TODO: get odds data for all specified options
 - read options from a config file. open and close every cycle to allow live option updating
 - the options will be the odds endpoint options
 - use the remaining number of requests and time left in the month to calculate request intervals on every cycle
 - write data as a flat table, expanded and flattened with polars
 - load the data into polars from json
 - write the table to the database
 - add triggers in the database to calculate other things like arbitrage and other table like games
 - write to database specified in .env
 - ignore .env in .gitignore
 - read api key from .env


app loop flow:
    1. open and read the options file (request_options.toml)
    2. check last request datetime,  if it exists read it and calculate whether to trigger, create it if it doesn't and triggers the request
"""


if __name__ == "__main__":
    options = opts.load_options()
    print(options)
    print("triggered", opts.check_request_trigger(options))
    # r = odds_api.fetch_odds(options)
    # print(r)
    # print(r.headers)
    # print(r.read())

    import pickle

    # with open("odds_response.pickle", "wb") as f:
    #     pickle.dump(r, f)

    with open("odds_response.pickle", "rb") as f:
        r = pickle.load(f)

    print(r)

    df = odds_api.flat_df_from_odds(r)
    print(df)
    print(df.schema)


    server_db.upsert_odds(df)
