# HackAI IIT Bombay Techfest Finale

# Personal Assistant Agent:
## [Youtube Video]([[https://youtu.be/ApsbYPHZoTA](https://drive.google.com/drive/folders/1PLGQ_YnQ4fvnEtzlbFvwRCLQBNDxQVbf?usp=sharing)]([https://youtu.be/ApsbYPHZoTA](https://drive.google.com/drive/folders/1PLGQ_YnQ4fvnEtzlbFvwRCLQBNDxQVbf?usp=sharing)))


## Video Demo
You can watch a video demo of our project:
[![Watch the video]]([https://youtu.be/ApsbYPHZoTA](https://youtu.be/ApsbYPHZoTA))



## **Vision of FetchAI**
- Automate repetitive tasks
- Remove decentralisation
- Replacing so many applications on our mobile phone with autonomous agents

## Project Information

## Abstract
*Travelling to a new city and unsure of the places to visit?*
*Tired of the repetitive tasks of booking cabs?*
*Want an assistant who automatically gives you important reminders?*
*Wish you had a digital twin who makes your life easier by maximizing your productivity and economic value?*

Well, this is absolutely what our project aims for! Let's dive in

## **Agents used in our Project, aligning with Vision of FetchAI**
1. User Agent
  - Interacts with other agents based on user input query
  - Knows the preferences of user based on previous interactions with agents
  - Aims to maximize the economic value of the user while also providing the best options towards user query
2. Travel Agent
  - Gives a travel plan according to user travel needs and preferences
  - Has the capability to *call the calender agent* and set up reminders for all set of events in our travel plan 
2. Calender Agent
  - Puts up reminders for various events in our google calender
  - Puts up a agent prefix on our events added to
3. Cab Service Agent
  - Every cab driver owns its own cab service agent in accordance with a decentralised economy of agents.
  - Has the communicate with the *call the travel agent* 

## Sample Flow of our Personal Assistant
1. User puts up a query "I am new to Delhi, suggest me a travel plan this weekend"
2. **User Agent** captures the query and calls the **Travel Agent** to get a list of latest travel plans that align with user preferences.
3. **Travel agent** responds with the list of travelling options.
4. **User agent** interacts with the user and gets the list of travel options confirmed.
5. **User agent** calls the **calender agent** to schedule the reminders for events in travel plans
6.  **User agent** calls the **travel agent** to schedule the cab service.
7.  **Travel agent** broadcasts the travel source and destinations to **cab service agent**  
8. Multiple cab service agents who  

**Screenshots:**
## Screenshots



**Technology Stack:**
- Python
- Fetch.ai uAgent Library
- ngrok
- Agentverse

*Project Architecture*


## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Node.js and npm installed on your development machine.
- Python installed for the backend.

### Installation

#### React Frontend

1. Clone the repository:

   ```bash
   git clone https://github.com/RuchikaSuryawanshi7/HackAI-Fledglings.git


2. Install

```bash
cd temperature-alert-agent
Install dependencies:
pip install -r requirements.txt
````

