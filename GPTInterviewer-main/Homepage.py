import streamlit as st
from streamlit_option_menu import option_menu
from app_utils import switch_page
import streamlit as st
from PIL import Image

im = Image.open("icon.png")
st.set_page_config(page_title = "AI Interviewer", layout = "centered",page_icon=im)

lan = st.selectbox("#### Language", ["English", "Français"])

if lan == "English":
    home_title = "RHIA - AI Interviewer"
    home_introduction = "Welcome to AI Interviewer, empowering your interview preparation with generative AI."
    with st.sidebar:
        st.markdown('RHIA - AI Interviewer')
        st.markdown(""" 
        #### Let's contact:
        [Léo Carré](https://www.linkedin.com/in/leocarre/)
        
        [Paul Giraudet](https://www.linkedin.com/in/paul-giraudet-5750921a9/)
                    
        [Léandra Mas](https://www.linkedin.com/in/l%C3%A9andra-mas-99a0601b2//)
        
        #### Powered by
    
        [OpenAI](https://openai.com/)
    
        [FAISS](https://github.com/facebookresearch/faiss)
    
        [Langchain](https://github.com/hwchase17/langchain)
    
                    """)
    st.markdown(
        "<style>#MainMenu{visibility:hidden;}</style>",
        unsafe_allow_html=True
    )
    st.image(im, width=100)
    st.markdown(f"""# {home_title} <span style=color:#2E9BF5><font size=5>Beta</font></span>""",unsafe_allow_html=True)
    st.markdown("""\n""")
    #st.markdown("#### Greetings")
    st.markdown("Welcome to RHIA, your AI Interviewer! 👏 RHIA is your personal interviewer powered by generative AI that conducts mock interviews. "
                "You can upload your resume and enter job descriptions, and AI Interviewer will ask you customized questions)")
    st.markdown("""\n""")
   
    st.markdown("#### Get started!")
    st.markdown("Select one of the following screens to start your interview!")
    selected = option_menu(
            menu_title= None,
            options=["Professional", "Resume", "Behavioral","Customize!"],
            icons = ["cast", "cloud-upload", "cast"],
            default_index=0,
            orientation="horizontal",
        )
    if selected == 'Professional':
        st.info("""
            📚In this session, the AI Interviewer will assess your technical skills as they relate to the job description.
            Note: The maximum length of your answer is 4097 tokens!
            - Each Interview will take 10 to 15 mins.
            - To start a new session, just refresh the page.
            - Choose your favorite interaction style (chat/voice)
            - Start introduce yourself and enjoy！ """)
        if st.button("Commencez l'entretien !"):
            switch_page("Professional Screen")
    if selected == 'Resume':
        st.info("""
        📚In this session, the AI Interviewer will review your resume and discuss your past experiences.
        Note: The maximum length of your answer is 4097 tokens!
        - Each Interview will take 10 to 15 mins.
        - To start a new session, just refresh the page.
        - Choose your favorite interaction style (chat/voice)
        - Start introduce yourself and enjoy！ """
        )
        if st.button("Commencez l'entretien !"):
            switch_page("Resume Screen")
    if selected == 'Behavioral':
        st.info("""
        📚In this session, the AI Interviewer will assess your soft skills as they relate to the job description.
        Note: The maximum length of your answer is 4097 tokens!
        - Each Interview will take 10 to 15 mins.
        - To start a new session, just refresh the page.
        - Choose your favorite interaction style (chat/voice)
        - Start introduce yourself and enjoy！ 
        """)
        if st.button("Start Interview!"):
            switch_page("Behavioral Screen")
    if selected == 'Customize!':
        st.info("""
            📚In this session, you can customize your own AI Interviewer and practice with it!
             - Configure AI Interviewer in different specialties.
             - Configure AI Interviewer in different personalities.
             - Different tones of voice.
             
             Coming later...""")
    st.markdown("""\n""")


