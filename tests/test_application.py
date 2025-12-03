import pytest
import time
from application import application


@pytest.fixture
def client():
    application.config['TESTING'] = True
    with application.test_client() as client:
        yield client


def test_hello_route(client):
    """
    Test the hello route returns the expected message with appropriate status and content.

    This test ensures that the root endpoint '/' responds quickly (within 1 second)
    to prevent potential hangs or slow responses, and includes comprehensive checks
    for status code, content type, and message content to verify the application's
    deployment message from AWS Elastic Beanstalk via GitHub Actions.
    """
    start_time = time.time()
    response = client.get('/')
    elapsed_time = time.time() - start_time

    # Assert response time is reasonable (less than 1 second to prevent long waits)
    assert elapsed_time < 1.0, f"Response took too long: {elapsed_time:.2f} seconds"

    # Standard assertions
    assert response.status_code == 200
    assert response.content_type == 'text/html; charset=utf-8'
    assert b"Hello from AWS Elastic Beanstalk via GitHub Actions! \xf0\x9f\x9a\x80" in response.data

    # Additional check: ensure response data is a string and contains key phrases
    data_str = response.data.decode('utf-8')
    assert "Hello from AWS Elastic Beanstalk" in data_str
    assert "via GitHub Actions" in data_str
