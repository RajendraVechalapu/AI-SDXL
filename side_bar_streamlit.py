with st.sidebar:
     # Selectbox
     st.image('fig/hf.png')
     add_selectbox = st.sidebar.selectbox(
     "Prompt examples",
       (
          "None",
           "Van Gogh painting with squirrels eating nuts", 
           "Homer Simpson on a computer wearing a space suit",
           "Mona Lisa with headphones on",
           "A digital artwork of a roborovski hamster dressed in blue wizards clothing casting a thunderstorm with lightning",
           "A model wearing a scuba diving suit",
           "A looney tunes character driving a car",
           "Optimus Prime on top of a surf board",
           "Albert Einstein with a goofy smile",
           "Nottingham Forest football team lifting the FA Cup"
        ), index=0)
     st.markdown('Use the above drop down box to generate _prompt_ examples')
     st.text('Application by Rajendar Vechalapu')