import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
from st_on_hover_tabs import on_hover_tabs
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import streamlit_analytics
import base64
from streamlit_extras.mention import mention
from streamlit_extras.app_logo import add_logo
#from bs4 import BeautifulSoup
from streamlit_extras.echo_expander import echo_expander


#Set Page Title
st.set_page_config(page_title="Nick Sofianakos",page_icon = "ice_hockey_stick_and_puck", layout="wide", initial_sidebar_state="auto")

#Including style.css file 
st.markdown('<style>' + open('style.css').read() + '<style>', unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def render_lottie(url, width, height):
    lottie_html = f"""
    <html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.7.14/lottie.min.js"></script>
    </head>
    <body>
        <div id="lottie-container" style="width: {width}; height: {height};"></div>
        <script>
            var animation = lottie.loadAnimation({{
                container: document.getElementById('lottie-container'),
                renderer: 'svg',
                loop: true,
                autoplay: true,
                path: '{url}'
            }});
            animation.setRendererSettings({{
                preserveAspectRatio: 'xMidYMid slice',
                clearCanvas: true,
                progressiveLoad: false,
                hideOnTransparent: true
            }});
        </script>
    </body>
    </html>
    """
    return lottie_html

#Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

footer = """
footer{
    visibility:visible;
}
footer:after{
    content:'Copyright © 2023 Harry Chang';
    position:relative;
    color:black;
}
"""
#Images for about me
img_me=Image.open("images/Me.jpg")
img_VGK=Image.open("images/NickVGK.jpg")
img_JW=Image.open("images/Jaywrightpic.jpg")

#Images for experience
img_EY=Image.open("images/EYLogo.png")
img_CBB=Image.open("images/CBB.png")
img_ECI=Image.open("images/ECILogo.png")
img_FIN=Image.open("images/FinTechLogo.png")
img_FIN2=Image.open("images/FinTechLogo.jpg")

#Images for Education
img_NovaU=Image.open("images/NovaU.png")
img_NovaLogo=Image.open("images/Nova.png")
img_ALJ1=Image.open("images/ALJ.png")
img_ALJ2=Image.open("images/ALJ (1).png")

#####################
#Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  with col2:
    b_no_commas = b.replace(',', '')
    st.markdown(b_no_commas)

def txt4(a, b):
  col1, col2 = st.columns([1.5,2])
  with col1:
    st.markdown(f'<p style="font-size: 25px; color: white;">{a}</p>', unsafe_allow_html=True)
  with col2: #can't seem to change color besides green
    st.markdown(f'<p style="font-size: 25px; color: red;"><code>{b}</code></p>', unsafe_allow_html=True)

#####################

#The background image of the website is done here!
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('bg2.jpg') 



def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 20px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "linkedin": "https://img.icons8.com/ios-filled/100/000000/linkedin.png",
                "github": "https://img.icons8.com/ios-filled/100/000000/github--v2.png",
                "email": "https://img.icons8.com/ios-filled/100/000000/filled-message.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html



# Sidebar: If using streamlit_option_menu
with st.sidebar:
    with st.container():
        l, m, r = st.columns((1,3,1))
        with l:
            st.empty()
        with m:
            st.empty()
        with r:
            st.empty()
    
    choose = option_menu(
                        "Nick Sofianakos", 
                        ["About Me", "Experience", "Technical Skills", "Education", "Projects", "Awards & Certifications"],
                         icons=['person fill',  'clock history', 'tools', 'book half', 'clipboard', 'trophy fill', ],
                         menu_icon="mortarboard", 
                         default_index=0,
                         styles={
        "container": {"padding": "0!important", "background-color": "#cc0000"},
        "icon": {"color": "#000000", "font-size": "20px"}, 
        "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#eee", "color": "#000000"},
        "nav-link-selected": {"background-color": "#cc0000", "color": "#000000"},
        "menu-title": {"color": "#000000"}
    }
    )
  
    linkedin_url = "https://www.linkedin.com/in/nick-sofianakos/"
    github_url = "https://github.com/Nick3429"
    email_url = "mailto:nsofianakos@gmail.com"
    with st.container():
        l, m, r = st.columns((0.11,2,0.1))
        with l:
            st.empty()
        with m:
            st.markdown(
                social_icons(30, 30, LinkedIn=linkedin_url, GitHub=github_url,  Email=email_url),
                unsafe_allow_html=True)
        with r:
            st.empty()

