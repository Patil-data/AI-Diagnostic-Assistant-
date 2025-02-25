import scispacy
import spacy
from scispacy.umls_linking import UmlsEntityLinker

# Load the SciSpaCy model
nlp = spacy.load("en_core_sci_md")

# Add the UMLS entity linker to the pipeline
linker = UmlsEntityLinker(resolve_abbreviations=True)
nlp.add_pipe(linker)

def extract_symptoms(text):
    doc = nlp(text)
    symptoms = []
    for ent in doc.ents:
        if "symptom" in ent._.umls_ents[0][1]:
            symptoms.append(ent.text)
    return symptoms