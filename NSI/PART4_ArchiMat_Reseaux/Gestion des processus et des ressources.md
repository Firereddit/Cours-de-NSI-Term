[TOC]
# Gestion des processus et des ressources


![](https://i.imgur.com/exgSUhL.gif)

**Introduction :**

Considérons une activité simple sur ordinateur. Je rédige le compte-rendu de mon projet de construction de rue aléatoire sur un logiciel de traitement de texte. Mon navigateur web est aussi ouvert avec divers onglets, l’un pointant vers Wikipedia, l’autre sur la documentation Turtle et un autre sur Spotify. J’ai d’ailleurs mes écouteurs branchés. Mon projet est aussi ouvert sur divers fenêtres Idle (il est écrit en Python).

Tous ces programmes s’exécutent « en même temps ». Pourtant (selon les cours de première), un ordinateur ne dispose que d’un nombre limité de processeurs. Or, un programme est une suite d’instruction en langage machine, ces instructions sont exécutées une à une par le processeur. Alors comment le processeur (on imagine qu’on utilise un ordinateur mono-processeur pour simplifier), peut-il exécuter « en même temps » les instructions du navigateur web, du logiciel de traitement de texte et de Idle ?
Cette fonctionnalité de base (l’exécution concurrente des programmes) est permise par tous les systèmes d’exploitation modernes. On parle de système d’exploitation multitâches.

**Objectif de la séance :** 

- Rappel sur les systèmes d’exploitations, programmes et processus 
- Comprendre l’exécution concurrente de processus
- Gestion des processus par le système d’exploitation
- Mettre en évidence le risque de l’interblocage (deadlock)
- Notions de concurrence en Python (prochaine séance)

## 1- Les Systèmes d’exploitation (ou Operating System)

### 1- Définition

Le **système d’exploitation** d’un ordinateur est chargé d’assurer les **fonctionnalités** de **communication** et d’**interfaçage** avec l’**utilisateur**. Un **OS** est un **logiciel** dont le principal domaine d’intervention est la **gestion de toutes les ressources de l’ordinateur** comme : 
- le chargement et le lancement des programmes ;
- la gestion des processeurs, de la mémoire, des périphériques ;
- la gestion des processus (programmes en cours d'exécution) et des fichiers ;
- la protection contre les erreurs et la détection des erreurs ;
- etc...

C'est donc une composante logicielle très importante.
Dans un ordinateur, les logiciels sont divisés en deux catégories : 

- les **programmes système** qui font fonctionner l'ordinateur : le système d'exploitation et les utilitaires (compilateurs, éditeurs, interpréteurs de commandes, etc.)
-  les **programmes d'application** qui résolvent les problèmes spécifiques des utilisateurs.

![](https://i.imgur.com/JMPT5Vk.png)

*Vidéo de 3 minutes : [Introduction aux Systèmes d’exploitation](https://www.youtube.com/watch?v=AcZ87MTiXr4&feature=emblogo)*

Voici quelques exemples de système d’exploitation :
- MS-DOS, Windows
- OS/2, Mac-OS
- Unix (AIX, Xenix, Ultrix, Solaris, etc.)
- Linux
- Android
- Mais il en existe d'autres comme Symbian développé par Nokia, Tizen par Samsung, ...

### 2- Principaux types de systèmes d’exploitation

#### 1- OS « monoprogrammation »

Un OS est dit de **"monoprogrammation"** lorsqu'un **seul** **utilisateur** est présent et a accès à toutes les ressources de la machine pendant tout le temps que dure son travail. Si cet utilisateur exécute **plusieurs programmes, ils le seront les uns à la suite des autres.**

A titre d’exemple, supposons que sur un tel système 4 utilisateurs exécutent chacun un programme : P1, P2, P3 et P4. L’OS ne permet le passage des programmes que un à un : 
![](https://i.imgur.com/xQ1dDUb.png)
*Ici le programme P2 ne pourra s'exécuter que lorsque le programme P1 sera terminé, et ainsi de suite.*

**Rmq** : Relative aux temps d’attente, un système de monoprogrammation est très injuste vis à vis des petits programmes.

#### 2- OS « multiprogrammation »

Un OS est dit de " **multiprogrammation** " lorsque **plusieurs utilisateurs** peuvent être présents en **" même temps "** dans la machine et se **partagent les ressources de la machine pendant tout leur temps d’exécution**.

La multiprogrammation est la capacité d'un système à exécuter à la suite plusieurs activités sans l'intervention de l'utilisateur. Elle apparut dans les années 1960.




![](https://i.imgur.com/pyttQke.png)

*En reprenant l’exemple, P1, P2, P3, P4, sont exécutés cycliquement par l’OS qui leur alloue les ressources nécessaires (disque, mémoire, fichier,…) pendant leur tranche de temps d’exécution.*

**Rmq** : Relative aux temps d’attente, un système de multiprogrammation rétablit une certaine justice entre petits et gros programmes.
A l'heure actuelle, tous les OS sont issus de la multiprogrammation. Par exemple, elle est apparue dans la famille Windows avec Win98.

## 2- Les processus

### Exercice

À l’aide de la vidéo ci-dessous (ne regardez que jusqu’à 4 minutes 30), de vos connaissances et de votre moteur de recherche favoris, **proposez** une **définition** pour les mots suivants : 

{%youtube bFqud0gcCHM %}
- **Exécutable (ou programme)**: 
- **Processus** :
- **Threads (ou tâche)** :
- **Exécution parallèle** : 
- **Exécution concurrente** :

**Contexte d'exécution d'un programme** : Lorsqu'un programme qui a été traduit en instructions machines s'exécute, le processeur central lui fournit toutes ses ressources (registres internes, place en mémoire centrale, données, code,…), on appelle cet ensemble de ressources mises à disposition d'un programme "son contexte d'exécution.".

### 1- Processus et ordonnancement

Un **processus** est l'image en mémoire centrale d'un programme s'exécutant avec son contexte d'exécution.

Un ordinateur possède un ou plusieurs processeurs, qui sont eux-mêmes constitués de plusieurs unités de calcul, les cœurs. 
**C'est le système d'exploitation qui va donner à un processus** l'accès à une unité de calcul, cela s'appelle l'**ordonnancement**. Les processus ne quitteront cette dernière que si :

- Le processus s'arrête, lorsqu’il est terminé.
- Le processus demande à partir, il n'est pas terminé et demandera à revenir plus tard pour poursuivre son exécution. C'est par exemple le cas d'une tâche cyclique.
- Le processus est en attente. C'est par exemple le cas s’il n'y a pas d'instance (exemplaire) disponible de la ressource demandée par le processus, il est mis en attente pour libérer la place sur l'unité de calcul.
- Le système choisit d'arrêter le processus. C'est par exemple le cas lors de l'interblocage que nous verrons plus loin.

#### 1- Propriétés 

Lorsqu'une unité de calcul est libre, c'est le système d'exploitation qui va déterminer un nouveau processus à affecter à l'unité de calcul. Pour cela il existe plusieurs **algorithmes d'ordonnancement** (algorithmes de scheduling) :

- Le **modèle FIFO ou FCFS (First-Come, Firts-Served)** : on affecte les processus dans l'ordre de leur apparition dans la file d'attente. **Premier arrivé/premier servi**. 
    * **Avantages** : Cet algorithme est simple. C’est une simple liste chaînée et l’ordonnancement est équitable. 
    * **Inconvénients** : le processus qui utilise davantage de temps est favorisé par rapport à ceux qui font beaucoup d’appels aux entrées/sorties.

- Le **modèle SJF : Shortest Job First**, on affecte en premier le « **plus court processus en premier** » de la file d'attente à l'unité de calcul. Le job le plus court d’abord.
    * **Inconvénients** : si de multiples processus courts arrivent sans cesse, les plus longs ne seront jamais exécutés.

- Le **modèle Round Robin** : (ou méthode du tourniquet) **Chaque processus se voit alloué un certain temps d’attente**, appelé quatum, et à **tour de rôle**, chacun d’eux est traité par le processeur. En général, dans les OS multitâches, c’est cet algorithme qui est utilisé, avec un quantum entre 20 ms et 50 ms. Si le processus n'est pas terminé, il repart en fin de liste d'attente.

Il existe d'autres algorithmes d'ordonnancement, comme par exemple le modèle **Priorité**, où chaque processus dispose d’une valeur de priorité et on choisit le processus de plus forte priorité à chaque fois (nous ne détaillerons pas cet algorithme).

Afin de savoir si un algorithme est préférable pour un ensemble de processus, nous devons connaître quelques définitions.

#### 2- Définitions

**Représentation de l'ordonnancement :**
Réaliser l'ordonnancement d'une succession de processus c'est compléter un tableau de ce processus :

![](https://i.imgur.com/TkKC7Up.png)
On détermine aussi le temps d'attente moyen et le temps d'exécution moyen.

Pour illustrer les définitions qui suivent nous allons traiter un ordonnancement avec le **modèle SJF**.

![](https://i.imgur.com/Z3wyVrW.png)

Le **schéma d'ordonnancement** de ces processus sur le modèle SJF est le suivant : 

![](https://i.imgur.com/OnU08AD.png)

***Temps d'arrivée :***
Le temps d'arrivée d'un processus, ou temps de soumission, correspond au moment où le processus arrive dans la file d'attente.

**Ici** : Le temps d'arrivée du processus P5 est 7. Celui de P4 est 6.

***Durée du processus :***
La durée du processus P, ou durée d'exécution sur le coeur, correspond à la durée en quantum P nécessaire à l'exécution du processus.

Ici : La durée du processus P5 est 1. Celui de P4 est 2.

***Temps de terminaison :*** 
Le temps de terminaison d'un processus P est la durée écoulée entre le temps 0 et le temps où le processus est terminé P.

![](https://i.imgur.com/XgqJjCU.png)

***Temps d'exécution ou temps de séjour :***
Le temps d'exécution du processus P, ou temps de séjour, correspond à la différence du temps d'arrivée de P et du temps de terminaison de P.

![](https://i.imgur.com/W6Bckpz.png)


***Temps d'attente :***
Le temps d'attente d'un processus P ou durée d'attente du processus P correspond à la différence entre le temps de séjour (=temps d'exécution) et la durée du processus.

![](https://i.imgur.com/lHZqlAP.png)


#### 3- Exercices

Complétez les schémas suivants : 

***Pour le modèle FIFO***
![](https://i.imgur.com/d9EBqyr.png)

***Pour le modèle SJF***
![](https://i.imgur.com/50f4BjN.png)

***Pour le modèle Round Robin***
![](https://i.imgur.com/98ruPau.png)

**Rmq** : Actuellement, la **plupart** des **systèmes d’exploitation** utilisent une **évolution du modèle priorité**, reposant sur les principes suivants :
- chaque processus possède une priorité de base.
- cette priorité augmente quand le processus est inactif et diminue quand il est actif (le taux de changement dépend de la priorité de base).
- le système choisit parmi les processus de plus forte priorité.


***Représenter l’ordonnancement des processus ci-dessous à l’aide du modèle FIFO :***

![](https://i.imgur.com/SqqkrKT.png)

***Représenter l’ordonnancement des processus ci-dessous à l’aide du modèle SJF :***

![](https://i.imgur.com/iUai5GI.png)

***Représenter l’ordonnancement des processus ci-dessous à l’aide du modèle RR :***

![](https://i.imgur.com/mEHzW69.png)


***Représenter l’ordonnancement des processus ci-dessous à l’aide du modèle RR :***

![](https://i.imgur.com/GHILYxJ.png)


***On considère les processus ci-dessous. Quel algorithme, parmi les trois que l'on a étudié, permet l'exécution la plus rapide.***

![](https://i.imgur.com/SUpWL8K.png)


## 3- Processus: état et fonctionnement

![](https://i.imgur.com/3U9xiiv.jpg)

Un **processus** peut-être dans les états suivants :

- L'**état nouveau** (ou création) : chargement des instructions, allocation de mémoires et des ressources (statiquement), il passe directement à l’état prêt. Il existe **4 événements pour créer un processus** :

    * L’**initialisation du système** : au chargement du système il y a création automatique du processus racine père de tous les processus utilisateurs (id=0)
    * Un processus peut lancer un autre processus, il en devient le parent, l’autre dernier sera désigné comme **processus fils**. (Un processus père ne se termine que lorsque tous ses fils sont terminés. On a donc une structure arborescente de processus).
    * Une **requête** de l’utilisateur
    * Initiation d’un travail en **traitement par lot** (on exécute le même travail sur plusieurs entités à la fois, c'est par exemple très utilisé en photographie où on applique la même action sur plusieurs clichés).

**Rmq** : Lors de sa création, un numéro unique d'identification est attribué à chaque processus, c'est l'**identifiant de processus** ou **PID** (Process IDentifier). Grâce à cet identifiant, nous pourrons appliquer différentes commandes sur le processus.

- L’**état prêt** : Le processus est prêt à être exécuté. Il est mis en attente jusqu’à ce qu’on lui libère le processeur (dispatch de l’Ordonnanceur), il passera alors à l’état Actif.

- L’**état actif** (ou élu) : Le **processus est en cours d’exécution** par le processeur.
    * Si le processus épuise le temps qui lui est alloué par le SE, il est remis en file d’attente des Prêts.
    * S'il a besoin d’une ressource non disponible (opérations sur les périphériques), il est mis en attente prolongée (Interruption : état bloqué) jusqu’à la libération de la ressource nécessaire.
    * Si le processus atteint son terme (se termine) il passe à l’état terminé.

- L’**état attente** (ou bloqué) : Le **processus est en attente d’une ressource pour terminer**. Dès sa libération il repasse à l’état Prêt.

- L’**état terminé** : Lors de la **destruction le processus libère les ressources allouées**. Il y a quatre causes possibles de la destruction d’un processus :
    * Arrêt normal : cet arrêt est volontaire et intervient lorsque le processus termine sa tâche.
    * Arrêt pour erreur : cet arrêt est volontaire, il fait suite à une erreur pour une instruction illégale
    * Arrêt pour erreur fatale : cet arrêt est involontaire et intervient généralement lorsque les paramètres de l’exécution du processus sont mauvais.
    * Arrêt volontaire par un autre processus.

### 1- Petite expérience

Les instructions d’horloges ne sont pas les seuls événements permettant d’interrompre les processus.
Soit le petit programme Python : 

```python=
texte = input("Donne moi ton nom")
print("Ton nom en majuscule:", texte.upper())
```

Tant que l’utilisateur du programme ne rentre pas son nom, le programme ne peut avancer. Le système d’exploitation (qui gère aussi le matériel, ici le clavier nous intéresse) peut suspendre le processus et le mettre en attente. Le système d’exploitation sait qu’il est inutile de réveiller le processus tant que l’utilisateur n’interagit pas avec le clavier.

### 2- Programmation concurrente

Les **processus s’exécutent de manière concurrente** : leurs **exécutions** sont **entrelacées**. De plus, nous **ne pouvons pas décider** de l’**ordre** dans lequel les **processus s’exécutent**. Cet ordre est **décidé** par l’**ordonnanceur**. 

Cela offre de **grands avantages**, comme la **possibilité** d’e**xécuter un très grand nombre de programmes** sur une même machine monoprocesseur. Ou encore d’**optimiser les ressources de la machine**. Comme vu sur l’exemple précédent, si le processus est en attente d’entrées-sorties, il est mis en pause.

![](https://i.imgur.com/DUuCnbF.gif)

Cependant **un grand pouvoir implique de grandes responsabilités** ! Lorsque un **processus** est **interrompu**, il ne s’en « rend pas compte ». Si un processus est interrompu, **il reprend son exécution dans l’état où il s’était arrêté**.

**Expérience :**

```python=
from os import getpid
pid = str(getpid())
with open("test.txt", "w") as fichier:
    for i in range(1000):
        fichier.write(pid + " : " + str(i) + "\n")
        fichier.flush()
```
> - Enregistrez ce code Python dans un fichier que vous appellerez ecritfichier.py
> - Testez ce code, regardez le fichier test.txt alors crée. Que voyez-vous ?
> - Lancer trois fois le script en simultané, à l’aide d’un shell Unix et de la commande : 
```shell=
$ python3 ecritfichier.py & python3 ecritfichier.py & python3 ecritfichier.py &
```
> - Que voyez-vous dans le fichier test.txt ? Comment l’expliquez vous ?

## 4- Interblocage

**Certaines ressources** nécessitent souvent un **accès exclusif**. Cet accès exclusif peut-être source de problèmes.

*Si difficultés, demander à réaliser l'activité débranchée.*

### Exemple

Soit deux programmes imaginaires :+1: : 

- **enregistrer_micro** : ce programme doit avoir un accès exclusif à la carte son. Il s’arrête après 10 secondes de son.
- **jouer_son** : ce programme doit avoir un accès exclusif à la carte son. Il joue le contenu qu’il a reçu en argument.

Si j’exécute les deux instructions suivantes, **tout se passe très bien** : le **message est enregistré** (dans message.mp3). Il **est ensuite lu** par jouer_son.

```shell=
$ enregistrer_micro > message.mp3
$ cat message.mp3 | jouer_son
```

Par contre **que se passe-t-il** **si** on **enchaîne** **directement** les **deux programmes** à l’aide de cette commande ?

```shell=
$ enregistrer_micro | jouer_son
```
Le premier programme ouvre la carte son. Il commence à envoyer des données sur sa sortie standard. Le second programme tente alors d’ouvrir la carte son, qui est bloquée par le premier programme. Le second programme est alors bloqué. Le premier programme ne peut continuer son exécution car personne ne lit son enregistrement. 

Il y a interblocage ! Ou deadlock en anglais.

**Interblocage** : Un **ensemble de processus** est dans une situation d’interblocage **si** chaque **processus** de l’ensemble **attend un événement** **qui ne peut être produit que par un autre processus de l’ensemble.**

L’**interblocage** est **LE danger de la programmation concurrente**. 

Il existe **4 conditions**, appelées **Conditions de Coffman**, qui sont **nécessaires à l’interblocage**. (https://fr.wikipedia.org/wiki/Interblocage )

### **Conditions de Coffman**

   1. **Exclusion mutuelle** : au moins une ressource du système doit être en accès exclusif.
   2. **Rétention et attente** : un processus détient une ressource et demande une autre ressource détenue par un autre processus.
   3. **Non préemption** : une ressource ne peut être rendue que par un processus qui la détient.
   4. **Attente circulaire** : l’ensemble des processus bloqués P1,…,Pn sont tels que P1 attend une ressource tenue par P2, …, Pn attend une ressource tenue par P1.
    
    
**Exercice** :
**Démontrez rigoureusement** que 
```shell=
$ enregistrer_micro | jouer_son
```
**entraîne un interblocage** ( à l’aide des conditions de Coffman).

**Exercice** : 
Problème du carrefour. Démontrez rigoureusement qu’il y a un interblocage.


Plus tard : Programmation concurrente en Python

Pour aller (beaucoup) plus loin : 
https://asr-lyon1.gitlabpages.inria.fr/prog-concurrente-2018-2019/cm-threads/cm-threads-slides.pdf 