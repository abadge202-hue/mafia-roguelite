from main import describe_best


def test_describe_best_handles_old_save_without_bosses():
    old_best = {"Won": False, "Floors": 2, "Enemies Defeated": 5, "Items Found": 1}
    result = describe_best(old_best)
    assert "0 bosses defeated" in result
