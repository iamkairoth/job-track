# pages/Tools.py
import streamlit as st

def tools_jobtrack():
    # Set page configuration
    st.set_page_config(page_title="JobTrack - Tools & Guides", layout="wide")

    st.title("Job Search Tools & Guides")
    st.sidebar.header("Tools")

    st.write("This section provides practical guides on how to craft essential job search documents and prepare for crucial career conversations. We break down the components and provide actionable tips to help you build effective tools for your job hunt.")
    st.write("Remember, these are not just templates, but educational resources to help you understand *what goes into* a strong application or interview.")

    st.markdown("---")

    # Navigation for different sections within Tools
    selected_section = st.sidebar.selectbox(
        "Select a tool guide:",
        options=["Overview", "Resume Components", "Cover Letter Structure", "Interview Question Types", "Networking Message Examples"],
        help="Choose a guide to learn how to build effective job search tools."
    )

    if selected_section == "Overview":
        st.markdown("### Explore our practical guides:")
        st.markdown("- **Resume Components**: Learn what makes a powerful resume section by section.")
        st.markdown("- **Cover Letter Structure**: Understand the essential parts of a compelling cover letter.")
        st.markdown("- **Interview Question Types**: Prepare for common interview questions and practice your responses.")
        st.markdown("- **Networking Message Examples**: Get templates and tips for effective professional outreach.")

    elif selected_section == "Resume Components":
        st.markdown("### Resume Components: Building Block by Building Block")
        st.write("A strong resume is built from well-structured sections. Learn what to include in each part to create a comprehensive and impactful document.")
        st.markdown("#### Essential Sections:")
        st.markdown("- **Contact Information**: Your name, phone, email, LinkedIn URL (optional: portfolio link).")
        st.markdown("- **Summary/Objective**: A brief, impactful statement tailored to the role. For experienced pros, a summary; for new grads, an objective.")
        st.markdown("- **Work Experience**: Focus on achievements, not just duties. Use action verbs and quantify results.")
        st.markdown("- **Education**: Degrees, institutions, graduation dates. Relevant coursework or projects can be added.")
        st.markdown("- **Skills**: List technical skills, software proficiencies, languages, and soft skills (e.g., communication, teamwork).")
        st.markdown("- **Optional Sections**: Projects, volunteer work, certifications, awards, publications.")
        st.markdown("---")
        st.markdown("#### Tip: Quantify your achievements! Instead of 'Managed projects,' try 'Managed 5 projects, leading to a 15% increase in efficiency.'")
        if st.checkbox("Mark 'Resume Components' Guide as Completed", key="resume_tools_complete"):
            st.session_state.get('completed_modules_jt', []).append('Resume Components Guide')
            st.success("Great job! You've learned about Resume Components.")

    elif selected_section == "Cover Letter Structure":
        st.markdown("### Cover Letter Structure: Your Personal Story")
        st.write("A well-structured cover letter tells your unique story and explains why you're the perfect fit for the job.")
        st.markdown("#### Key Paragraphs:")
        st.markdown("- **Introduction**: State the position you're applying for, where you saw the listing, and a brief hook about why you're interested and qualified.")
        st.markdown("- **Body Paragraph 1 (Skills Match)**: Highlight 1-2 key skills/experiences from your resume that directly align with the job description. Provide specific examples (using STAR method if applicable).")
        st.markdown("- **Body Paragraph 2 (Culture Fit/Passion)**: Show your enthusiasm for the company and its mission. Explain why you want to work *there*, not just any company.")
        st.markdown("- **Conclusion**: Reiterate your interest, express eagerness for an interview, and thank them for their time and consideration.")
        st.markdown("---")
        st.markdown("#### Tip: Always customize your cover letter for *each* application. Generic letters rarely get noticed!")
        if st.checkbox("Mark 'Cover Letter Structure' Guide as Completed", key="coverletter_tools_complete"):
            st.session_state.get('completed_modules_jt', []).append('Cover Letter Structure Guide')
            st.success("Excellent! You've learned about Cover Letter Structure.")

    elif selected_section == "Interview Question Types":
        st.markdown("### Interview Question Types: Preparing for Any Scenario")
        st.write("Interviews come in various forms. Understanding the different types of questions can help you prepare targeted and confident responses.")
        st.markdown("#### Common Interview Question Categories:")
        st.markdown("- **Behavioral Questions**: 'Tell me about a time when...' (e.g., 'Tell me about a time you faced a challenge and how you overcame it.')")
        st.markdown("    - **Strategy**: Use the **STAR method** (Situation, Task, Action, Result) to structure your answers.")
        st.markdown("- **Situational Questions**: 'What would you do if...' (e.g., 'What would you do if a team member wasn't pulling their weight?')")
        st.markdown("    - **Strategy**: Describe your thought process and action plan, focusing on problem-solving and collaboration.")
        st.markdown("- **Technical Questions**: Specific to your field (e.g., 'Explain how OAuth works,' 'Write a function for X').")
        st.markdown("    - **Strategy**: Be clear, concise, and explain your reasoning. If you don't know, explain how you would approach finding the answer.")
        st.markdown("- **Motivational Questions**: 'Why do you want this job?' 'Why our company?'")
        st.markdown("    - **Strategy**: Show genuine interest, align with company values, and highlight what excites you about the role.")
        st.markdown("---")
        st.markdown("#### Tip: Practice answering questions out loud, even recording yourself. This helps refine your responses and build confidence.")
        if st.checkbox("Mark 'Interview Question Types' Guide as Completed", key="interview_tools_complete"):
            st.session_state.get('completed_modules_jt', []).append('Interview Question Types Guide')
            st.success("Fantastic! You've learned about Interview Question Types.")

    elif selected_section == "Networking Message Examples":
        st.markdown("### Networking Message Examples: Crafting Effective Outreach")
        st.write("Effective networking starts with clear, concise, and respectful communication. Here are examples for various networking scenarios.")
        st.markdown("#### Examples:")
        st.markdown("- **LinkedIn Connection Request (Cold)**:")
        st.code("""
Hi [Name],
I saw your profile and was impressed by your work at [Company] in [Industry/Role]. I'm currently [Your Situation - e.g., looking to transition into X / a student studying Y] and would love to connect and learn more about your career path.
Best,
[Your Name]
            """)
        st.markdown("- **Informational Interview Request (after connecting)**:")
        st.code("""
Hi [Name],
Thanks for connecting! I'm really interested in learning more about [Specific Area, e.g., product management] at [Company]. Would you be open to a brief 15-20 minute virtual chat sometime next week to share your insights?
Thanks,
[Your Name]
            """)
        st.markdown("- **Follow-up after an Event/Meeting**:")
        st.code("""
Hi [Name],
It was great meeting you at [Event Name / Context] today. I particularly enjoyed our conversation about [Specific Topic]. I'd love to stay in touch.
Best,
[Your Name]
            """)
        st.markdown("---")
        st.markdown("#### Tip: Always be clear about your purpose, keep messages concise, and respect the other person's time.")
        if st.checkbox("Mark 'Networking Message Examples' Guide as Completed", key="networking_tools_complete"):
            st.session_state.get('completed_modules_jt', []).append('Networking Message Examples Guide')
            st.success("Excellent! You've learned about Networking Message Examples.")

# Run the function when the script is executed
if __name__ == "__main__":
    tools_jobtrack()
