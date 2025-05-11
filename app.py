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

def render_result(message, description):
    st.success(message)
    st.markdown(description)

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
    
    if scores["Visual"] == scores["Audio"] == scores["Kinestetik"]:
        st.warning("⚠️ There is no suitable learning style, please try again")
    else:
        learning_style = max(scores, key=scores.get)

        message = ""
        description = ""

        if learning_style == "Visual":
            message = "👀 Congratulations, you are a VISUAL learner"
            description = "**Visual learners** understand best through seeing. They prefer images, diagrams, charts, and written instructions. They retain information more effectively when it's presented visually and often benefit from color-coded notes or mind maps."
        elif learning_style == "Audio":
            message = "👂 Congratulations, you are a AUDITORY learner"
            description = "**Auditory learners** grasp concepts better through listening. They enjoy discussions, lectures, and audio materials, and they often remember information by hearing it or repeating it aloud. Sound and rhythm play a key role in how they process knowledge."
        else:
            message = "🙌 Congratulations, you are a KINESTHETIC learner"
            description = "**Kinesthetic learners** learn best by doing. They prefer hands-on experiences, movement, and physical engagement with materials. They remember information through action, experiments, and real-world practice rather than passive observation or listening."

        render_result(message, description)