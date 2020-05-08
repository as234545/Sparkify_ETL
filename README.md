# Sparkify ETL

## Introduction 
Sparkify is a music streaming app startup that wants to analyze songs and user activity of their app. 


## purpose of this project 
Sparkify doesn't have an easy way to analyze their data which is in JSON files and want to create a Postgres database with tables designed to optimize queries on song play analysis. 

### Project steps

#### 1- Create a database schema  
We choose a start schema since it is the simplest type of data mart schema. It consists of one more fact tables referencing any number of dimension tables and is more effective for handling simpler queries.   
![Sparkify_ER Digram](https://github.com/as234545/Sparkify_ETL/blob/master/Sparkify_ER.png?raw=true)


#### 2- ETL pipeline  
Python script that reads and processes JSON files and loads them into Postgres tables.  


### How to run 
First, run the `create_tables.py` to create the database schema, then run `etl.py` to populate the database with data from the JSON files. The jupyter notebook files were used for testing the code.  

#### Test 
How many songs to each artisit have ?  
`SELECT count(song_id ) , songs.artist_id, name FROM artists JOIN songs ON artists.artist_id = songs.artist_id 
GROUP BY 2,3 ORDER BY count(song_id ) DESC `

what type of account has the most users ?  
`select count(level) , level from users group by 2`

what songs has the longist duration ?  
`SELECT *  FROM songs ORDER BY duration DESC`
