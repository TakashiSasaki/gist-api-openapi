import json

# Load the provided components.json file
with open('../original/components.json', 'r', encoding='utf-8') as file:
    components_data = json.load(file)

# Define the list of components to extract
components_to_extract = {
    "schemas": [
        "base-gist", "gist-comment", "gist-commit", "gist-simple"
    ],
    "responses": [
        "not_modified", "forbidden", "not_found", "forbidden_gist", 
        "validation_failed", "requires_authentication"
    ],
    "parameters": [
        "since", "per-page", "page", "gist-id", "comment-id"
    ],
    "headers": [
        "link"
    ],
    "examples": [
        "base-gist-items", "gist-comment", "gist-comment-items", 
        "gist-commit-items", "gist-fork-items", "base-gist", "gist", 
        "delete-gist-file", "rename-gist-file"
    ]
}

# Extract the specified components
extracted_components = {
    "schemas": {key: components_data["schemas"][key] for key in components_to_extract["schemas"] if key in components_data["schemas"]},
    "responses": {key: components_data["responses"][key] for key in components_to_extract["responses"] if key in components_data["responses"]},
    "parameters": {key: components_data["parameters"][key] for key in components_to_extract["parameters"] if key in components_data["parameters"]},
    "headers": {key: components_data["headers"][key] for key in components_to_extract["headers"] if key in components_data["headers"]},
    "examples": {key: components_data["examples"][key] for key in components_to_extract["examples"] if key in components_data["examples"]}
}

# Save the extracted components to a new JSON file
output_path = 'extracted_gist_components.json'
with open(output_path, 'w') as outfile:
    json.dump(extracted_components, outfile, indent=4)
