# Detoxipy Server
The server-side of a Twitch extension that allows users to visualize trending keywords in a Twitch chat using bubbles that grow and shrink depending on popularity.
___

**GitHub(Client)**

[https://github.com/DeToxers/DeToxipyClient](https://github.com/DeToxers/DeToxipyClient)

**GitHub(Server)**

[https://github.com/DeToxers/DeToxipyServer](https://github.com/DeToxers/DeToxipyServer)
___
## Branches
* Test
* Master
___
## Table of contents
* [Tools](#tools)
* [Overview](#overview)
* [Getting Started](#start)
* [Routes](#routes)
* [Models](#models)
* [Contribute](#contrib)
* [Participants](#participants)
* [Sources](#sources)
___
<a id="tools"></a>
## Tools
- Python3
- Javascript ES6
- Django 2.1.1
- Twitch Messaging Interface
- D3

___
<a id="overview"></a>
## Overview
![Wireframe](/wireframe.jpeg)

___
## Getting started
<a id="start"></a>
- Clone all the repositories. Start the chatbot server, the django server, and the D3 server.
___

## Routes

<a id="routes"></a>

**GET:**  `api/v1/bubble`

- **Usage:**

    Gets json chat data out of database.

- **Output:**
```
Code Block
```

**POST:**  `api/v1/chat`

- **Usage:**

    Post route for sending JSON of chat to our database.

- **Output:**
`
Code Block
```
___
## Models
<a id="models"></a>

- **ChatText**

    Holds the data for the current stream session. Stores it in the database in JSON.

___
<a id="contrib"></a>
## Contributing to our project
- Thanks for your interest in our project! Please name your branch according to the following convention: f_featurename_yourname. Then please make a pull request back to our master branch and we will review it.
___
<a id="participants"></a>
## Participants
- Max McFarland
- Luther Mckeiver
- Chris Chapman
- Madeline Peters
- Alex Stone
___
<a id="sources"></a>
## Sources
- Twitch Documentation
- D3 Documentation
___
<a id="Special Thanks"></a>
- Michael Sklepowich
- JJ Feore
- Shannon Tully
- Brian Nations
- James Salamonsen
- Benjamin Hurst
