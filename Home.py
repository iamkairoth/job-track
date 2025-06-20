# Home.py
import streamlit as st

def home():
    # Set page configuration must be at the very top of the script
    # It's usually placed in the main app file or conditionally
    # However, for multi-page apps, it's often placed in the main app.py if using st.Page,
    # or at the top of each page file for st.switch_page.
    # Placing it here as requested.
    st.set_page_config(page_title="JobTrack - Home", layout="wide")

    st.title("JobTrack: Navigating Your Career Journey")
    st.sidebar.header("JobTrack") # Sidebar for navigation, typical in Streamlit multi-page apps

    st.subheader("Your Personalized Compass for Career Success.")
    st.write("JobTrack is a comprehensive guide designed to empower your job search, no matter where you're starting from. We believe that understanding *how* to approach your career goals and *why* certain strategies work is essential for success.")
    st.write("At JobTrack, you'll discover personalized guidance, dive into essential career knowledge, and build strategies that truly fit *your* professional aspirations. We're here to help you learn, grow, and feel confident in every step towards your ideal career.")

    st.markdown("### Explore our features:")
    st.markdown("- **Assessment**: A personalized assessment to understand your current journey, goals, and preferences.")
    st.markdown("- **Fundamentals**: Articles and resources to deepen your understanding of key career topics.")
    st.markdown("- **Tools**: Practical guides on crafting essential job search documents and preparing for interviews.")
    st.markdown("- **Playbook**: Curated job search strategies tailored to your assessment results, with options to design your own.")
    st.markdown("- **Progress**: Track your learning milestones and stay motivated on your unique career path.")

    st.markdown("### Why JobTrack?")
    st.markdown("JobTrack is more than just a job board or application tracker; it's a comprehensive guidance platform designed to educate and empower you. We believe that career success is not just about finding a job, but also about understanding the process, honing your skills, and building a confident approach.")

    # Call to action button to navigate to the Assessment page
    if st.button("Start Your Career Journey!", key="start_journey_home", help="Begin your personalized career journey with JobTrack!"):
        st.switch_page("pages/2_Assessment.py") # Ensure this path is correct for your file structure

    st.markdown("### Disclaimer")
    st.warning("Please note that JobTrack provides general career guidance and educational resources. It is not a substitute for professional career counseling, legal, or financial advice. Always consult with a qualified professional for personalized assistance.")

# This ensures the home() function runs only when the script is executed directly
# and not when imported as a module by other pages.
if __name__ == "__main__":
    home()

