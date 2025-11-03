import os

import httpx
import polars as pl


HOST = "https://api.the-odds-api.com/v4"


def fetch_sports(options: dict) -> httpx.Response:
    params = options.get("sports", {})
    params.update({"apiKey": os.environ.get("ODDSAPI_KEY")})

    r = httpx.get(
        HOST + "/sports",
        params=params,
    )

    return r


def fetch_odds(options: dict, sport: str = "upcoming") -> httpx.Response:
    params = options.get("odds", {})
    params.update({"apiKey": os.environ.get("ODDSAPI_KEY")})

    r = httpx.get(
        HOST + f"/sports/{sport}/odds",
        params=params,
    )

    return r


def flat_df_from_odds(res: httpx.Response) -> pl.DataFrame:
    df = (
        pl.from_dicts(res.json())
        .explode("bookmakers")
        .unnest("bookmakers")
        .rename({"key": "book_key", "last_update": "last_update_book"})
        .explode("markets")
        .unnest("markets")
        .explode("outcomes")
        .unnest("outcomes")
        .rename(
            {
                "id": "game_id",
                "title": "book_title",
                "key": "market_key",
                "last_update": "last_update_market",
                "name": "team_name",
            }
        ).with_columns(
            pl.col("commence_time").str.to_datetime("%Y-%m-%dT%H:%M:%SZ"),
            pl.col("last_update_book").str.to_datetime("%Y-%m-%dT%H:%M:%SZ"),
            pl.col("last_update_market").str.to_datetime("%Y-%m-%dT%H:%M:%SZ"),
        )
    )

    return df
