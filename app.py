import streamlit as st
import random

# region Variables
questions = [
    {
        "title": "When learning something new, you prefer to:",
        "choices": {
            "Look at diagrams, colors, and images": "Visual",
            "Listen to explanations or audiobooks": "Auditory",
            "Try it out and practice directly": "Kinesthetic"
        }
    },
    {
        "title": "When you need to remember something, you find it easier to recall by:",
        "choices": {
            "Imagining images or concept maps": "Visual",
            "Repeating it aloud or through discussions": "Auditory",
            "Doing it or rewriting the material": "Kinesthetic"
        }
    },
    {
        "title": "What type of learning material do you enjoy the most:",
        "choices": {
            "Videos with animations or illustrations": "Visual",
            "Podcasts or verbal explanations": "Auditory",
            "Workshops or hands-on simulations": "Kinesthetic"
        }
    },
    {
        "title": "Which activity sounds most appealing during a class?",
        "choices": {
            "Watching a demonstration or visual slides": "Visual",
            "Listening to a lecture or group discussion": "Auditory",
            "Engaging in an experiment or role-play": "Kinesthetic"
        }
    },
    {
        "title": "What do you usually do when trying to understand a new idea?",
        "choices": {
            "Draw it or visualize it in your mind": "Visual",
            "Talk it through with someone": "Auditory",
            "Act it out or build a model": "Kinesthetic"
        }
    },
    {
        "title": "Your note-taking style is usually:",
        "choices": {
            "Color-coded with diagrams or charts": "Visual",
            "Writing down what the teacher says word-for-word": "Auditory",
            "Minimal notes, preferring to recall from doing": "Kinesthetic"
        }
    },
    {
        "title": "How do you usually solve a problem?",
        "choices": {
            "Sketch out or map the situation": "Visual",
            "Talk through it step by step": "Auditory",
            "Tinker and try different things": "Kinesthetic"
        }
    },
    {
        "title": "When giving directions, you tend to:",
        "choices": {
            "Draw a map or show landmarks": "Visual",
            "Explain verbally with street names": "Auditory",
            "Physically point or gesture directions": "Kinesthetic"
        }
    },
    {
        "title": "In group projects, you are the one who usually:",
        "choices": {
            "Creates slides or visual materials": "Visual",
            "Leads the discussion or presents ideas": "Auditory",
            "Builds prototypes or does the hands-on tasks": "Kinesthetic"
        }
    },
    {
        "title": "What helps you relax the most?",
        "choices": {
            "Watching calming visuals or nature": "Visual",
            "Listening to music or podcasts": "Auditory",
            "Doing physical activities like stretching": "Kinesthetic"
        }
    },
    {
        "title": "Which type of game do you enjoy the most?",
        "choices": {
            "Puzzle or visual games": "Visual",
            "Music-based or quiz games": "Auditory",
            "Movement-based or active games": "Kinesthetic"
        }
    },
    {
        "title": "What is your biggest strength?",
        "choices": {
            "Observing patterns and visuals": "Visual",
            "Listening and expressing ideas": "Auditory",
            "Doing and making things happen": "Kinesthetic"
        }
    },
    {
        "title": "If you have to give a presentation, you'd prefer to:",
        "choices": {
            "Use slides and visual cues": "Visual",
            "Speak clearly and tell stories": "Auditory",
            "Use props or demonstrations": "Kinesthetic"
        }
    },
    {
        "title": "How do you like to spend your weekend?",
        "choices": {
            "Watching movies or reading": "Visual",
            "Chatting or listening to music": "Auditory",
            "Doing physical activities or crafts": "Kinesthetic"
        }
    },
    {
        "title": "When attending a workshop, what do you value most?",
        "choices": {
            "Visual aids and organized charts": "Visual",
            "Interactive discussion and audio clarity": "Auditory",
            "Hands-on practice and physical involvement": "Kinesthetic"
        }
    }
]

question_options = [3, 6, 9, 12, 15]
# endregion

# region Methods
def render_result(message, description, image_link, popup_type):
    if popup_type == "Success":
        st.success(message)
    elif popup_type == "Warning":
        st.warning(message)
    else:
        st.error(message)
    st.markdown(description)
    st.image(image_link, use_container_width=True)

def on_option_change():
    initialize_quiz_state()

