# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays
(songplay_id BIGINT PRIMARY KEY, 
    start_time BIGINT NOT NULL, 
    user_id BIGINT REFERENCES users (user_id), 
    level TEXT, 
    song_id TEXT REFERENCES songs (song_id),
    artist_id TEXT REFERENCES artists (artist_id), 
    session_id INT, 
    location TEXT, 
    user_agent TEXT);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users 
(user_id BIGINT CONSTRAINT user_tb PRIMARY KEY, 
    first_name Text, 
    last_name Text, 
    gender CHAR(1),
    level TEXT);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs
(song_id TEXT CONSTRAINT song_tb PRIMARY KEY, 
    title Text, 
    artist_id text , 
    year smallint,
    duration interval);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists
(artist_id TEXT CONSTRAINT artist_tb PRIMARY KEY, 
    name Text, 
    location text , 
    latitude float(5),
    longitude float(5));
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time
(start_time BIGINT PRIMARY KEY, 
    hour smallint, 
    day smallint, 
    week smallint,
    month smallint,
    year smallint,
    weekday text
    );
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""
INSERT INTO songs 
    (song_id, title, artist_id, year, duration) 
    VALUES 
    (%s, %s, %s, %s, %s) 
ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO songs VALUES (%s, %s, %s, %s, %s)
""")


time_table_insert = ("""
INSERT INTO songs VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]