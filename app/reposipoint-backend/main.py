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
        config.personal_access_token,
        repo_name,
        description
    )
  
    response = repository.create()

    if response.status_code == 201:
        logger.info("Successfully created repository")
        return jsonify({'success': 'Successfully created repository'}), 201
    else:
        logger.error(f"Failed to create repository: {response.text}")
        return jsonify({'error': response.text}), response.status_code
    

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
