import robo_speaker


def test_speak_returns_bool():
    result = robo_speaker.speak('pytest run')
    assert isinstance(result, bool)
