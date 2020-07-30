[![Build Status](https://travis-ci.org/pollen-robotics/rosa.svg?branch=master)](https://travis-ci.org/pollen-robotics/rosa)

# Le projet Rosa : un robot ramasseur d'objets

Le robot Rosa a été conçu dans le cadre d'une mission de [Poppy station](https://www.poppystation.org) effectuée par [Pollen-Robotics](https://www.pollen-robotics.com) et visant à concevoir un robot pour l'éducation capable de se déplacer dans l'environnement, de détecter et reconnaître des objets et de les transporter. Il peut être programmé depuis un ordinateur ou une tablette en Python ou Scratch 3.

Ce projet est entièrement open-source et s'appuie sur des composants Makers et DIY. Il a été conçu pour être facilement assemblable et personalisable. Il vise à être construit et distribué par les réseaux de distribution de la ligue pour l'Enseignement.

[![Video](http://i3.ytimg.com/vi/BjSzU6EHspg/hqdefault.jpg)](https://www.youtube.com/watch?v=BjSzU6EHspg)

## Guide de démarrage

### Modèles 3D

La CAO mécanique est faite avec OnShape et est disponible dans le [workspace Rosa](https://cad.onshape.com/documents/35ce243fe860772b30e007b8/w/907a682bb2447d12f8562319/e/38b8be09478438249969e7f1).

[![Onshape Rosa](img/onshape.png)](https://cad.onshape.com/documents/35ce243fe860772b30e007b8/w/907a682bb2447d12f8562319/e/38b8be09478438249969e7f1)

Les exports STL pour l'impressions sont disponibles dans les [releases](https://github.com/pollen-robotics/rosa/releases).

### Liste du materiel

| Nom                                                | Reference | Quantitée | Coût estimé| lien                                                                                                  |
|-----------------------------------------------------|------------|----------|----------------|-------------------------------------------------------------------------------------------------------|
| FeeTech 130 DC motor gear box **with 90° shaft**    | FT-DC-130D | 2        | US$0.72        | http://www.feetechrc.com/                                                                             |
| FeeTech Wheel for DC Motor gear box                 | FT-DC-W    | 2        | US$0.73        | http://www.feetechrc.com/                                                                             |
| Raspberry Pi 3 - Model A+                           |            | 1        | 20€            | https://fr.rs-online.com/web/p/products/8332699/                                                      |
| Raspberry Pi Camera Board - Fisheye 160° Lens (5MP) |            | 1        | 7-25€          | https://fr.aliexpress.com/item/32963289790.html                                                       |
| SD card 16Go                                        |            | 1        | 4€             | https://www.amazon.fr/NMicro-m%C3%A9moire-MicroSD-microSDHC-adaptateur/dp/B00N5TM8TY/ref=sr_1_1_sspa? |
| ZIPPY Compact 850mAh 2S 25C Lipo                    |ZC.850.2S.25| 1        | 5€             | https://hobbyking.com/fr_fr/zippy-compact-850mah-2s-25c-lipo-pack.html |
| Koncepto Custom Board                               |            | 1        | 57.5           |                                                                                                       |
| Vis M2.5x8 pour fixer les moteurs                   |            | 4        |                | https://www.cergy-vis.fr/vis-autotaraudeuses/vis-pour-thermoplastiques/tete-fraisee-pozidrive/eco-syn-pour-thermoplastiques-tfz-acier-zingue-blanc.html
| Vis M2.5x6 pour fixer la coque                      |            | 4        |                | https://www.cergy-vis.fr/vis-autotaraudeuses/vis-pour-thermoplastiques/tete-cylindrique-bombee-phillips/plastite-tcb-phillips-wn-1412-acier-zingue-blanc.html
| Vis M2.5x6 pour fixer la coque                      |            | 4        |                | https://www.cergy-vis.fr/vis-autotaraudeuses/vis-pour-thermoplastiques/tete-cylindrique-bombee-phillips/plastite-tcb-phillips-wn-1412-acier-zingue-blanc.html
| Vis M2.2x5 pour fixer la pi                         |            | 4        |                | https://www.cergy-vis.fr/vis-autotaraudeuses/vis-pour-thermoplastiques/tete-cylindrique-bombee-phillips/plastite-tcb-phillips-wn-1412-acier-zingue-blanc.html
| Vis M2 pour fixer la custom boar + camera           |            | 8        |                | 

### Electronique

La conception électronique a été réalisée par [Koncepto](https://koncepto.io/). Les sources des cartes permettant leur production sont disponibles dans les [releases](https://github.com/pollen-robotics/rosa/releases).

![Koncepto board top view](img/top_view.png)

![Koncepto board bottom view](img/bottom_view.png)

### Préparer la carte SD

Le logiciel embarqué du robot est disponible sous forme ISO prête à flasher sur une carte SD (8Go minimum). Cette ISO est disponible [ici](https://github.com/pollen-robotics/rosa/releases). Ce logiciel est responsable de piloter les moteurs en fonction des commandes reçues ainsi que d'envoyer les informations des différents capteurs.

Pour plus d'information sur comment écrire cette image on pourra se référer, par exemple, au site de Raspberry Pi [à cette adresse](https://www.raspberrypi.org/documentation/installation/installing-images/README.md).

Une fois la carte écrite avec l'image téléchargée, elle peut être insérée dans la carte Raspberry Pi de Rosa.

Afin de simplifier la première connexion au réseau WiFi, il est possible de le paramétrer directement sur la carte SD que l'on vient d'écrire. Il peut donc être plus pratique de réaliser cette étape avant d'insérer dans le robot (voir section [Connecter au réseau WiFi](https://github.com/pollen-robotics/rosa#connecter-rosa-au-réseau) pour plus d'informations).

### Alimentation

Nous conseillons d'alimenter Rosa avec cette batterie: [Zippy Compact 800mAh 2S](https://hobbyking.com/fr_fr/zippy-compact-800mah-2s1p-20c.html). Elle peut être rechargé via un chargeur LiPo comme celui ci: [HobbyKing B3AC Compact Chargeur](https://hobbyking.com/fr_fr/hobbykingr-b3ac-compact-charger-eu-plug.html).

### Connecter Rosa au réseau

Afin de pouvoir programmer le robot, il est nécessaire de le connecter au même réseau que son ordinateur ou sa tablette. Il peut se connecter au WiFi ou en Ethernet via un adaptateur USB.

#### WiFi

La carte Raspberry-Pi utilisée par le robot permet de se connecter à un réseau WiFi. Il est donc possible de la configurer comme n'importe quelle carte Raspberry-Pi.

Si vous avez facilement accès à la carte, il est possible de brancher un clavier (en USB) et un écran (en HDMI) sur la carte et d'utiliser l'interface de Raspberry-Pi pour configurer un réseau WiFi. Ce réseau sera conservé et le robot utilisera automatiquement ce réseau.

Il est également possible de venir rajouter un fichier spécial directement sur la partition BOOT de la carte SD. Par exemple, si on souhaite se connecter automatiquement au réseau WiFI "mon-reseau-wifi" avec comme mot de passe "password" il faut ajouter le fichier *wpa_supplicant.conf* suivant :

```
country=fr
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
    ssid="mon-reseau-wifi"
    psk="password"
}
```

Plus d'informations sur comment connecter une Raspberry-Pi à un réseau WiFi sont disponibles [sur le site de Raspberry-Pi](https://www.raspberrypi.org/documentation/configuration/wireless/).

#### Ethernet via USB

Il est également possible de connecter le robot au réseau via un cable en utilisant un adaptateur USB-Ethernet et en utilisant le port USB accessible à l'arrière du robot.

La détection du réseau est alors automatique.

#### Utilisation de ZeroConf

Le robot est toujours accessible sur le réseau à l'adresse *rosa.local*. Cela permet de simplifier la procédure de connexion, il n'est pas nécessaire de connaître l'adresse IP du robot. Cette addresse est utilisée par défaut par l'extension Scratch 3.

Cependant, pour pouvoir fonctionner ZeroConf nécessite d'installer un logiciel sur l'ordinateur.

- Pour Windows : [Bonjour print services](https://support.apple.com/kb/DL999)
- Pour Linux : avahi-daemon (mDNS) et avahi-autoipd (IPv4LL)
- Pour MacOS : ZeroConf est déjà installé.

## Capacités et caractéristiques

Le robot a été conçu pour pouvoir être utilisé dans différentes activités et dans des contextes variés. Les différentes capacités et caractéristiques du robot sont présentées ci-dessous.

### Navigation

Le robot possède deux roues actionnées chacune par un moteur. Elles peuvent tourner vers l'avant, vers l'arrière et s'arrêter. Le robot est donc capable de se déplacer dans un plan et de tourner sur lui même. La vitesse de déplacement du robot est réglable.

### Détection d'obstacles

Le robot possède plusieurs capteurs de distance (utilisant un émetteur/récepteur infra-rouge). Ces capteurs sont situés à l'avant du robot ainsi que sous le robot.

Ceux situés à l'avant peuvent être utilisés pour faire de la détection d'obstacles ou suivre un objet. Ils détectent un objet situé à une distance de 5 à 15cm. Ils permettent de mesurer la distance. Les capteurs sont positionnés :

- à l'avant gauche
- à l'avant centre
- et à l'avant droite.

À noter que le capteur central peut également être utilisé pour mesurer la couleur d'un objet positionné juste devant.

Ceux situés sous le robot sont utilisés pour détecter le vide, par exemple un bord de table. Ils peuvent également servir à détecter une ligne noire si elle est suffisament large (~ la largeur du robot). Il y a 4 capteurs de bord de table situés à chacun des coins du robot.

### Suivi de ligne

Le robot peut également suivre une ligne noire. La caméra est utilisée pour la détecter et identifier sa position verticale à une distance du robot donnée.

### Détection et reconnaissance d'objet

Le robot peut également détecter et reconnaître certains objets placés devant lui. Cette capacité permet la création d'activités autour de la collecte, du convoyage et du tri d'objets.

Les objets de couleur reconnus par le robot sont un cube, une étoile et une boule. Le modèle 3D de ces objets est disponible [ici](https://github.com/pollen-robotics/rosa/releases) et ils sont facilement imprimables sur une imprimante 3D du commerce.

La caméra du robot est utilisée pour reconnaître et détecter ses objets. Le robot renvoie une liste de l'ensemble des objets présents à l'image (il n'y a pas de limite maximale) avec pour chacun des objets son type (cube, étoile ou boule) et sa position dans l'image (la boite englobante).

*Note: il est possible, bien que plus compliqué, d'entrainer le robot à reconnaître de nouveaux objets si l'on souhaite.*

### Autres interactions

Le robot est également équipé d'un buzzer et de deux leds à l'avant permettant d'enrichir les interactions possibles.

## Utilisation

### Montage

* Insérer et fixer le moteur vertical (gauche) avec 2 vis XXX
* Insérérer et fixer le moteur horizontal (droit) avec 2 vis XXX
* Insérer la nappe dans la caméra, et fixer la caméra avec 4 vis XXX. Faire passer la nappe entre les 2 moteurs
* Approcher la custom board, faire passer la nappe dans l'encoche et connecter le moteur :
  * gauche sur J2
  * droit sur J3
* Fixer la custom board sous le chassis à l'aide de 4 vis XXX
* Connecter la nappe dans la Raspi et connecter la Raspi sur la custom board
* Connecter la batterie et l'insérer verticalement dans son logement, fils vers le haut 
* Fixer le couvercle arrière à l'aide de deux vis XXX à l'arrière et 2 vis XXX dessous sous la Raspi
* Flasher la carte microSD et l'insérer dans son emplacement
* Fixer le couvercle avant à l'aide de 2 vis XXX à l'avant et 2 vis XXX dessous sous la Raspi
* Monter 2 pneus sur 2 roues et les insérer sur leurs axes

### Python

L'API Python permet de controler le robot, d'accéder aux valeurs renvoyées par les senseurs ainsi que d'accéder à la caméra. Elle permet également l'utilisation des primitives de vision telles que la détection d'une ligne noire ou la détection d'objets.

Pour plus de détails, se reporter à la documentation dédiée : [Python's API](./api/python/readme.md)

### Scratch 3

Le robot peut également être programmé à l'aide d'une version dédiée de Scratch 3. Elle est accessible en ligne directement ici : http://www.scratch.pollen-robotics.cc

Les différents blocs proposés sont présentés ici : [extension Rosa pour Scratch 3](./api/scratch/readme.md).
