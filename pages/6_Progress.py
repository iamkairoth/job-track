# pages/Progress.py
import streamlit as st

def progress_jobtrack():
    # Set page configuration
    st.set_page_config(page_title="JobTrack - Progress", layout="wide")

    st.title("Your Progress: Celebrating Your Career Milestones")
    st.sidebar.header("Progress")

    st.write("Your career journey isn't just about the jobs you apply for – it's about what you learn, the skills you develop, and the strategies you implement. This page highlights your growth with JobTrack, celebrating every educational module completed and every strategic playbook you've engaged with.")
    st.write("See how far you've come in mastering job search concepts and staying consistent with your learning and strategic actions.")

    st.markdown("---")

    # Navigation for different sections within Progress
    selected_section = st.sidebar.selectbox(
        "Select a section to explore:",
        options=["Overview", "Fundamentals Progress", "Playbooks Progress", "Milestones"],
        help="Choose a section to audit your progress and celebrate your achievements."
    )

    # Fetching data from session state (assuming it's set in other pages)
    assessment_completed = True if st.session_state.get('assessment_results_jt') else False
    completed_fundamentals = st.session_state.get('completed_modules_jt', [])
    completed_playbooks = st.session_state.get('completed_playbooks_jt', [])
    user_custom_playbooks = st.session_state.get('user_custom_playbooks_jt', {})

    if selected_section == "Overview":
        st.markdown("### Your Career Journey at a Glance:")

        if assessment_completed:
            st.success("✅ **Assessment Completed!** You've defined your starting point.")
        else:
            st.info("💡 **Assessment Pending:** Complete your assessment to get personalized recommendations!")
            if st.button("Go to Assessment", key="go_to_assessment_from_progress"):
                st.switch_page("pages/Assessment.py")

        st.markdown(f"#### Learning & Development:")
        st.info(f"You've completed **{len(set(completed_fundamentals))}** unique Fundamentals modules!") # Using set to count unique modules
        st.info(f"You've explored **{len(set(completed_playbooks))}** Pre-Defined Playbooks.")
        st.info(f"You've created **{len(user_custom_playbooks)}** custom Playbooks.")

        st.markdown("#### Your Progress Checklist:")
        if 'assessment_results_jt' in st.session_state:
            st.checkbox("Completed Initial Assessment", value=True, disabled=True)
        else:
            st.checkbox("Completed Initial Assessment", value=False, disabled=True)

        st.checkbox("Explored Career Fundamentals", value=len(set(completed_fundamentals)) > 0, disabled=True)
        st.checkbox("Reviewed Job Search Tools & Guides", value=any(item.endswith('Guide') for item in set(completed_fundamentals)), disabled=True) # Check if any tool guide was marked complete
        st.checkbox("Engaged with Playbooks", value=len(set(completed_playbooks)) > 0 or len(user_custom_playbooks) > 0, disabled=True)


    elif selected_section == "Fundamentals Progress":
        st.markdown("### Career Fundamentals Progress:")
        if completed_fundamentals:
            st.write("Here are the fundamental topics you've marked as completed:")
            for module in sorted(list(set(completed_fundamentals))): # Display unique and sorted modules
                st.markdown(f"- ✅ {module}")
        else:
            st.info("You haven't marked any Fundamentals modules as completed yet. Head over to the 'Fundamentals' page to start learning!")
            if st.button("Go to Fundamentals", key="go_to_fundamentals_from_progress_fundamentals"):
                st.switch_page("pages/Fundamentals.py")

    elif selected_section == "Playbooks Progress":
        st.markdown("### Playbooks Progress:")
        if completed_playbooks:
            st.write("You've explored these Pre-Defined Playbooks:")
            for playbook in sorted(list(set(completed_playbooks))):
                st.markdown(f"- ✅ {playbook}")
        else:
            st.info("You haven't marked any Pre-Defined Playbooks as completed yet. Explore the 'Playbook' page to find a strategy that fits you!")
            if st.button("Go to Playbook", key="go_to_playbook_from_progress_playbooks"):
                st.switch_page("pages/Playbook.py")

        st.markdown("#### Your Custom Playbooks:")
        if user_custom_playbooks:
            for name, tasks in user_custom_playbooks.items():
                with st.expander(f"**{name}** ({len(tasks)} steps)"):
                    for task in tasks:
                        st.write(f"- {task}")
        else:
            st.info("You haven't created any custom playbooks yet. Visit the 'Playbook' page to design your own!")
            if st.button("Build a Custom Playbook", key="build_custom_playbook_from_progress"):
                st.switch_page("pages/Playbook.py")


    elif selected_section == "Milestones":
        st.markdown("### Your Career Learning Milestones:")
        st.write("Celebrate your achievements in building knowledge and strategy!")

        # Example milestones - you can add more complex logic later
        if assessment_completed:
            st.success("🏆 **Milestone Achieved:** Completed your initial Career Assessment!")
        if len(set(completed_fundamentals)) >= 3:
            st.balloons()
            st.success("🏅 **Milestone Achieved:** Mastered 3+ Core Career Fundamentals!")
        if len(set(completed_fundamentals)) >= 7:
            st.balloons()
            st.success("🌟 **Milestone Achieved:** Become a Career Fundamentals Expert!")
        if len(set(completed_playbooks)) >= 1 or len(user_custom_playbooks) >= 1:
            st.success("🏆 **Milestone Achieved:** Engaged with your first Job Search Playbook!")
        if len(user_custom_playbooks) >= 3:
            st.balloons()
            st.success("🏅 **Milestone Achieved:** Designed 3+ Custom Career Playbooks!")

        if not (assessment_completed or len(set(completed_fundamentals)) >= 3 or len(set(completed_playbooks)) >= 1 or len(user_custom_playbooks) >= 1):
            st.info("Keep exploring and learning to unlock your first milestones!")

# Run the function when the script is executed
if __name__ == "__main__":
    progress_jobtrack()
