from goatools import obo_parser
from dotenv import load_dotenv, find_dotenv
import os
import pandas as pd

load_dotenv(find_dotenv())

def load_go_df():
    go_obo = obo_parser.GODag(os.getenv('GO_OBO_FILE'), optional_attrs=['def'])

    # Convert to a DataFrame
    go_terms = []
    for go_id, go_term in go_obo.items():
        term_data = {
            'go_id': go_id,
            'name': go_term.name,
            'namespace': go_term.namespace,
            'definition': go_term.defn,
            'is_obsolete': go_term.is_obsolete,
            'parents': [parent.id for parent in go_term.parents],
            'children': [child.id for child in go_term.children],
        }
        go_terms.append(term_data)

    go_df = pd.DataFrame(go_terms)
    
    return go_df