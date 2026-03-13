"""Basic placeholder tests."""

from happystudy.pingpong import ping


def test_pingpong() -> None:
    """Test the pingpong placeholder function."""

    result = ping()
    assert result == "pong"
