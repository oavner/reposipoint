import logging
from flask import Flask, request, jsonify
from waitress import serve
from config import AppConfig
from repository import Repository

logger = logging.getLogger()
app = Flask(__name__)


@app.route("/create", methods=['POST'])
def index():
    """
    Index page for reposipoint. This endpoint is used to create a repository.
    """

    data = request.get_json()
    logger.info(f"Received request data: {data}")

    repo_name = data.get('repo_name')
    description = data.get('description')

    if not repo_name or not description:
        logger.error('Missing required parameters in request')
        return jsonify({'error': 'Missing required parameters'}), 400
    
    repository = Repository(
        config.api_url,
        config.owner,
        config.personal_access_token,
        repo_name,
        description
    )
  
    response = repository.create()
    if response.status_code == 201:
        logger.info("Successfully created repository")
    else:
        logger.error(f"Failed to create repository: {response.text}")
        return jsonify({'error:' 'Fail to create repository': response.text}), response.status_code
    
    response = repository.push_local_file('hello.txt', 'hello.txt')
    if response.status_code == 201:
        logger.info("Successfully added file to repository")
    else:
        logger.error(f"Failed to add file to repository: {response.text}")
        return jsonify({'error:' 'Failed to add file to repository': response.text}), response.status_code
    
    response = repository.add_branch_protection()
    if response.status_code == 200:
        logger.info("Successfully added branch protection")
    else:   
        logger.error(f"Failed to add branch protection: {response.text}")
        return jsonify({'error:' 'Failed to add branch protection': response.text}), response.status_code
    
    return jsonify({'success': 'Successfully created repository'}), 201


    

@app.route("/healthz")
def healthz():
    """
    Healthcheck endpoint for Kubernetes.
    """
    return "I AM ALIVE!"


if __name__ == "__main__":
    config = AppConfig()
    logger.setLevel(logging.DEBUG)
    serve(app, host="0.0.0.0", port=config.port)
