# pages/ThankYou.py
import streamlit as st

def thankyou_jobtrack():
    # Set page configuration
    st.set_page_config(page_title="JobTrack - Thank You", layout="wide")

    st.title("Thank You for Choosing JobTrack!")
    st.sidebar.header("Thank You")

    st.write("We're incredibly grateful you've chosen JobTrack to guide your career journey. We hope you've found valuable insights, clear guidance, and the confidence to take control of your professional path.")
    st.write("Remember, JobTrack is your companion for *understanding* and *strategizing* your job search. When it comes to the detailed logistics of applying, tracking applications, or managing outreach, we recommend using specialized tools.")

    st.markdown("---")

    st.markdown("### Recommendations & Next Steps:")

    st.markdown("#### 1. For Application Tracking & Job Searching:")
    st.markdown("While JobTrack provides the strategy, these tools can help with the execution:")
    st.markdown("- **LinkedIn Jobs**: For finding and applying to a wide range of roles and leveraging your professional network.")
    st.markdown("- **Indeed / Naukri.com (India-specific)**: Popular job boards for diverse listings.")
    st.markdown("- **Notion / Google Sheets**: Simple, customizable options for tracking applications, interviews, and networking outreach manually. There are many free templates available online.")
    st.markdown("- **Dedicated Application Trackers (e.g., Huntr, Teal)**: Explore these if you need more robust features for managing your pipeline.")

    st.markdown("#### 2. Stay Connected & Continue Learning:")
    st.markdown("- **Explore more topics**: Your career journey is ongoing. Revisit our 'Fundamentals' and 'Tools' sections, and refine your 'Playbooks' as you gain more experience.")
    st.markdown("- **Connect with us**: Follow us on social media for the latest career tips, industry insights, and community discussions. [Link to your social media, if applicable]")
    st.markdown("- **Join professional communities**: Engage with forums and groups in your target industry or role to stay updated and network.")

    st.markdown("#### 3. Share Your Feedback:")
    st.write("We value your feedback immensely! Your insights help us improve JobTrack and create even better resources for everyone.")
    st.markdown("[Provide a link to a feedback form here, e.g., Google Form, SurveyMonkey, or a simple email address.]")

    st.markdown("---")
    st.info("We wish you the very best in your career endeavors! Keep learning, keep growing, and keep pushing forward.")

# Run the function when the script is executed
if __name__ == "__main__":
    thankyou_jobtrack()