st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
st.title("Nick Sofianakos")
# Create header
if choose == "About Me":
    #aboutme.createPage()
    with st.container():
        left_column, middle_column, right_column = st.columns((1,0.2,0.5))
        with left_column:
            st.header("About Me")
            st.write("Email: nsofianakos@gmail.com")
            st.write("Cell Number: 732-397-0761")
            st.subheader("Aspiring Data Analyst/Data Scientist/Consultant")
            st.write("👋🏻 Hi, I'm Nick! I'm a recent 2024 graduate of Villanova University. I graduated magna cum laude with a bachelor of science in computer engineering, and also received minors in both statistics and computer science.")
            st.write("In my freetime, I like to exercise in the gym, run, and play sports (especially hockey). ")
            st.write("👨🏼‍💻 Academic interests: Data Visualization, Dashboarding, Data Analysis, Natural Language Processing")
            st.write("💭 Ideal Career Paths: Data Analyst, Data Scientist, Artificial Intelligence Engineer, Technology Consultant, Product Manager")
           # st.write("📄 [Resume (1 page)](https://drive.google.com/file/d/164EEVH6BmvC89q2M4WsBNF1JyddDAbNY/view?usp=sharing)")
        with middle_column:
            st.empty()
        with right_column:
            st.image(img_me)

