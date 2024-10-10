# GitHub Gist API OpenAPI Documents

This section provides two OpenAPI document files related to Gist endpoints in the GitHub REST API.

## File List

- **github\_gist\_api.yaml**: This document covers all endpoints related to the GitHub Gist API. It includes the following endpoints:

  - `/gists` (list and create)
  - `/gists/public` (list public gists)
  - `/gists/starred` (list starred gists)
  - `/gists/{gist_id}` (get, update, delete a specific gist)
  - `/gists/{gist_id}/comments` (list, create, update, delete comments)
  - `/gists/{gist_id}/forks` (list and create forks)
  - `/gists/{gist_id}/star` (star operations)

- **github\_gist\_api\_subset.yaml**: This document covers a subset of endpoints related to basic operations of the GitHub Gist API. It includes the following endpoint:

  - `/gists` (list and create)

These files are provided to facilitate understanding and use of GitHub Gist API endpoints.

## Download Links

You can download the corresponding OpenAPI documents from the links below, or view the Gist containing both documents here: [GitHub Gist](https://gist.github.com/TakashiSasaki/494513122fc5627f6e1a78732b64d4a6):

1. [github\_gist\_api.yaml](https://gist.githubusercontent.com/TakashiSasaki/494513122fc5627f6e1a78732b64d4a6/raw/045ab1efa87a2e6ba91ed202fd46d8ddc44483c2/github_gist_api.yaml)
2. [github\_gist\_api\_subset.yaml](https://gist.githubusercontent.com/TakashiSasaki/494513122fc5627f6e1a78732b64d4a6/raw/045ab1efa87a2e6ba91ed202fd46d8ddc44483c2/github_gist_api_subset.yaml)

## Validation

These two OpenAPI documents have been validated using the tool available at [Swagger Parser Online](https://apitools.dev/swagger-parser/online/). Additionally, they have been configured to resolve all reference relationships correctly, ensuring that they are properly parsed when entered in the ChatGPT custom actions settings page.

## Usage

The `github_gist_api_subset.yaml` document is also used in the ChatGPT custom GPT named ["Gist Writer"](https://chatgpt.com/g/g-EJnDg5v36-gist-writer), which allows for streamlined interaction with Gist endpoints.

You can import these files into Swagger Editor or Postman to view the API details and generate API clients.

Contact

The author of this Gist is Takashi Sasaki. You can contact him via X (formerly Twitter) for any inquiries or further information.
