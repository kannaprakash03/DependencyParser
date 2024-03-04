import spacy
import streamlit as st

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Define a function to parse sentences using SpaCy's dependency parser
def parse_with_spacy(sentence):
    doc = nlp(sentence)
    dependencies = [(token.text, token.dep_, token.head.text) for token in doc]
    return dependencies, doc

# Streamlit UI
st.set_page_config(
    page_title="Dependency Parser",
    page_icon="🔍",
    layout="wide"
)

# Header with title and description
st.title("Dependency Parser")
st.write("Enter a sentence in the text area below and click 'Parse' to visualize its dependency tree.")

# Input text area for user input
sentence_input = st.text_area("Enter a sentence for parsing:")

# Parse button
if st.button("Parse", key="parse_button"):
    # Parse the input text using SpaCy
    parsed_dependencies, doc = parse_with_spacy(sentence_input)

    # Display parsed dependencies
    st.write("Parsed Dependency Tree:")
    st.write(parsed_dependencies)

    # Visualize the dependency tree using SpaCy's displacy
    html = spacy.displacy.render(
        doc, style="dep", options={"distance": 120}, page=False
    )

    # Display the dependency tree
    st.write(html, unsafe_allow_html=True)
