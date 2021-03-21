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
    user_id BIGINT, 
    level TEXT, 
    song_id TEXT,
    artist_id TEXT, 
    session_id INT, 
    location TEXT, 
    user_agent TEXT);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users 
(user_id BIGINT PRIMARY KEY, 
    first_name Text, 
    last_name Text, 
    gender CHAR(1),
    level TEXT);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs
(song_id TEXT PRIMARY KEY, 
    title Text, 
    artist_id text , 
    year smallint,
    duration numeric);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists
( artist_id TEXT PRIMARY KEY, 
    name Text, 
    location text , 
    latitude numeric,
    longitude numeric);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time
(start_time timestamp PRIMARY KEY, 
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
INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s)
""")


time_table_insert = ("""
INSERT INTO time VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id, a.artist_id
    FROM songs s
    JOIN artists a
        ON a.artist_id = s.artist_id
        WHERE s.title = %s
        AND  a.name = %s
        AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]