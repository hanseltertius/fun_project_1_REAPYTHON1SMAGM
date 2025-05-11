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

# Content
st.header("📚 Learning Style Test")

for index, question in enumerate(questions):
    # index=None is to use the placeholder value
    question_number = index + 1
    question_number_key = f"question-{question_number}"
    question_title = f"{question_number}. {question["title"]}"
    st.radio(question_title, question["choices"], key=question_number_key)

# TODO : create a button to calculate the results
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
    
    learning_style = max(scores, key=scores.get)

    st.write("Learning style :", learning_style)