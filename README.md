# Sparkify Songs Analysis

Sparkify is a music streaming startup, and currently have songs and logs data into json files.
Their analytics team is interested in understanding what songs users are listening to but since data is in json files the don't have an easy way to query data. This project was model to attend this demand and make Sparkify analysis easier 

## Source data

The data is stored in json format and distributed in 2 datasets Songs and Logs.

### Song Dataset
Song dataset are stored in `data/song_data`, in the following layout

```javascript
{
    "num_songs": 1,
    "artist_id": "AR7G5I41187FB4CE6C",
    "artist_latitude": null,
    "artist_longitude": null,
    "artist_location": "London, England",
    "artist_name": "Adam Ant",
    "song_id": "SONHOTT12A8C13493C",
    "title": "Something Girls",
    "duration": 233.40363,
    "year": 1982
}
```

#### Logs dataset
Logs dataset are stored in `data/log_data` will contain a list of files with following layout:

```javascript
{
    "artist": null,
    "auth": "Logged In",
    "firstName": "Walter",
    "gender": "M",
    "itemInSession": 0,
    "lastName": "Frye",
    "length": null,
    "level": "free",
    "location": "San Francisco-Oakland-Hayward, CA",
    "method": "GET",
    "page": "Home",
    "registration": 1540919166796.0,
    "sessionId": 38,
    "song": null,
    "status": 200,
    "ts": 1541105830796,
    "userAgent": "\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36\"",
    "userId": "39"
}
```