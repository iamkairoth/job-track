# pages/Playbook.py
import streamlit as st

def playbook_jobtrack():
    # Set page configuration
    st.set_page_config(page_title="JobTrack - Playbook", layout="wide")

    st.title("Your Job Search Playbook: Strategic Action Plans")
    st.sidebar.header("Playbook")

    st.write("Whether you need a ready-made strategic roadmap or want to design your own, this section is your go-to for structured career action. We provide you with the frameworks to build effective job search plans, ensuring you're always strategizing smart.")

    st.markdown("---")

    # Navigation for different sections within Playbook
    selected_section = st.sidebar.selectbox(
        "Select a playbook type:",
        options=["Overview", "Pre-Defined Playbooks", "Build Your Own Playbook"],
        help="Choose to explore curated strategies or create your custom plan."
    )

    if selected_section == "Overview":
        st.markdown("### Choose your path to career success:")
        st.markdown("- **Pre-Defined Playbooks**: Curated action plans designed for common job search scenarios, ready for you to follow.")
        st.markdown("- **Build Your Own Playbook**: Create custom action plans by defining your own steps and tasks, tailored to your unique journey.")

    elif selected_section == "Pre-Defined Playbooks":
        st.markdown("### Pre-Defined Playbooks: Expert-Designed Roadmaps, Ready for You.")
        st.write("Take the guesswork out of your job hunt with our expertly crafted playbooks. Each plan is designed with a specific career goal, experience level, or challenge in mind. Simply choose the playbook that fits you, and we'll guide you through the structure, linking to all the necessary educational content from our Fundamentals and Tools sections.")

        st.markdown("#### Explore Our Playbooks:")

        # Playbook 1: Entry-Level Job Hunt
        st.expander("🚀 **Entry-Level Job Hunt: Your First 30 Days**").markdown("""
        **Goal:** Secure your first professional role.
        **Ideal for:** Students, recent graduates, or those with minimal professional experience.
        **Focus:** Building foundational application materials, identifying entry-level roles, and basic networking.

        **Key Steps:**
        1.  **Week 1: Resume & LinkedIn Foundations**
            * Review "Resume Writing" fundamentals.
            * Optimize your LinkedIn profile using "Personal Branding" tips.
            * Craft a master resume.
        2.  **Week 2: Targeted Applications & Cover Letters**
            * Research target companies and roles.
            * Learn "Cover Letter Structure" and tailor 5 applications.
        3.  **Week 3: Networking & Informational Interviews**
            * Review "Networking" fundamentals.
            * Send 10 LinkedIn connection requests (using "Networking Message Examples").
            * Aim for 1-2 informational interviews.
        4.  **Week 4: Interview Prep & Follow-Up**
            * Practice common "Interview Question Types."
            * Prepare for typical behavioral questions.
            * Learn effective follow-up strategies.
        """)
        if st.checkbox("Mark 'Entry-Level Job Hunt' Playbook as Completed", key="entry_level_playbook_complete"):
            st.session_state.get('completed_playbooks_jt', []).append('Entry-Level Job Hunt')
            st.success("Great work! You've marked 'Entry-Level Job Hunt' Playbook as completed.")


        # Playbook 2: Career Change Sprint
        st.expander("🔄 **Career Change Sprint: Pivoting Your Path**").markdown("""
        **Goal:** Successfully transition into a new industry or role.
        **Ideal for:** Professionals looking to make a significant career pivot.
        **Focus:** Identifying transferable skills, targeted networking, and re-framing experience.

        **Key Steps:**
        1.  **Phase 1: Self-Assessment & Skill Mapping**
            * Identify transferable skills using "Assessment" insights.
            * Research target industries/roles (Fundamentals: "Job Search Strategy").
        2.  **Phase 2: Networking for Insights**
            * Connect with 10-15 professionals in the new industry (Networking: "Informational Interview Request").
            * Learn industry-specific language and challenges.
        3.  **Phase 3: Re-packaging Your Experience**
            * Revamp resume/LinkedIn for the new industry (Fundamentals: "Resume Writing", "Personal Branding").
            * Practice answering "Why the career change?" (Interview Skills).
        """)
        if st.checkbox("Mark 'Career Change Sprint' Playbook as Completed", key="career_change_playbook_complete"):
            st.session_state.get('completed_playbooks_jt', []).append('Career Change Sprint')
            st.success("Excellent! You've marked 'Career Change Sprint' Playbook as completed.")

        # Add more pre-defined playbooks as needed...

    elif selected_section == "Build Your Own Playbook":
        st.markdown("### Build Your Own Playbook: Design Your Custom Career Plan.")
        st.write("Ready to take control? Use this section to design custom action plans that perfectly match your unique career goals and situation. Define your steps, set your milestones, and make your job search truly yours.")
        st.markdown("#### Tips for Building Your Playbook:")
        st.markdown("- **Break it down**: Divide your job search into manageable phases (e.g., 'Research', 'Preparation', 'Application', 'Networking', 'Interviewing').")
        st.markdown("- **Be specific**: Instead of 'Apply for jobs,' try 'Apply for 3 jobs per week in my target industry.'")
        st.markdown("- **Integrate learning**: Link your tasks to relevant sections in our 'Fundamentals' and 'Tools' pages.")
        st.markdown("- **Review and adapt**: Your playbook is a living document. Adjust it as you learn and progress.")

        # Input fields for custom playbook
        playbook_name = st.text_input("Name Your Playbook:", key="custom_playbook_name")
        st.markdown("#### Add Steps to Your Playbook:")

        # Using session state to manage dynamic tasks
        if 'custom_playbook_tasks' not in st.session_state:
            st.session_state.custom_playbook_tasks = [""] # Start with one empty task

        for i, task in enumerate(st.session_state.custom_playbook_tasks):
            col1, col2 = st.columns([0.9, 0.1])
            with col1:
                st.session_state.custom_playbook_tasks[i] = st.text_input(f"Step {i+1}", value=task, key=f"task_{i}_jt")
            with col2:
                if st.button("X", key=f"remove_task_{i}_jt"):
                    del st.session_state.custom_playbook_tasks[i]
                    st.rerun() # Rerun to update the list

        if st.button("Add Another Step", key="add_task_jt"):
            st.session_state.custom_playbook_tasks.append("")
            st.rerun() # Rerun to add new input field

        if st.button("Save My Custom Playbook", key="save_custom_playbook_jt"):
            if playbook_name and any(st.session_state.custom_playbook_tasks):
                # Simple save mechanism for non-commercial MVP
                # In a real app, you'd save this to a database
                if 'user_custom_playbooks_jt' not in st.session_state:
                    st.session_state.user_custom_playbooks_jt = {}
                st.session_state.user_custom_playbooks_jt[playbook_name] = st.session_state.custom_playbook_tasks
                st.success(f"Playbook '{playbook_name}' saved!")
                st.session_state.custom_playbook_tasks = [""] # Reset for next playbook
                st.session_state.custom_playbook_name = "" # Clear name
                st.rerun()
            else:
                st.warning("Please name your playbook and add at least one step.")

        if 'user_custom_playbooks_jt' in st.session_state and st.session_state.user_custom_playbooks_jt:
            st.markdown("#### Your Saved Custom Playbooks:")
            for name, tasks in st.session_state.user_custom_playbooks_jt.items():
                with st.expander(f"**{name}**"):
                    for i, task in enumerate(tasks):
                        st.write(f"- {task}")


# Run the function when the script is executed
if __name__ == "__main__":
    playbook_jobtrack()
