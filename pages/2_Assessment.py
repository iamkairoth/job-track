# pages/Assessment.py
import streamlit as st

def assess_jobtrack():
    # Set page configuration
    st.set_page_config(page_title="JobTrack - Assessment", layout="wide")

    st.title("Assessment: Your Career Compass")
    st.sidebar.header("Assessment")

    st.write("To provide you with the most relevant and personalized guidance, we need to understand your current career situation. This quick assessment will help us tailor recommendations, suggest the right learning paths, and connect you with content that truly speaks to your needs.")
    st.write("There are no right or wrong answers – just be honest! Your responses will help us map out your ideal path in the world of career development.")

    # Initialize session state for storing assessment results
    if 'assessment_results_jt' not in st.session_state:
        st.session_state.assessment_results_jt = {}

    st.markdown("---") # Separator for better UI

    # Question 1: Current Career Stage
    st.markdown("#### 1. What is your current career stage?")
    career_stage = st.radio(
        "Select the option that best describes you:",
        ("Student / Recent Grad", "Early Career (1-3 years experience)", "Mid-Career (3-10 years experience)", "Senior / Executive (10+ years experience)", "Career Changer / Exploring New Fields"),
        horizontal=True,
        key="career_stage_jt"
    )
    st.session_state.assessment_results_jt['career_stage'] = career_stage

    st.markdown("---")

    # Question 2: Primary Career Goals
    st.markdown("#### 2. What are your primary career goals?")
    career_goals = st.multiselect(
        "Select all that apply:",
        ["Land my first job", "Get promoted / Advance my current role", "Change industries / career paths", "Improve specific professional skills", "Expand my professional network", "Negotiate a higher salary", "Start my own business (exploring)"],
        key="career_goals_jt"
    )
    st.session_state.assessment_results_jt['career_goals'] = career_goals

    st.markdown("---")

    # Question 3: Biggest Job Search Challenge
    st.markdown("#### 3. What's your biggest job search challenge right now?")
    career_challenge = st.multiselect(
        "Select your top challenges:",
        ["Resume writing / CV optimization", "Interview preparation / anxiety", "Networking effectively", "Finding relevant job opportunities", "Salary negotiation", "Personal branding / LinkedIn profile", "Lack of clear career direction"],
        key="career_challenge_jt"
    )
    st.session_state.assessment_results_jt['career_challenge'] = career_challenge

    st.markdown("---")

    # Question 4: Industry Interest
    st.markdown("#### 4. What industry or field are you most interested in?")
    industry_interest = st.text_input(
        "e.g., Tech, Marketing, Healthcare, Finance, Arts, Education, etc.",
        key="industry_interest_jt"
    )
    st.session_state.assessment_results_jt['industry_interest'] = industry_interest

    st.markdown("---")

    # Question 5: Time Commitment for Learning
    st.markdown("#### 5. How much time can you realistically commit to learning and working on your career journey each week?")
    time_commitment = st.radio(
        "Select your availability:",
        ("< 1 hour/week", "1-3 hours/week", "3-5 hours/week", "> 5 hours/week"),
        horizontal=True,
        key="time_commitment_jt"
    )
    st.session_state.assessment_results_jt['time_commitment'] = time_commitment

    st.markdown("---")

    # Button to save assessment and potentially navigate
    if st.button("Save My Assessment & Get My Path!", key="save_assessment_jt"):
        # Displaying a confirmation or summary (for now)
        st.success("Your assessment has been saved! Here's a quick summary:")
        for key, value in st.session_state.assessment_results_jt.items():
            st.write(f"- **{key.replace('_', ' ').title()}**: {value}")

        # In a real app, you'd use these results to recommend content
        st.info("Based on your responses, we recommend starting with our 'Fundamentals' and exploring the 'Resume Writing' section!")
        
        # Option to navigate to the recommended next page
        if st.button("Go to Career Fundamentals", key="go_to_fundamentals_from_assessment_jt"):
             st.switch_page("pages/3_Fundamentals.py")

    st.sidebar.info("Your assessment helps us tailor your JobTrack experience.")

# Run the assessment function when the script is executed
if __name__ == "__main__":
    assess_jobtrack()
