# 🎬 CHILLFLIX 🎬

**A Movie and Show app powered by [TMDb](https://www.themoviedb.org/).** \
This app is made using Django with PostgresSQL

(GIFs are down there 👇)

## Top Features 🎉
- Popular Movies and Shows
- Get details about a movie or show
- Search for Movie or Show
- Get Movies and Shows Recommendation
- Filter the movies or shows

## Environment Setup 👷‍♂️
Before setting up the project you will need to configure few things.\
First you will need to get TMDB API from [here](https://www.themoviedb.org/settings/api) \
You will need to create postgres database named `CHILLFLIX`
## Installation ⚡️
Creating Virtual Environment
```bash
python3 -m venv chillflix_env 
```
Activate the Environment
```bash
soruce chillflix_env/bin/activate 
```
Clone the project to this directory 
```bash
git clone {project url}  
```
Add .env file where there is [settings.py](./chillflix/settings.py) and add the following value

NAME | VALUE | 
--- | --- 
`TMDB_API` | Your API Key
`DJ_SECRET_KEY` | Django Secret Key(You can add something like this `xx-Secret-Key-xx`)
`DB_USER` | Database User 
`DB_PASSWORD` | Database User's Password 
<br />

Install all the Dependencies 
```bash
pip3 install -r requirements.txt  
```
Setting up the databases models
```bash
./manage.py makemigrations
./manage.py migrate
```
Setup the Initial Data (For First Run Only)
```bash
python3 initial_setup.py
``` 
Start the local server
```bash
./manage.py runserver
``` 
## Want to access admin panel? 😎
Become Super User
```bash
./manage.py createsuper user
```
## Some GIFs 👾
<img src="gifs/home.gif" alt="Home GIF"/>
<center><bold> Home Page</bold> </center>
<br />
<br />
<img src="gifs/details.gif" alt="Movie Details Page GIF"/>
<center><bold> Movie Details Page </bold> </center>
<br />
<br />
<img src="gifs/search&filter.gif" alt="Filter Page GIF"/>
<center><bold> Filter Page </bold> </center>

## Future Plans 👨‍💻

 - Changing the Frontend to React 
 - For Backend will use Django Rest API
 - Better Design
 - Push Notification
 - Movie and Show List
 - Login with Google, Github, ...

## Contributing 💁‍♂️
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.