def initialize_quiz_state():
    st.session_state.quiz_started = False
    st.session_state.filtered_questions = []

def initialize_dialog_state():
    st.session_state.open_dialog = False

def render_question_list():
    for index, question in enumerate(st.session_state.filtered_questions):
        question_number = index + 1
        question_number_key = f"question-{question_number}"
        question_title = f"{question_number}.{question['title']}"
        st.radio(question_title, question["choices"], index=None, key=question_number_key)

def render_scores(scores):
    for key, value in scores.items():
        st.markdown(f"Your {key.lower()} learning score is : **{value}**")

def calculate_scores():
    scores = {
        "Visual": 0,
        "Auditory": 0,
        "Kinesthetic": 0
    }

    unanswered_questions = []

    for index, question in enumerate(st.session_state.filtered_questions):
        question_number = index + 1
        question_number_key = f"question-{question_number}"
        selected_text = st.session_state.get(question_number_key)
        if selected_text:
            selected_value = question["choices"][selected_text]
            scores[selected_value] += 1
        else:
            unanswered_questions.append(question_number)
    
    return scores, unanswered_questions

@st.dialog("Result Summary")
def show_result_dialog():
    # region Variable in Results
    scores, unanswered_questions = calculate_scores()
    message = ""
    description = ""
    image_link = ""
    popup_type = ""
    is_all_questions_answered = len(unanswered_questions) == 0
    dominant_learning_style = max(scores.values())
    dominant_learning_style_list = list(scores.values()).count(dominant_learning_style)
    is_multiple_learning_styles = dominant_learning_style_list >= 2
    # endregion

    # region Render Results Component
    if is_all_questions_answered:
        if is_multiple_learning_styles:
            message = "⚠️ There is no suitable learning style, please try again"
            description = "This application requires one learning style to have the highest score. If Visual, Audio, and Kinesthetic scores are all equal or 2 of the learning styles have equal value, we cannot determine a dominant learning preference. Please try again and answer more reflectively."
            image_link = "assets/try-again.gif"
            popup_type = "Warning"
        else:
            if dominant_learning_style == "Visual":
                message = "👀 Congratulations, you are a VISUAL learner"
                description = "**Visual learners** understand best through seeing. They prefer images, diagrams, charts, and written instructions. They retain information more effectively when it's presented visually and often benefit from color-coded notes or mind maps."
                image_link = "assets/visual.gif"
            elif dominant_learning_style == "Auditory":
                message = "👂 Congratulations, you are a AUDITORY learner"
                description = "**Auditory learners** grasp concepts better through listening. They enjoy discussions, lectures, and audio materials, and they often remember information by hearing it or repeating it aloud. Sound and rhythm play a key role in how they process knowledge."
                image_link = "assets/auditory.gif"
            else:
                message = "🙌 Congratulations, you are a KINESTHETIC learner"
                description = "**Kinesthetic learners** learn best by doing. They prefer hands-on experiences, movement, and physical engagement with materials. They remember information through action, experiments, and real-world practice rather than passive observation or listening."
                image_link = "assets/kinesthetic.gif"
            
            popup_type = "Success"
    else:
        message = f"You haven't answered question number: {', '.join(str(item) for item in unanswered_questions)}"
        description = "Please answer all the questions before submitting. This application requires all responses to determine your learning style accurately."
        image_link = "assets/dont-do-this.gif"
        popup_type = "Error"

    render_result(message, description, image_link, popup_type)
    #endregion

    # region Detailed Scores
    if is_all_questions_answered:
        with st.expander("🔍 See Detailed Scores"):
            render_scores(scores)
    #endregion
# endregion

# region Content
st.header("📚 Learning Style Test")
selected_options = st.selectbox("Please select how many questions to display", question_options, on_change=on_option_change)

if "quiz_started" not in st.session_state:
    initialize_quiz_state()

if "open_result_dialog" not in st.session_state:
    initialize_dialog_state()

if st.button("Start Quiz"):
    st.session_state.quiz_started = True
    st.session_state.filtered_questions = random.sample(questions, selected_options)

if st.session_state.quiz_started:
    render_question_list()

    if st.button("Calculate Results"):
        st.session_state.open_dialog = True

if st.session_state.open_dialog:
    show_result_dialog()
# endregion