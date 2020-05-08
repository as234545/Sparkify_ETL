# DROP TABLES

songplay_table_drop = "DROP TABLE  IF EXISTS songplays;"
user_table_drop = "DROP TABLE  IF EXISTS  users;"
song_table_drop = "DROP TABLE  IF EXISTS  songs;"
artist_table_drop = "DROP TABLE  IF EXISTS artists;"
time_table_drop = "DROP TABLE  IF EXISTS  time;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE songplays(
   songplay_id          SERIAL   PRIMARY KEY     NOT NULL,
   start_time           timestamp,
   user_id              TEXT ,
   level                CHAR(50),
   song_id              TEXT ,
   artist_id            TEXT ,
   session_id           TEXT ,
   location             TEXT,
   user_agent           TEXT  
);
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS  users(
   user_id              TEXT PRIMARY KEY UNIQUE,
   first_name           TEXT    ,
   last_name            TEXT    ,
   gender               CHAR(2) ,
   level                CHAR(50)
    
);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(
   song_id             TEXT PRIMARY KEY UNIQUE,
   title               TEXT,
   artist_id           TEXT,
   year                TEXT,
   duration            float(24)
    
);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (
   artist_id          TEXT PRIMARY KEY UNIQUE,
   name               TEXT,
   location           TEXT,
   latitude           TEXT,
   longitude          TEXT
    
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS  time (
   start_time timestamp  PRIMARY KEY     NOT NULL,
   hour           TEXT,
   day            TEXT,
   week           TEXT,
   month          TEXT,
   year           TEXT,
   weekday        TEXT
   
    
);
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (start_time,user_id ,level ,song_id, artist_id ,session_id ,location, user_agent) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name,gender,level) VALUES (%s,%s,%s,%s,%s) \
ON CONFLICT (user_id) DO UPDATE SET first_name = EXCLUDED.first_name, last_name=EXCLUDED.last_name, \
                      gender = EXCLUDED.gender, level = EXCLUDED.level;
""")


song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id,year,duration) VALUES (%s,%s,%s,%s,%s) \
ON CONFLICT (song_id) DO UPDATE SET title = EXCLUDED.title, artist_id=EXCLUDED.artist_id, \
                      year = EXCLUDED.year, duration = EXCLUDED.duration;
""")



artist_table_insert = ("""INSERT INTO artists (artist_id, name, location,latitude,longitude) VALUES (%s,%s,%s,%s,%s) \
ON CONFLICT (artist_id) DO UPDATE SET name = EXCLUDED.name, location=EXCLUDED.location, \
                      latitude = EXCLUDED.latitude, longitude = EXCLUDED.longitude;
""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day,week,month,year,weekday) VALUES (%s,%s,%s,%s,%s,%s,%s) \
ON CONFLICT (start_time) DO UPDATE SET hour = EXCLUDED.hour, day=EXCLUDED.day, \
                      week = EXCLUDED.week, month = EXCLUDED.month, year = EXCLUDED.year,  weekday = EXCLUDED.weekday;
""")

# FIND SONGS

song_select = ("""SELECT artists.artist_id, songs.song_id FROM artists JOIN songs ON artists.artist_id = songs.artist_id
WHERE title = (%s) AND name = (%s) AND duration = (%s);
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]