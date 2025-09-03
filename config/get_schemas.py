import yaml
import sys
import os
import json

def get_schemas():
    schemas_yml = os.path.join(os.path.dirname(__file__), "schemas.yml")
    # ✅ send debug to stderr, not stdout
    print(f"Current directory: {os.getcwd()}", file=sys.stderr)
    print(f"Looking for: {schemas_yml}", file=sys.stderr)

    try:
        with open(schemas_yml, 'r') as file:
            data = yaml.safe_load(file)
            if data and 'schemas' in data and data['schemas']:
                return data['schemas']
            else:
                print("Error: No valid schemas found in schemas.yml", file=sys.stderr)
                sys.exit(1)
    except FileNotFoundError:
        print("Error: schemas.yml not found", file=sys.stderr)
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error: Invalid YAML in schemas.yml - {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    schemas = get_schemas()
    # ✅ only JSON goes to stdout
    print(json.dumps(schemas))
