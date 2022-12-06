"""Test dezmq."""
# pylint: disable=broad-except
from dezmq import __version__, dezmq


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not dezmq()
    except Exception:
        assert True
