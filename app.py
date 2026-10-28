import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# PAGE CONFIGURATION (Starter Code Base)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Froilan | Portfolio",
    page_icon="👋",
    layout="wide",
)

# ---------------------------------------------------------
# EXTRA 1: SESSION STATE (Persists data across reruns)
# ---------------------------------------------------------
if "feedback_entries" not in st.session_state:
    st.session_state.feedback_entries = []
if "fact_index" not in st.session_state:
    st.session_state.fact_index = 0

# ---------------------------------------------------------
# SIDEBAR: Profile Image, Student Info & Global Controls
# ---------------------------------------------------------
with st.sidebar:
    # EXTRA 2: Image (Replace URL with "profile.jpg" if using a local photo)
    st.image(
        "https://api.dicebear.com/7.x/avataaars/svg?seed=FroilanCando",
        caption="Johanne Froilan T. Cando (Profile Stand-in)",
        use_container_width=True,
    )

    st.markdown("### **Johanne Froilan T. Cando**")
    st.caption("BS Computer Science — 3rd Year")
    st.markdown("**University:** CIT University (CIT-U)")
    st.markdown("**Section:** BSCS - 3 (Update Section)")
    st.markdown("**Location:** Cebu City, Philippines")
    st.divider()

    # EXTRA 3: Download Button (Purposeful portfolio summary export)
    portfolio_summary = (
        "JOHANNE FROILAN T. CANDO\n"
        "BS Computer Science - 3rd Year | CIT University\n"
        "GitHub: github.com/Cratorixx\n\n"
        "CORE SKILLS:\n"
        "- Languages: Python, C#, Java, C++, Kotlin, TypeScript, SQL\n"
        "- Frameworks: React, Electron, Django, ASP.NET Core Blazor, Tailwind CSS\n\n"
        "FEATURED PROJECTS:\n"
        "1. Pharmacy Inventory System (Electron, React, SQLite - FEFO Indexing)\n"
        "2. Rain Before the Outbreak: Dengue Incidence Analysis (Python, Multiple Linear Regression)\n"
        "3. TindaTrack Inventory System (JavaFX, SQLite)\n"
        "4. PackageQueue Mobile App (Kotlin, MVP Architecture)\n"
    )
    st.download_button(
        label="📄 Download Portfolio Summary",
        data=portfolio_summary,
        file_name="Froilan_Cando_Portfolio.txt",
        mime="text/plain",
        use_container_width=True,
    )

# ---------------------------------------------------------
# HEADER SECTION: Clear Title & Visible Name/Section
# ---------------------------------------------------------
head_col1, head_col2 = st.columns([3, 1])

with head_col1:
    st.title("Johanne Froilan T. Cando")
    st.subheader("3rd-Year BS Computer Science Student | Software & Full-Stack Developer")
    st.write(
        "Welcome to my personal portfolio. I build desktop systems, modular web "
        "applications, and data-driven software with a focus on clean architecture."
    )

with head_col2:
    with st.container(border=True):
        st.markdown("**Academic Identification**")
        st.markdown("🎓 **Program:** BSCS - 3rd Year")
        st.markdown("🏫 **School:** CIT University")
        st.markdown("📌 **Section:** BSCS-3")

# EXTRA 4: Metrics Row (Easy-to-scan key figures)
m1, m2, m3, m4 = st.columns(4)
m1.metric(label="Academic Level", value="3rd Year", delta="BS Computer Science")
m2.metric(label="Featured Projects", value="4 Systems", delta="Desktop, Web & AI")
m3.metric(label="Tech Stack", value="10+ Tools", delta="Multi-Language")
m4.metric(label="Version Control", value="Git / GitHub", delta="Conventional Commits")

st.divider()

# ---------------------------------------------------------
# EXTRA 5: TABS (Grouped Sections for Scannability)
# ---------------------------------------------------------
tab_about, tab_skills, tab_projects, tab_contact = st.tabs([
    "👤 About & Autobiography",
    "📊 Skills & Proficiencies",
    "💻 Featured Projects",
    "📬 Contact & Feedback"
])

