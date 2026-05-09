import argparse
import json
from src.core import ModelProvenance

def main():
    parser = argparse.ArgumentParser(description='Model Provenance Toolkit')
    parser.add_argument('--model_name', type=str, help='Model name')
    parser.add_argument('--model_version', type=str, help='Model version')
    args = parser.parse_args()
    provenance = ModelProvenance(args.model_name, args.model_version)
    print(provenance.get_provenance())
if __name__ == '__main__':
    main()
