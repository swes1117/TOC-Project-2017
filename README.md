# TOC Project 2017 

### Name : 謝明軒
### ID : F74042183

### Function ： A bot which can show nba standing and famous player data
A telegram bot based on a finite state machine


### Run Locally
Using `ngrok` as a proxy.

**`ngrok` would be used in the following instruction**

```sh
ngrok http 5000
```

#### Run the sever

```sh
python3 app.py
```

## Finite State Machine
![](https://i.imgur.com/EjQsaGV.png)

## 10 state
### 01.user (intial state)
### 02.gretting (say hello and some info)
### 03.rank (ask you which nba standing you want to see east or west)
### 04.player (ask which player you want to see)
### 05.trap (wrong input when you are in greeting state go back to greeting)
### 06.showEast (show you nba east standing and go back to greeting state)
### 07.showWest (show you nba west standing and go back to greeting state)
### 08.trap2 (wrong input when you are in rank state go back to rank state)
### 09.showPlayer (show you specific player data and go back  greeting state)
### 10.trap3 (wrong input when you are in player go back to player state)

## Usage
The initial state user no matter what you input you will enter greeting state and you have two option to choose show player or show nba standing and this state maching has memory machanism 

* user
	* Just follow the respond bot tell you 
## Author
[Tim](https://github.com/swes1117)
