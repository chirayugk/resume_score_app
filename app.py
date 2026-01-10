import streamlit as st
from engine import analyze, imp
import tempfile

st.set_page_config("Resume Score Checker")
st.title("ResumeFit AI")
st.subheader("Upload Resume & Job Description")

resume_file = st.file_uploader("Upload Resume", type=["pdf"])
jd_file = st.file_uploader("Upload Job Description", type=["pdf"])

if resume_file and jd_file:

    with tempfile.NamedTemporaryFile(delete=False) as r:
        r.write(resume_file.getvalue())
        resume_path = r.name

    with tempfile.NamedTemporaryFile(delete=False) as j:
        j.write(jd_file.getvalue())
        jd_path = j.name

    if st.button("Analyze"):

        with st.spinner("Analyzing..."):
            result = analyze(resume_path, jd_path)

        st.success("Analysis Complete")
        st.metric("Match Score", result)

    if st.button("What needs to be changed"):

        with st.spinner("Analyzing..."):
            result = imp(resume_path, jd_path)

        st.write(result)
