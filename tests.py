import rules


def test_update_state():
    state1 = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 1, 1, 1, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]
    state2 = [[0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0],
              [0, 0, 1, 0, 0],
              [0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0]]
    assert rules.update_state(state1) == state2


if __name__ == '__main__':
    test_update_state()
