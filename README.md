# udm_arduino_control

Dans ce package nous allons voir comment interfacer ROS et pyfirmata afin de pouvoir controler une carte arduino.

# Installation

Pour installer ce noeud il faut le cloner dans le dossier src de votre catkin workspace (catkin_ws)

```sh
cd catkin_ws/src
git clone https://github.com/Kramoth/udm_arduino_control.git
catkin build
cd ..
source devel/setup.bash
sudo apt-get install curl
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install pyfirmata
```

# source

Dans le dossier source il y a le script hello_firmata.py ou se trouve l'objet arduino_control qui nous permet de controler la carte arduino.

avant de pour tester ce script, il faut d'abord determiner le port serie sur lequel la carte arduino est connectee. Pour ce faire, brancher la carte arduino, ouvrir l'IDE Arduino, puis dans Tools>Port noter le numero de port de l'arduino (i.e. : /dev/ttyACM0)

Ensuite ouvrir le sketch standard firmata dans l'IDE File>Examples>Firmata>StandardFirmata televerser le code vers la carte Arduino.

Pour lancer hello_firmata.py en supposant que le port serie soit /dev/ttyUSB0. Ouvrir un terminal et se deplacer dans le dossier source

```sh
python hello_firmata.py /dev/ttyUSB0
```
Normalement, la LED embarquee de l'arduino devrait clignoter.


# Execution

## simple server
Ouvrir un terminal puis lancer le roscore

Ouvrir deux terminaux et sourcer le devel/setup.bash dans chaque terminal
Dans un terminal lancer le serveur
```sh
rosrun udm_arduino_control arduino_simple_service.py _port:=/dev/ttyUSB0
```
Dans l'autre terminal

Pour allumer la LED
```sh
rosservice call /arduino_simple_server "data: true"
```
Pour eteindre la LED
```sh
rosservice call /arduino_simple_server "data: false"
```
## custom server
Ouvrir un terminal puis lancer le roscore

Ouvrir deux terminaux et sourcer le devel/setup.bash dans chaque terminal
Dans un terminal lancer le serveur
```sh
rosrun udm_arduino_control arduino_custom_service.py _port:=/dev/ttyUSB0
```
Dans l'autre terminal

Pour faire clignoter la LED, modifier la valeur pour augmenter ou reduire la durer du clignotement
```sh
rosservice call /arduino_custom_server "delay:                  
  data: 0.50" 
```

# client

Dans source, il y a client.py qui n'est pas un noeud (il n'y pas de init_node()) mais c'est un script qui peut faire appel au service arduino_custom_server. 

Pour le lancer, assurez-vous d'avoir sourcer le devel/setup.bash puis se deplacer dans le repertoire source et lancer le script:

```sh
python client.py 0.2
```