# =========================================================
# TAB 1: ABOUT & AUTOBIOGRAPHY
# =========================================================
with tab_about:
    col_bio, col_auto = st.columns([1, 1.6], gap="large")

    with col_bio:
        with st.container(border=True):
            st.header("About Me")
            st.write(
                "Hi! I'm **Froilan**, a third-year Computer Science student at "
                "**Cebu Institute of Technology – University (CIT-U)**. Originally from "
                "Bilar, Bohol, I moved to Cebu City to pursue my degree in computing."
            )
            st.write(
                "I enjoy designing software using modular patterns like **Model-View-Presenter (MVP)**, "
                "**Model-View-Template (MVT)**, and **Vertical Slicing**, pairing structured backend "
                "logic with clean, high-contrast interfaces."
            )

            st.divider()
            st.markdown("##### **Quick Facts Generator**")
            fun_facts = [
                "🏋️ Outside of coding, I follow a consistent 3-day weekly strength training routine.",
                "📐 I strictly follow the Conventional Commits specification across all my Git repositories.",
                "🎨 I love designing dark-mode dashboards with high-contrast accents and glassmorphism.",
                "🎮 In my downtime, I enjoy online multiplayer games, chess, and building custom game scripts."
            ]
            # WIDGET: Button (Used on purpose to cycle through personal facts)
            if st.button("🔄 Show Another Fact About Me", use_container_width=True):
                st.session_state.fact_index = (st.session_state.fact_index + 1) % len(fun_facts)
            st.info(fun_facts[st.session_state.fact_index])

    with col_auto:
        with st.container(border=True):
            st.header("Autobiography")

            # WIDGET: Radio (Used on purpose to switch reading modes)
            bio_view = st.radio(
                "Choose how to read my story:",
                ["Full Narrative", "Education & Milestones"],
                horizontal=True
            )

            if bio_view == "Full Narrative":
                st.markdown("#### **From Bohol to Cebu City**")
                st.write(
                    "I grew up in **Población, Bilar, Bohol**, where my curiosity for technology "
                    "started through tinkering with computers and online games. During Senior High School "
                    "at **Bohol Wisdom School**, I took the **STEM (Science, Technology, Engineering, "
                    "and Mathematics)** strand and graduated as a consistent honor student. Those years "
                    "solidified my foundation in analytical problem-solving and mathematics."
                )
                st.markdown("#### **Growing as a Computer Science Student**")
                st.write(
                    "Transitioning to university life in **Cebu City** at **CIT University** opened the "
                    "door to formal software engineering. Over the past three years, I have progressed from "
                    "learning fundamental C and Java syntax to architecting full-stack web apps, native "
                    "Android apps in Kotlin, and cross-platform desktop software with Electron and React. "
                    "Today, my coursework spans **Applied AI, Information Management, Digital Image Processing, "
                    "App Development, and Automata Theory**."
                )
            else:
                st.markdown("#### **Educational Background**")
                st.markdown(
                    "* **BS Computer Science (3rd Year)** — *Cebu Institute of Technology – University (Cebu City)*\n"
                    "* **Senior High School (STEM Strand, Honor Student)** — *Bohol Wisdom School (Bohol)*\n"
                    "* **Hometown:** Población, Bilar, Bohol"
                )
                st.markdown("#### **Key Academic Milestones**")
                st.markdown(
                    "1. **Foundation Year:** Mastered Object-Oriented Programming (OOP) in Java and C++ alongside core discrete structures.\n"
                    "2. **Sophomore Systems:** Built desktop and mobile applications (*TindaTrack* in JavaFX and *PackageQueue* in Kotlin MVP) with relational SQLite databases.\n"
                    "3. **Junior Year & Applied AI:** Developed *Rain Before the Outbreak* (a multi-city dengue regression study in Python) and engineered a *Pharmacy Inventory System* with FEFO stock indexing using Electron, React, and Tailwind CSS."
                )