# Create section for Work Experience
elif choose == "Experience":
    #st.write("---")
    st.header("Experience")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_EY)
        with text_column:
            st.subheader("Technology Consulting Intern, [EY](https://www.ey.com/en_us)")
            st.write("*Summer 2023*")
            st.markdown("""
            Developed a ChatGPT Plugin, streamlining the customer inquiry process and enhancing the client's market presence. Conducted in-depth research on leveraging generative AI to drive revenue growth and foster business expansion for the client.
                        
            `Python` `OpenAI` `Langchain` `Streamlit`
            """)
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.write(" ")
            st.write(" ")
            st.write(" ")
            st.write(" ")
            st.image(img_CBB)
        with text_column:
            st.subheader("Data Science Intern, [CBB Analytics](https://cbbanalytics.com/)")
            st.write("*Winter-Spring 2023*")
            st.markdown("""
            Devised an advanced suite of college basketball streakiness metrics, empowering clients to make more informed decisions. Pioneered a daily newsletter, delivering essential statistical highlights from previous nights' conference games to clients each morning, facilitating real time updates on their opponents.
            
            `Python`  `SQL` `Google BigQuery` `Pandas` `Numpy` 
            """)
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.write(" ")
            st.write(" ")
            st.image(img_ECI)
        with text_column:
            st.subheader("Intern, [Eze Castle Integration](https://www.eci.com/)")
            st.write("*Summer 2022*")
            st.markdown("""
            Audited and migrated existing scripts to GitHub to ensure scripts being used in production are up to date. Developed test scripts written in PowerShell to validate client servers are correctly configured. Created Azure resource topology diagrams in PowerShell to reveal interconnectedness of technology resources.

            `Python` `Git` `GitHub` `Jira` `ElasticSearch` `PowerShell` `Azure`
            """)
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.write(" ")
            st.write(" ")
            st.write(" ")
            st.image(img_FIN)
        with text_column:
            st.subheader("Intern at FinTech Focus")
            st.write("*Summer 2020*")
            st.markdown("""
            Developed full-stack web applications using the Flask web framework, MongoDB, Python, HTML, and CSS. Co-created a website called TravelEase which uses HTML extensions and API's, which helps travelers in need of currency conversions, restaurant locations, and flights to their vacation destinations.

            `Flask` `MongoDB` `Python` `HTML` `CSS` `API's`
            """)
    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:0px;
    }
    </style>
    ''', unsafe_allow_html=True)
#st.write("##")

# Create section for Technical Skills
elif choose == "Technical Skills":
    #st.write("---")
    st.header("Technical Skills")
    txt3("Programming Languages","`Python`, `R`, `SQL`, `HTML` ,`CSS`, `PowerShell`, `JavaScript (Work in Progress)`, `Java`, `C`, `C++`, `MATLAB`")
    txt3("Academic Interests","`Data Visualization`, `Data Analysis`, `Statistical Modeling`, `Natural Language Processing`")
    txt3("Data Visualization", "`ggplot2`, `matplotlib`, `seaborn`, `Plotly`")
    txt3("Database Systems", "`MySQL`, `NoSQL`, `Google BigQuery`, `MongoDB`")
    txt3("Cloud Platforms", "`Google Cloud Platform`, `Amazon Web Services`, `Heroku`, `Streamlit Cloud`")
    txt3("Version Control", "`Git`")
    txt3("Design and Front-end Development", "`HTML`, `CSS`, `Streamlit`, `Wordpress`, `Bootstrap`, `React (Work in Progress)`")
    txt3("Data Science Techniques", "`Regression`, `XGBoost`, `Random Forest`, `Decison Trees`")
    txt3("Machine Learning Frameworks", "`Numpy`, `Pandas`, `Scikit-Learn`")
    txt3("Task Management Tools", "`Slack`, `Jira`")
    txt3("Technologies", "`ChatGPT`, `Heroku`, `Microsoft Word`, `Microsoft PowerPoint`, `Google Docs`, `Google Slides`")


# Create section for Education
#st.write("---")
elif choose == "Education":
    # st.header("Education")
    # selected_options = ["Summary", "Modules"
    #                     ]
    # selected = st.selectbox("Which section would you like to read?", options = selected_options)
    # st.write("Current selection:", selected)
    # if selected == "Summary":
        st.subheader("Summary")
        st.write("*Summary of education from high school and university*")
        with st.container():
            image_column, text_column = st.columns((1,2.5))
            with image_column:
                st.write(" ")
                st.write(" ")
                st.image(img_NovaLogo)
            with text_column:
                st.subheader("Bachelor of Science - [Computer Engineering](https://www1.villanova.edu/university/engineering/academic-programs/departments/electrical-computer/bs-computer-engineering.html), [Villanova University](https://www1.villanova.edu/university.html) (2020-2024)")
                st.write("Relevant Coursework: Engineering Programming and Applications, C++, Algorithms, and Data structures, Fundamentals of MATLAB, Fundamentals of Computer Engineering I, Fundamentals of Computer Engineering II, Discrete Structures, Statistical Methods, Java Bootcamp, Computer Architecture, Digital Electronics, Operating Systems, Engineering Probability and Statistics, Data Science, Computer Networks, Computer Ethics, Applied Statistical Modeling, Principles of Database Systems, Math Stat 1, Artificial Intelligence, Platform Computing, Public Speaking")
                st.markdown("Clubs/Organizations:")
                st.markdown("""
                - [Villanova Sports Analytics Club](https://sportsanalyticsatnova.com/) - President
                - [Insitution of Electrical and Electronic Engineers](https://www.ieee.org/) - Treasurer
                - [Villanova Blue and White Scholarship Foundation](https://www.bluewhitescholarship.org/) 
                - Villanova Club Roller Hockey - Vice President
                """)
        with st.container():
            image_column, text_column = st.columns((1,2.5))
            with image_column:
                st.write(" ")
                st.image(img_ALJ1)
            with text_column:
                st.subheader("High School Diploma - [Arthur L. Johnson High School](https://alj.clarkschools.org/) (2016-2020)")
                st.write("Coursework: English, Mathematics, Science, History, Computer Science, Literature, Italian, Gym, Pupetry")
                st.markdown("Clubs/Organizations:")
                st.markdown(""" 
                - Varsity Ice Hockey
                - Key Club
                - National Honors Society
                - Robotics Club
                """)
    # elif selected == "Modules":
    #     st.subheader("Modules")
    #     st.write("*List of modules taken at National University of Singapore*")
    #     with st.container():
    #         sem1, mid, sem2 = st.columns((1,0.1,1))
    #         with sem1:
    #             st.write("**Academic Year 2019/20 Semester 1**")
    #             st.markdown("""
    #             |Code|Module Title                       |Workload|
    #             |--------|--------------------------------------|---------|
    #             |AY1130| Human Anatomy and Physiology I       |4 MCs|
    #             |GER1000| Quantitative Reasoning              |4 MCs|
    #             |PR1110A| Foundations for Medicinal Chemistry |4 MCs|
    #             |PR1111A|Pharmaceutical Biochemistry          |4 MCs|
    #             |ST1232| Statistics for Life Sciences         |4 MCs|
    #             """)
    #             st.write("")
    #             st.markdown("""
    #             Total Workload for Semester: **20 Modular Credits (MCs)**
    #             """)
    #         with mid:
    #             st.empty()
    #         with sem2:
    #             st.write("**Academic Year 2020/21 Semester 1**")
    #             st.markdown("""
    #             |Code|Module Title                       |Workload|
    #             |--------|--------------------------------------|---------|
    #             |CS1010S|Programming Methodology|4 MCs|
    #             |DSA1101|Introduction to Data Science|4 MCs|
    #             |GER1000|Quantitative Reasoning|4 MCs|
    #             |MA1102R|Calculus|4 MCs|
    #             |SP1541|Exploring Science Communication Through Popular Science|4 MCs|
    #             """)
    #             st.write("")
    #             st.markdown("""
    #             Total Workload for Semester: **20 Modular Credits (MCs)**
    #             """)
    #     with st.container():
    #         sem1, mid, sem2 = st.columns((1,0.1,1))
    #         with sem1:
    #             st.write("**Academic Year 2020/21 Semester 2**")
    #             st.markdown("""
    #             |Code|Module Title                       |Workload|
    #             |--------|--------------------------------------|---------|
    #             |CFG1002|Career Catalyst|2 MCs|
    #             |EC1301|Principles of Economics|4 MCs|
    #             |GEQ1000|Asking Questions|4 MCs|
    #             |GES1010|Nation-Building in Singapore|4 MCs|
    #             |GET1030|Computers and the Humanities|4 MCs|
    #             |MA1101R|Linear Algebra I|4 MCs|
    #             |ST2131|Probability|4 MCs|
    #             """)
    #             st.write("")
    #             st.markdown("""
    #             Total Workload for Semester: **26 Modular Credits (MCs)**
    #             """)
    #         with mid:
    #             st.empty()
    #         with sem2:
    #             st.write("**Academic Year 2020/21 Special Term (Part II)**")
    #             st.markdown("""
    #             |Code|Module Title                       |Workload|
    #             |--------|--------------------------------------|---------|
    #             |CS2040|Data Structures and Algorithms|4 MCs|
    #             """)
    #             st.write("")
    #             st.markdown("""
    #             Total Workload for Semester: **4 Modular Credits (MCs)**
    #             """)
    #     with st.container():
    #         sem1, mid, sem2 = st.columns((1,0.1,1))
    #         with sem1:
    #             st.write("**Academic Year 2021/22 Semester 1**")
    #             st.markdown("""
    #             |Code|Module Title                       |Workload|
    #             |--------|--------------------------------------|---------|
    #             |DSA2102|Essential Data Analytics Tools: Numerical Computation|4 MCs|
    #             |EC2101|Microeconomic Analysis I|4 MCs|
    #             |EC2102|Macroeconomic Analysis I|4 MCs|
    #             |EC2204|Financial Accounting for Economists|4 MCs|
    #             |EC3305|Programming Tools for Economics|4 MCs|
    #             |GEH1049|Public Health in Action|4 MCs|
    #             """)
    #             st.write("")
    #             st.markdown("""
    #             Total Workload for Semester: **24 Modular Credits (MCs)**
    #             """)
    #         with mid:
    #             st.empty()
    #         with sem2:
    #             st.write("**Academic Year 2021/22 Semester 2**")
    #             st.markdown("""
    #             |Code|Module Title                       |Workload|
    #             |--------|--------------------------------------|---------|
    #             |ALS1010|Learning to Learn Better|2 MCs|
    #             |DSA2101|Essential Data Analytics Tools: Data Visualization|4 MCs|
    #             |GES1037|A History of Singapore in Ten Objects|4 MCs|
    #             |IS1103|Ethics in Computing|4 MCs|
    #             |IT2002|Database Technology and Management|4 MCs|
    #             |MA2104|Multivariable Calculus|4 MCs|
    #             |ST2132|Mathematical Statistics|4 MCs|
    #             """)
    #             st.write("")
    #             st.markdown("""
    #             Total Workload for Semester: **26 Modular Credits (MCs)**
    #             """)
    #     with st.container():
    #         sem1, mid, sem2 = st.columns((1,0.1,1))
    #         with sem1:
    #             st.write("**Academic Year 2022/23 Semester 1**")
    #             st.markdown("""
    #             |Code|Module Title                       |Workload|
    #             |--------|--------------------------------------|---------|
    #             |CFG1003|Financial Wellbeing - Introduction|0 MCs|
    #             |CS3244|Machine Learning|4 MCs|
    #             |DSA3101|Data Science in Practice|4 MCs|
    #             |DSA3102|Essential Data Analytics Tools: Convex Optimization|4 MCs|
    #             |ST3131|Regression Analysis|4 MCs|
    #             |ST3248|Statistical Learning I|4 MCs|
    #             """)
    #             st.write("")
    #             st.markdown("""
    #             Total Workload for Semester: **20 Modular Credits (MCs)**
    #             """)
    #         with mid:
    #             st.empty()
    #         with sem2:
    #             st.write("**Academic Year 2022/23 Semester 2**")
    #             st.markdown("""
    #             |Code|Module Title                       |Workload|
    #             |--------|--------------------------------------|---------|
    #             |DSA4212|Optimization for Large-Scale Data-Driven Inference|4 MCs|
    #             |LSM1301|General Biology|4 MCs|
    #             |ST4248|Statistical Learning II|4 MCs|
    #             """)
    #             st.write("")
    #             st.markdown("""
    #             Total Workload for Semester: **12 Modular Credits (MCs)**
    #             """)
    #     with st.container():
    #         sem1, mid, sem2 = st.columns((1,0.1,1))
    #         with sem1:
    #             st.write("**Academic Year 2023/24 Semester 1**")
    #             st.markdown("""
    #             |Code|Module Title                       |Workload|
    #             |--------|--------------------------------------|---------|
    #             |CS4225|Big Data Systems for Data Science|4 MCs|
    #             |DSA4199|Applied Project in Data Science and Analytics|8 MCs|
    #             """)
    #             st.write("")
    #             st.markdown("""
    #             Total Workload for Semester: **12 Modular Credits (MCs)**
    #             """)
    #         with mid:
    #             st.empty()
    #         with sem2:
    #             st.write("**Academic Year 2022/23 Semester 2 (Expected)**")
    #             st.markdown("""
    #             |Code|Module Title                       |Workload|
    #             |--------|--------------------------------------|---------|
    #             |DSA426X|Sense-Making Case Analysis|4 MCs|
    #             |ST4234|Bayesian Statistics|4 MCs|
    #             |DSA4199|Applied Project in Data Science and Analytics|8 MCs|
    #             """)
    #             st.write("")
    #             st.markdown("""
    #             Total Workload for Semester: *16 Modular Credits (MCs)**
    #             """)
    #     with st.container():
    #         left, mid, right = st.columns((0.1,1,0.1))
    #         with left:
    #             st.empty()
    #         with mid:
    #             st.write("**Graduation Requirements**")
    #             st.image(img_NovaU)
    #         with right:
    #             st.empty()
elif choose == "Projects":
    st.header("Projects")
    st.subheader("Coming Soon")



elif choose == "Awards & Certifications":
    with st.container():
            left_column, middle_column, right_column = st.columns((1,0.2,0.5))
            with left_column:
                st.header("Awards and Certifications")
                st.write(":trophy: Villanova University Deans List: Fall 2020, Spring 2021, Spring 2022, Fall 2022, Spring 2023, Fall 2023, Spring 2024 ")
                st.write(":trophy: Syracuse University 2023 Basketball Analytics Competition Overall Winner ")
                st.write(":trophy: Syracuse University 2024 Basketball Analytics Competition Room Winner (Top 3) ")
                st.write(":trophy: Syracuse University 2024 Football Analytics Competition Room Winner (Top 4)")
                st.write(":trophy: Villanova Athletics Leadership Summit Certification")
            with middle_column:
                st.empty()
            # with right_column:
            #     st.image(img_me)