if lan ==  'Français':
    home_title = "RHIA - AI Interviewer"
    home_introduction = "Bienvenue chez RHIA, l'interviewer IA intelligent, qui renforce votre préparation aux entretiens grâce à l'intelligence artificielle générative."
    with st.sidebar:
        st.markdown('RHIA - interviewer IA intelligent')
        st.markdown(""" 
        #### Contactez-nous:
        [Léo Carré](https://www.linkedin.com/in/leocarre/)
        
        [Paul Giraudet](https://www.linkedin.com/in/paul-giraudet-5750921a9/)
                    
        [Léandra Mas](https://www.linkedin.com/in/l%C3%A9andra-mas-99a0601b2//)
        
        #### Développé grâce à
    
        [OpenAI](https://openai.com/)
    
        [FAISS](https://github.com/facebookresearch/faiss)
    
        [Langchain](https://github.com/hwchase17/langchain)
    
                    """)
    st.markdown(
        "<style>#MainMenu{visibility:hidden;}</style>",
        unsafe_allow_html=True
    )
    st.image(im, width=100)
    st.markdown(f"""# {home_title} <span style=color:#2E9BF5><font size=5>Beta</font></span>""",unsafe_allow_html=True)
    st.markdown("""\n""")
    #st.markdown("#### Greetings")
    st.markdown("Bienvenue chez RHIA, votre Intervieweur IA ! &rsquo;👏 RHIA est votre interviewer personnel alimenté par l'intelligence artificielle générative qui mène des entretiens simulés.Vous pouvez télécharger votre CV et saisir des descriptions de poste, et l'Intervieweur IA vous posera des questions personnalisées.")
    st.markdown("""\n""")
   
    st.markdown("#### Commencez ici!")
    st.markdown("Sélectionnez l'un des écrans suivants pour commencer votre entretien !")
    selected = option_menu(
            menu_title= None,
            options=["Professional", "Resume", "Behavioral","Customize!"],
            icons = ["cast", "cloud-upload", "cast"],
            default_index=0,
            orientation="horizontal",
        )
    if selected == 'Professional':
        st.info("""
            📚Dans cette session, l'intervieweur évaluera vos compétences techniques par rapport à la description du poste.
            Remarque : la longueur maximale de votre réponse est de 4097 jetons !
            - Chaque entretien dure entre 10 et 15 minutes.
            - Pour commencer une nouvelle session, il suffit de rafraîchir la page.
            - Choisissez votre style d'interaction préféré (chat/voix)
            - Commencez à vous présenter et appréciez！ """)
        if st.button("Start Interview!"):
            switch_page("Professional Screen")
    if selected == 'Resume':
        st.info(
        """
        📚Dans cette session, l'intervieweur AI examinera votre CV et discutera de vos expériences passées.
        Remarque : la longueur maximale de votre réponse est de 4097 jetons !
        - Chaque entretien dure entre 10 et 15 minutes.
        - Pour commencer une nouvelle session, il suffit de rafraîchir la page.
        - Choisissez votre style d'interaction préféré (chat/voix)
        - Commencez à vous présenter et appréciez！ """
        )
        if st.button("Commencez l'entretien !"):
            switch_page("Resume Screen")
    if selected == 'Behavioral':
        st.info("""
        📚Dans cette session, l'intervieweur AI évaluera vos compétences non techniques par rapport à la description du poste.
        Remarque : la longueur maximale de votre réponse est de 4097 jetons !
        - Chaque entretien dure entre 10 et 15 minutes.
        - Pour commencer une nouvelle session, il suffit de rafraîchir la page.
        - Choisissez votre style d'interaction préféré (chat/voix)
        - Commencez à vous présenter et appréciez！
        """)
        if st.button("Commencez l'entretien !"):
            switch_page("Behavioral Screen")
    if selected == 'Customize!':
        st.info("""
            📚Dans cette session, vous pouvez personnaliser votre propre AI Interviewer et vous entraîner avec !
             - Configurez AI Interviewer dans différentes spécialités.
             - Configurez l'intervieweur AI en différentes personnalités.
             - Différents tons de voix.
             
             À venir plus tard...""")
    st.markdown("""\n""")