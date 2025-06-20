# pages/Fundamentals.py
import streamlit as st

def fundamentals_jobtrack():
    # Set page configuration
    st.set_page_config(page_title="JobTrack - Fundamentals", layout="wide")

    st.title("Career Fundamentals: Your Knowledge Hub")
    st.sidebar.header("Fundamentals")

    st.write("Welcome to your essential knowledge library! This is where you'll gain the insights to truly understand various aspects of job searching and career development. We’ve curated expert-led content and broken down complex topics into easy-to-digest guides.")
    st.write("Learn the 'why' behind effective resumes, successful interviews, strategic networking, and more. Empower yourself with knowledge from trusted sources, including top career coaches, recruiters, and industry experts.")

    st.markdown("---")

    # Navigation for different sections within Fundamentals
    selected_section = st.sidebar.selectbox(
        "Select a section to explore:",
        options=["Overview", "Resume Writing", "Cover Letters", "Interview Skills", "Networking", "Personal Branding", "Salary Negotiation", "Job Search Strategy", "Mindset for Job Search"],
        help="Choose a section to dive deeper into career fundamentals."
    )

    if selected_section == "Overview":
        st.markdown("### Explore our core learning areas:")
        st.markdown("- **Resume Writing**: Craft a compelling resume that stands out to recruiters and ATS systems.")
        st.markdown("- **Cover Letters**: Learn how to write impactful cover letters that get noticed.")
        st.markdown("- **Interview Skills**: Prepare for various interview formats and master your responses.")
        st.markdown("- **Networking**: Build meaningful professional connections effectively.")
        st.markdown("- **Personal Branding**: Develop a strong online presence and tell your unique career story.")
        st.markdown("- **Salary Negotiation**: Understand how to negotiate for the compensation you deserve.")
        st.markdown("- **Job Search Strategy**: Design an efficient and effective plan for your job hunt.")
        st.markdown("- **Mindset for Job Search**: Cultivate resilience, manage stress, and stay motivated throughout your journey.")

    elif selected_section == "Resume Writing":
        st.markdown("### Resume Writing: Crafting Your First Impression")
        st.write("Your resume is often the first interaction a potential employer has with you. Learn how to create a powerful document that highlights your skills and experience effectively.")
        st.markdown("#### Key Concepts:")
        st.markdown("- **ATS Optimization**: Understanding Applicant Tracking Systems and how to beat them.")
        st.markdown("- **Action Verbs**: Using strong, impactful verbs to describe your achievements.")
        st.markdown("- **Quantifying Achievements**: How to add numbers and data to show your impact.")
        st.markdown("- **Formatting Best Practices**: Tips for clean, readable, and professional layouts.")
        st.markdown("---")
        st.markdown("#### External Resources:")
        st.markdown("- [Video: ATS Friendly Resume Tips by Career Expert A](https://www.youtube.com/watch?v=example1) (Placeholder Link)")
        st.markdown("- [Article: Top Resume Mistakes to Avoid by Blog B](https://www.exampleblog.com/resume-mistakes) (Placeholder Link)")
        # Example of marking module complete
        if st.checkbox("Mark 'Resume Writing' as Completed", key="resume_fundamentals_complete"):
            st.session_state.get('completed_modules_jt', []).append('Resume Writing')
            st.success("Great job! You've marked 'Resume Writing' as completed.")

    elif selected_section == "Cover Letters":
        st.markdown("### Cover Letters: Making Your Application Personal")
        st.write("A well-written cover letter can be your secret weapon, allowing you to showcase your personality and passion beyond your resume. Learn how to tailor each letter to the specific job and company.")
        st.markdown("#### Key Concepts:")
        st.markdown("- **Structure**: The essential paragraphs of a compelling cover letter.")
        st.markdown("- **Personalization**: How to make your letter relevant to the role and company.")
        st.markdown("- **Storytelling**: Using brief anecdotes to demonstrate your fit.")
        st.markdown("---")
        st.markdown("#### External Resources:")
        st.markdown("- [Video: How to Write a Winning Cover Letter by Recruiter C](https://www.youtube.com/watch?v=example2) (Placeholder Link)")
        if st.checkbox("Mark 'Cover Letters' as Completed", key="coverletter_fundamentals_complete"):
            st.session_state.get('completed_modules_jt', []).append('Cover Letters')
            st.success("Excellent! You've marked 'Cover Letters' as completed.")

    elif selected_section == "Interview Skills":
        st.markdown("### Interview Skills: Confidently Acing Your Conversations")
        st.write("Interviews are your chance to shine and demonstrate your fit for the role. This section covers various interview types and strategies to help you respond confidently and effectively.")
        st.markdown("#### Key Concepts:")
        st.markdown("- **Behavioral Interviews**: Mastering the STAR method.")
        st.markdown("- **Technical Interviews**: Strategies for coding or problem-solving assessments.")
        st.markdown("- **Virtual Interview Etiquette**: Tips for looking and sounding professional online.")
        st.markdown("- **Asking Questions**: Why and what questions to ask your interviewer.")
        st.markdown("---")
        st.markdown("#### External Resources:")
        st.markdown("- [Article: Ultimate Interview Prep Guide by Career Coach D](https://www.examplewebsite.com/interview-prep) (Placeholder Link)")
        if st.checkbox("Mark 'Interview Skills' as Completed", key="interview_fundamentals_complete"):
            st.session_state.get('completed_modules_jt', []).append('Interview Skills')
            st.success("Fantastic! You've marked 'Interview Skills' as completed.")

    elif selected_section == "Networking":
        st.markdown("### Networking: Building Your Professional Circle")
        st.write("Networking is about building genuine relationships that can open doors to new opportunities. Learn effective strategies for connecting with professionals in your target industry.")
        st.markdown("#### Key Concepts:")
        st.markdown("- **Informational Interviews**: How to conduct them and what to ask.")
        st.markdown("- **LinkedIn Strategies**: Maximizing your presence and connections on the platform.")
        st.markdown("- **Event Networking**: Tips for virtual and in-person events.")
        st.markdown("- **Follow-Up Etiquette**: Nurturing your new connections.")
        st.markdown("---")
        st.markdown("#### External Resources:")
        st.markdown("- [Guide: Networking for Introverts by Expert E](https://www.exampleguide.com/networking-introverts) (Placeholder Link)")
        if st.checkbox("Mark 'Networking' as Completed", key="networking_fundamentals_complete"):
            st.session_state.get('completed_modules_jt', []).append('Networking')
            st.success("Great! You've marked 'Networking' as completed.")

    elif selected_section == "Personal Branding":
        st.markdown("### Personal Branding: Defining Your Unique Professional Identity")
        st.write("Your personal brand is what sets you apart. Learn how to articulate your strengths, values, and career aspirations to create a consistent and compelling professional narrative.")
        st.markdown("#### Key Concepts:")
        st.markdown("- **Identifying Your Niche**: What makes you unique?")
        st.markdown("- **Online Presence**: Curating your LinkedIn, portfolio, and other digital footprints.")
        st.markdown("- **Storytelling**: Crafting your professional narrative.")
        st.markdown("---")
        st.markdown("#### External Resources:")
        st.markdown("- [Article: Building Your Brand on LinkedIn by Influencer F](https://www.examplearticle.com/linkedin-branding) (Placeholder Link)")
        if st.checkbox("Mark 'Personal Branding' as Completed", key="branding_fundamentals_complete"):
            st.session_state.get('completed_modules_jt', []).append('Personal Branding')
            st.success("Excellent! You've marked 'Personal Branding' as completed.")

    elif selected_section == "Salary Negotiation":
        st.markdown("### Salary Negotiation: Advocating for Your Value")
        st.write("Negotiating your salary can be daunting, but it's a crucial skill. Learn strategies to confidently discuss compensation and secure a fair offer.")
        st.markdown("#### Key Concepts:")
        st.markdown("- **Researching Market Value**: Knowing your worth.")
        st.markdown("- **Timing Your Negotiation**: When to bring up salary.")
        st.markdown("- **Beyond Base Salary**: Benefits, bonuses, and perks.")
        st.markdown("---")
        st.markdown("#### External Resources:")
        st.markdown("- [Webinar Replay: Salary Negotiation Tactics by Expert G](https://www.examplewebinar.com/salary-negotiation) (Placeholder Link)")
        if st.checkbox("Mark 'Salary Negotiation' as Completed", key="salary_fundamentals_complete"):
            st.session_state.get('completed_modules_jt', []).append('Salary Negotiation')
            st.success("Awesome! You've marked 'Salary Negotiation' as completed.")

    elif selected_section == "Job Search Strategy":
        st.markdown("### Job Search Strategy: Designing Your Efficient Hunt")
        st.write("An organized and strategic job search can save you time and reduce stress. Learn how to build a systematic approach to finding and applying for roles.")
        st.markdown("#### Key Concepts:")
        st.markdown("- **Goal Setting**: Defining clear job targets.")
        st.markdown("- **Time Management**: Allocating time for applications, networking, and skill development.")
        st.markdown("- **Tracking Your Progress**: Simple methods to monitor your applications.")
        st.markdown("- **Leveraging Job Boards**: Maximizing your use of online platforms.")
        st.markdown("---")
        st.markdown("#### External Resources:")
        st.markdown("- [Podcast: Building a Job Search System by Coach H](https://www.examplepodcast.com/job-search-system) (Placeholder Link)")
        if st.checkbox("Mark 'Job Search Strategy' as Completed", key="strategy_fundamentals_complete"):
            st.session_state.get('completed_modules_jt', []).append('Job Search Strategy')
            st.success("Fantastic! You've marked 'Job Search Strategy' as completed.")

    elif selected_section == "Mindset for Job Search":
        st.markdown("### Mindset for Job Search: Cultivating Resilience & Positivity")
        st.write("The job search can be challenging. This section focuses on the mental aspect, helping you build resilience, manage stress, and maintain a positive outlook throughout your journey.")
        st.markdown("#### Key Concepts:")
        st.markdown("- **Managing Rejection**: How to bounce back stronger.")
        st.markdown("- **Combating Imposter Syndrome**: Believing in your own abilities.")
        st.markdown("- **Celebrating Small Wins**: Staying motivated through progress.")
        st.markdown("- **Self-Care**: Prioritizing your well-being during the search.")
        st.markdown("---")
        st.markdown("#### External Resources:")
        st.markdown("- [Article: Overcoming Job Search Burnout by Psychologist I](https://www.examplearticle.com/job-search-burnout) (Placeholder Link)")
        if st.checkbox("Mark 'Mindset for Job Search' as Completed", key="mindset_fundamentals_complete"):
            st.session_state.get('completed_modules_jt', []).append('Mindset for Job Search')
            st.success("Great! You've marked 'Mindset for Job Search' as completed.")

# Run the function when the script is executed
if __name__ == "__main__":
    fundamentals_jobtrack()
