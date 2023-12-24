import pytest
import random


# 该注解会生成参数
@pytest.mark.parametrize('x', [(3), (7), (9)])
def test_add(x):
    print(x)
    assert x == random.randrange(1, 7)



