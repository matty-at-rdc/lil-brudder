import pytest
from fastapi.testclient import TestClient

from lil_brudder.app.main import create_app

@pytest.fixture()
def app():
    app = create_app()
    return app

@pytest.fixture()
def tc(app):
    return TestClient(app)

@pytest.mark.asyncio
async def test_it(tc):
    resp = tc.get("/")
    print(resp)
    assert "apples" == "apples"


