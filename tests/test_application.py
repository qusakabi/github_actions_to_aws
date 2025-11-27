import pytest
from application import application


@pytest.fixture
def client():
    application.config['TESTING'] = True
    with application.test_client() as client:
        yield client


def test_hello_route(client):
    """Test the hello route returns the expected message."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello from AWS Elastic Beanstalk via GitHub Actions! \xf0\x9f\x9a\x80" in response.data
