# fun_project_1_REAPYTHON1SMAGM

### Table of Contents

- [fun_project_1_REAPYTHON1SMAGM](#fun_project_1_reapython1smagm)
  - [Table of Contents](#table-of-contents)
  - [Project Description](#project-description)
  - [How to Setup Project](#how-to-setup-project)
  - [Usage](#usage)
  - [Features](#features)
  - [Demo](#demo)
    - [Starting the App](#starting-the-app)
    - [Unanswered Questions](#unanswered-questions)
    - [Equal Value](#equal-value)
    - [Visual Learning Style](#visual-learning-style)
    - [Auditory Learning Style](#auditory-learning-style)
    - [Kinesthetic Learning Style](#kinesthetic-learning-style)

### Project Description

To test correct learning style between Visual, Auditory and Kinesthetic learning
style.

This project is a part of Ruangguru Skill Academy Python AI Bootcamp Batch 1.

For more info about Ruangguru Skill Python Academy Bootcamp can check out in
here: [Python AI Bootcamp by Ruangguru](https://rea.ruangguru.com/python-ai)

### How to Setup Project

1. Clone the Repository
   - `git clone https://github.com/hanseltertius/fun_project_1_REAPYTHON1SMAGM.git`
2. Create Virtual Environment in Python
   - `python -m venv myenv`
   - To activate the virtual environment, we need to type:
     - If using Windows : `myenv\Scripts\activate`
     - If using Mac : `source myenv/bin/activate`
3. Install streamlit library (only if streamlit does not installed globally):
   - `python install streamlit`
   - `python3 install streamlit` (if above command does not work)

### Usage

In order to run the project locally, we need to type:

- `streamlit run app.py`
- Click the link in the Local URL part
  ![Screenshot](screenshots/Running%20the%20project%20in%20localhost.png)

If not in local, we can use:

- [Learning Style Fun Project 1](https://learning-style-fun-project.streamlit.app/)

### Features

In this project the features includes:

- Option to select how many questions, which is displayed in random order
- Condition to handle unanswered questions
- Condition to handle equal value
- Condition to handle Visual learning style
- Condition to handle Auditory learning style
- Condition to handle Kinesthetic learning style

### Demo

#### Starting the App

![Screenshot](screenshots/Select%20Box%20Choices.png) We can select the how many
questions we displayed ![Screenshot](screenshots/How%20to%20Start%20Quiz.png)
Click the button "Start Quiz" to start.

#### Unanswered Questions

![Screenshot](screenshots/Unanswered%20Question.png) Click "Calculate Results"
button

![Screenshot](screenshots/Unanswered%20Question%20Result.png)

#### Equal Value

![Screenshot](screenshots/Equal%20Value%20Answer.png)

- Click "Calculate Results" button
- This condition happens when score of "Visual", "Auditory" and "Kinesthetic"
  value are equal to each other

![Screenshot](screenshots/Equal%20Value%20Result.png)

#### Visual Learning Style

![Screenshot](screenshots/Visual%20Answer.png)

- Click "Calculate Results" button
- This condition happens when score of "Visual" (the first choice) is more
  dominant than the other

![Screenshot](screenshots/Visual%20Result.png)

#### Auditory Learning Style

![Screenshot](screenshots/Auditory%20Answer.png)

- Click "Calculate Results" button
- This condition happens when score of "Auditory" (the second choice) is more
  dominant than the other

![Screenshot](screenshots/Auditory%20Result.png)

#### Kinesthetic Learning Style

![Screenshot](screenshots/Kinesthetic%20Answer.png)

- Click "Calculate Results" button
- This condition happens when score of "Kinesthetic" (the third choice) is more
  dominant than the other

![Screenshot](screenshots/Kinesthetic%20Result.png)
