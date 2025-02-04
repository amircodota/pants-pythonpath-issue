import os


def test_get_message():
    print(f"PYTHONPATH = {os.environ.get('PYTHONPATH', 'No PYTHONPATH')}")
    
    from service1.logic import get_message
    assert get_message() == "Hello, World!"