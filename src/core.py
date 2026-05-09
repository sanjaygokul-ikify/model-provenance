import json
from typing import Dict

class ModelProvenance:
    def __init__(self, model_name: str, model_version: str):
        self.model_name = model_name
        self.model_version = model_version
        self.provenance = self.load_provenance()
    def load_provenance(self) -> Dict:
        # Load provenance metadata from file or database
        return json.load(open('provenance.json'))
    def get_provenance(self) -> Dict:
        return self.provenance
