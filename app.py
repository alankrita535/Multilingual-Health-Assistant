import streamlit as st

st.title(" Multilingual AI Health Assistant")

user_input = st.text_input(
    "Enter your symptoms (English, Hindi, or Punjabi):"
)

if st.button("Get Advice"):

    text = user_input.lower()

    # Fever
    if "fever" in text or "बुखार" in text or "ਬੁਖਾਰ" in text:
        st.success(
            "Drink plenty of water and take proper rest. Consult a doctor if symptoms persist."
        )

    # Headache
    elif "headache" in text or "सिर दर्द" in text or "ਸਿਰ ਦਰਦ" in text:
        st.success(
            "Take adequate rest and stay hydrated."
        )

    # Cough
    elif "cough" in text or "खांसी" in text or "ਖੰਘ" in text:
        st.success(
            "Stay hydrated and avoid cold drinks."
        )

    # Cold
    elif "cold" in text or "जुकाम" in text or "ਜ਼ੁਕਾਮ" in text:
        st.success(
            "Take rest and drink warm fluids."
        )

    # Stomach pain
    elif "stomach pain" in text or "पेट दर्द" in text or "ਪੇਟ ਦਰਦ" in text:
        st.success(
            "Eat light food and consult a doctor if the pain is severe."
        )

    # Sore throat
    elif "sore throat" in text or "गले में दर्द" in text or "ਗਲੇ ਵਿੱਚ ਦਰਦ" in text:
        st.success(
            "Drink warm water and avoid cold foods."
        )

    else:
        st.warning(
            "Please consult a healthcare professional."
        )  
