import streamlit as st

questions = [
    {
        "title": "Saat belajar sesuatu yang baru, kamu lebih suka:",
        "choices": {
            "Melihat diagram, warna, dan gambar": "Visual",
            "Mendengarkan penjelasan atau audio book": "Audio",
            "Langsung mencoba dan praktek": "Kinestetik"
        }
    },
    {
        "title": "Jika kamu harus mengingat sesuatu, kamu lebih mudah mengingat dengan cara:",
        "choices": {
            "Membayangkan gambar atau peta konsep": "Visual",
            "Mengulang-ulang dengan suara atau diskusi": "Audio",
            "Melakukan atau menulis ulang materi tersebut": "Kinestetik"
        }
    },
    {
        "title": "Jenis materi belajar yang paling kamu sukai:",
        "choices": {
            "Video dengan animasi atau ilustrasi": "Visual",
            "Podcast atau penjelasan verbal": "Audio",
            "Workshop atau simulasi langsung": "Kinestetik"
        }
    }
]

def render_result(message, description, image_link, popup_type = "Success"):
    if popup_type == "Success":
        st.success(message)
    elif popup_type == "Warning":
        st.warning(message)
    else:
        st.error(message)
    st.markdown(description)
    st.image(image_link, use_container_width=True)

# Content
st.header("📚 Learning Style Test")

for index, question in enumerate(questions):
    # index=None is to use the placeholder value
    question_number = index + 1
    question_number_key = f"question-{question_number}"
    question_title = f"{question_number}. {question["title"]}"
    st.radio(question_title, question["choices"], key=question_number_key)

if st.button("Calculate Results"):
    scores = {
        "Visual": 0,
        "Audio": 0,
        "Kinestetik": 0
    }

    for index, question in enumerate(questions):
        question_number = index + 1
        question_number_key = f"question-{question_number}"
        selected_text = st.session_state.get(question_number_key)
        if selected_text:
            selected_value = question["choices"][selected_text]
            scores[selected_value] += 1

    message = ""
    description = ""
    image_link = ""
    
    if scores["Visual"] == scores["Audio"] == scores["Kinestetik"]:
        message = "⚠️ There is no suitable learning style, please try again"
        description = "In this application, we cannot use the same values for Visual, Audio and Kinesthetic learning style, must have the highest value in one learning style."
        image_link = "assets/try-again.gif"
        render_result(message, description, image_link, popup_type="Warning")
    else:
        learning_style = max(scores, key=scores.get)

        if learning_style == "Visual":
            message = "👀 Congratulations, you are a VISUAL learner"
            description = "**Visual learners** understand best through seeing. They prefer images, diagrams, charts, and written instructions. They retain information more effectively when it's presented visually and often benefit from color-coded notes or mind maps."
            image_link = "assets/visual.gif"
        elif learning_style == "Audio":
            message = "👂 Congratulations, you are a AUDITORY learner"
            description = "**Auditory learners** grasp concepts better through listening. They enjoy discussions, lectures, and audio materials, and they often remember information by hearing it or repeating it aloud. Sound and rhythm play a key role in how they process knowledge."
            image_link = "assets/auditory.gif"
        else:
            message = "🙌 Congratulations, you are a KINESTHETIC learner"
            description = "**Kinesthetic learners** learn best by doing. They prefer hands-on experiences, movement, and physical engagement with materials. They remember information through action, experiments, and real-world practice rather than passive observation or listening."
            image_link = "assets/kinesthetic.gif"

        render_result(message, description, image_link)