# =========================================================
# TAB 2: SKILLS (Text, Table, and Chart with Purposeful Controls)
# =========================================================
with tab_skills:
    st.header("Technical Skills & Proficiencies")
    st.write(
        "Use the controls below to filter my technical stack by category, adjust the "
        "minimum proficiency threshold, or sort the dataset."
    )

    skills_df = pd.DataFrame({
        "Skill": [
            "Python", "SQL / SQLite", "C# / .NET Blazor", "Java / JavaFX",
            "JavaScript / TypeScript", "React & Electron", "Django",
            "Kotlin (Android)", "C++", "Git & GitHub"
        ],
        "Category": [
            "Languages", "Databases & Tools", "Frameworks & Web", "Languages",
            "Languages", "Frameworks & Web", "Frameworks & Web",
            "Languages", "Languages", "Databases & Tools"
        ],
        "Proficiency (%)": [90, 88, 84, 85, 86, 87, 83, 80, 78, 92],
        "Primary Use Case": [
            "Applied AI, Data Science & Scripting",
            "Relational Schema Design & Queries",
            "Interactive Web & Desktop Portfolios",
            "OOP Coursework & Desktop Inventory Apps",
            "Frontend Logic & Full-Stack Apps",
            "Cross-Platform Desktop Systems",
            "Modular MVT Web Applications",
            "MVP Mobile App Development",
            "Algorithms & Systems Programming",
            "Version Control & Conventional Commits"
        ]
    })

    # Interactive Filter Bar (Selectbox, Slider, Checkbox used on purpose)
    ctrl_col1, ctrl_col2, ctrl_col3 = st.columns([1.2, 1.5, 1])

    with ctrl_col1:
        # WIDGET: Selectbox
        selected_category = st.selectbox(
            "Filter by Category:",
            ["All Categories", "Languages", "Frameworks & Web", "Databases & Tools"]
        )

    with ctrl_col2:
        # WIDGET: Slider
        min_prof = st.slider(
            "Minimum Proficiency (%):",
            min_value=50,
            max_value=100,
            value=75,
            step=5
        )

    with ctrl_col3:
        st.write("")  # Alignment spacer
        # WIDGET: Checkbox
        sort_desc = st.checkbox("Sort Highest to Lowest", value=True)

    # Apply filters dynamically
    filtered_skills = skills_df[skills_df["Proficiency (%)"] >= min_prof]
    if selected_category != "All Categories":
        filtered_skills = filtered_skills[filtered_skills["Category"] == selected_category]
    if sort_desc:
        filtered_skills = filtered_skills.sort_values(by="Proficiency (%)", ascending=False)

    # Display Chart and Table Side-by-Side
    chart_col, table_col = st.columns([1.2, 1.3], gap="large")

    with chart_col:
        with st.container(border=True):
            st.subheader("Proficiency Visualization")
            if not filtered_skills.empty:
                st.bar_chart(
                    filtered_skills.set_index("Skill")["Proficiency (%)"],
                    height=360
                )
            else:
                st.warning("No skills match the selected filter criteria.")

    with table_col:
        with st.container(border=True):
            st.subheader("Detailed Skills Breakdown")
            st.dataframe(
                filtered_skills,
                use_container_width=True,
                hide_index=True,
                height=360
            )

# =========================================================
# TAB 3: PROJECTS (4 Specific Projects with Role, Tools, Outcome)
# =========================================================
with tab_projects:
    st.header("Featured Software & Academic Projects")
    st.write(
        "Below are specific applications and research projects I have designed and built. "
        "Use the filter below to highlight projects by domain."
    )

    # WIDGET: Multiselect (Used on purpose: dynamically shows/hides project cards!)
    project_domains = ["Desktop Systems", "Applied AI & Data Science", "Web Applications", "Mobile Development"]
    selected_domains = st.multiselect(
        "Filter displayed projects by domain:",
        options=project_domains,
        default=project_domains
    )

    projects_list = [
        {
            "title": "01. Pharmacy Inventory System (FEFO Indexing)",
            "domain": "Desktop Systems",
            "role": "Lead Full-Stack Desktop Developer",
            "tools": "Electron, React, Tailwind CSS v4, SQLite (better-sqlite3)",
            "description": (
                "Built a cross-platform desktop inventory application tailored for pharmacy stock management. "
                "Engineered native SQLite bindings and automated First-Expired, First-Out (FEFO) batch indexing "
                "to prioritize near-expiry medicine dispensing and prevent wastage."
            ),
            "outcome": "Outcome: Delivered sub-second local database queries and automated expiration alerts.",
            "link": "https://github.com/Cratorixx"
        },
        {
            "title": "02. Rain Before the Outbreak: Dengue Incidence Study",
            "domain": "Applied AI & Data Science",
            "role": "Data Science Researcher & Developer",
            "tools": "Python, Pandas, Scikit-Learn, Multiple Linear Regression, Matplotlib",
            "description": (
                "Conducted an Applied AI (CS365) study analyzing multi-week lagged weather variables "
                "(rainfall, temperature, humidity) against Department of Health (DOH) dengue incidence counts "
                "across 8 Philippine cities."
            ),
            "outcome": "Outcome: Modeled multi-week meteorological lag effects to predict outbreak surges.",
            "link": "https://github.com/Cratorixx"
        },
        {
            "title": "03. TindaTrack Desktop Inventory",
            "domain": "Desktop Systems",
            "role": "Software Developer",
            "tools": "Java, JavaFX, SQLite, JDBC",
            "description": (
                "Developed a structured retail and sari-sari store inventory management desktop app. "
                "Implemented CRUD operations, low-stock threshold indicators, and persistent local "
                "SQLite storage through a clean JavaFX user interface."
            ),
            "outcome": "Outcome: Streamlined item tracking and sales logging for small-scale retail workflows.",
            "link": "https://github.com/Cratorixx"
        },
        {
            "title": "04. PackageQueue & SulitDiri PH",
            "domain": "Mobile Development",
            "role": "Mobile & Web Developer",
            "tools": "Kotlin (Android MVP), Django (Python MVT)",
            "description": (
                "Architected PackageQueue in Kotlin using strict Model-View-Presenter (MVP) separation for "
                "parcel queue tracking, alongside SulitDiri PH, a multi-category price and value comparison "
                "web platform built in Django using Vertical Slicing."
            ),
            "outcome": "Outcome: Demonstrated clean modular architecture across both mobile and web stacks.",
            "link": "https://github.com/Cratorixx"
        }
    ]

    # Filter projects based on the multiselect widget
    visible_projects = [p for p in projects_list if p["domain"] in selected_domains]

    if not visible_projects:
        st.info("Select at least one domain above to view projects.")
    else:
        proj_cols = st.columns(2, gap="large")
        for idx, proj in enumerate(visible_projects):
            with proj_cols[idx % 2]:
                with st.container(border=True):
                    st.subheader(proj["title"])
                    st.caption(f"Category: {proj['domain']}")
                    st.markdown(f"**My Role:** {proj['role']}")
                    st.markdown(f"**Tools Used:** `{proj['tools']}`")
                    st.write(proj["description"])
                    st.success(proj["outcome"])
                    st.markdown(f"[🔗 View on GitHub ({proj['link']})]({proj['link']})")

