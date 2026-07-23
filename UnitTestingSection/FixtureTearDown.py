import pytest


@pytest.fixture(autouse=True)
def cal():
    print("\nOpening a file")

    yield

    print("\nClosing the file")


def test_tarak():
    assert 1==1