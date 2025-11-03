USE sports_odds

CREATE TABLE IF NOT EXISTS odds (
    game_id TEXT,
    sport_key TEXT,
    sport_title TEXT,
    commence_time DATETIME, 
    home_team TEXT,
    away_team TEXT,
    book_key TEXT,
    book_title TEXT,
    last_update_book DATETIME,
    market_key TEXT,
    last_update_market DATETIME,
    team_name TEXT,
    price FLOAT
);
