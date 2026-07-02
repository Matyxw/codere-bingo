import os
import sys
import types
from pathlib import Path

from fastapi.testclient import TestClient

project_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(project_root))

os.environ.setdefault("DATABASE_URL", "sqlite://")
os.environ.setdefault("SECRET_KEY", "test-secret")
os.environ.setdefault("CORS_ORIGINS", "*")

backend_pkg = types.ModuleType("backend")
backend_pkg.__path__ = [str(project_root / "backend")]
sys.modules["backend"] = backend_pkg

core_pkg = types.ModuleType("backend.core")
core_pkg.__path__ = [str(project_root / "backend" / "core")]
sys.modules["backend.core"] = core_pkg

from backend.main import app  # noqa: E402

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
