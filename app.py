import streamlit as st
from mediaguard import check_hash, check_metadata, detect_faces, error_level_analysis, detect_ai_generation, save_report
import os

st.set_page_config(page_title="MediaGuard", page_icon="🛡️")
st.title("🛡️ MediaGuard - Image Forensics Tool")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file is not None:
    file_path = os.path.join("temp_input." + uploaded_file.type.split("/")[-1])
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.image(file_path, caption="Uploaded Image", use_column_width=True)

    if st.button("🔍 Analyze Image"):
        st.success("✅ Analysis Started")
        st.text("📦 SHA256 Hash:")
        check_hash(file_path)

        st.text("\n📸 Metadata:")
        check_metadata(file_path)

        st.text("\n🧠 Face Detection:")
        detect_faces(file_path)

        st.text("\n🧪 ELA:")
        error_level_analysis(file_path)

        st.text("\n🤖 AI-Generation Check:")
        detect_ai_generation(file_path)

        save_report(file_path)
        st.success("📄 Report saved as MediaGuard_Report.txt")
