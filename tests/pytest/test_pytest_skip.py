import pytest


@pytest.mark.skip(reason="Фича в разработке")
def test_feature_in_development():
    ...

@pytest.mark.skip(reason="Фича в разработке")
class TestSuiteSkip:
    def test_feature_in_development1(self):
        ...

    def test_feature_in_development2(self):
        ...