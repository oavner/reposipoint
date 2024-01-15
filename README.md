# Reposipoint

Reposipoint is a streamlined tool designed to simplify the process of setting a new GitHub repository with standard add-ons into a single `curl` request. The project includes a bootstrap script tailored for macOS users, leveraging Docker, GitHub Personal Access Tokens (PAT), and a k3d cluster for a seamless experience.
Reposipoint automates the repository creation process, allowing you to focus on your code without worrying about tedious setup tasks. 

## Prerequisites

Before using Reposipoint, ensure that you have the following prerequisites:

1. **Docker:** Install Docker on your mac to run k3d and setup the reposipoint backend.

2. **GitHub Account:** Create a GitHub account if you don't have one already. This account will be the owner of the repositories generated by reposipoint (use this account to also generate a Personal Access Token). 

3. **GitHub Personal Access Token (PAT):** Generate a PAT with 'repo' and 'workflow' permissions from your GitHub account. This token is necessary for repository creation and adding standard github workflows.

## Bootstrap the Project

To set up Reposipoint over your macOS, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/oavner/reposipoint.git
2. **Add Execution Permissions to the Bootstrap Script:**
   ```bash
   chmod u+x reposipoint/bootstrap/mac.sh
3. **Run the Bootstrap Script** 
   ```bash
   ./reposipoint/bootstrap/mac.sh <github personal access token> <github owner>

This script sets up a local k3d cluster, deploys the Reposipoint application chart, and exposes the app via localhost:8081.



## Using Reposipoint with cURL

Execute the following cURL command, replacing the placeholder values with your desired repository name and description:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"repo_name": <your repo name>, "description": <short description>}' http://localhost:8081/create
```
This command sends a request to Reposipoint, creating a new GitHub repository with default protection rules, CI and README.md files. See the following example repo: https://github.com/oavner/example

**That's it!  Enjoy Seamless Repository Setup  :)**  