# =========================================================
# TAB 4: CONTACT & FEEDBACK FORM (Responds after submission)
# =========================================================
with tab_contact:
    st.header("Contact & Portfolio Feedback")
    st.write(
        "Have a question about one of my projects or want to leave feedback on this portfolio? "
        "Fill out the form below and it will respond immediately."
    )

    form_col, log_col = st.columns([1.4, 1], gap="large")

    with form_col:
        # EXTRA 6: Form Component
        with st.form("portfolio_feedback_form", clear_on_submit=True):
            st.subheader("Send a Message")
            # WIDGET: Text Inputs
            visitor_name = st.text_input("Your Name *", placeholder="e.g., Juan Dela Cruz")
            visitor_email = st.text_input("Your Email *", placeholder="e.g., juan@cit.edu")

            # WIDGET: Selectbox & Slider inside form
            reason = st.selectbox(
                "Subject:",
                ["Classmate / Peer Feedback", "Instructor Evaluation", "Project Collaboration", "General Inquiry"]
            )
            rating = st.slider("Rate this Portfolio Layout (1 = Needs Work, 5 = Excellent):", 1, 5, 5)

            # WIDGET: Text Area
            comments = st.text_area(
                "Message / Feedback *",
                placeholder="Share your thoughts or questions here..."
            )

            submitted = st.form_submit_button("📨 Submit Feedback", use_container_width=True)

            if submitted:
                if visitor_name.strip() and visitor_email.strip() and comments.strip():
                    st.session_state.feedback_entries.append({
                        "name": visitor_name.strip(),
                        "email": visitor_email.strip(),
                        "reason": reason,
                        "rating": rating,
                        "comments": comments.strip()
                    })
                    st.success(
                        f"Thank you, **{visitor_name}**! Your **{reason}** submission "
                        f"(Rating: {rating}/5) has been recorded."
                    )
                    st.balloons()
                else:
                    st.error("Please fill in your Name, Email, and Message before submitting.")

    with log_col:
        with st.container(border=True):
            st.subheader("Session Responses")
            st.write("Messages submitted during this session appear here:")
            if st.session_state.feedback_entries:
                for entry in reversed(st.session_state.feedback_entries):
                    with st.container(border=True):
                        st.markdown(f"**{entry['name']}** ({entry['reason']}) — ⭐ **{entry['rating']}/5**")
                        st.write(entry["comments"])
            else:
                st.caption("No feedback submitted yet in this session. Try submitting the form!")