"""numerology テストスイート

numerology.py が提供する 3 つの関数
`calculate_future_number`、`calculate_life_path`、`calculate_past_number`
の正確性を検証する PyTest テストケースを集約しています。

テスト項目の概要
----------------

* **Life Path（ライフパス）**
  - 生年月日 (year, month, day) から算出される番号が期待通りか確認。
  - 基本例、マスターナンバー（11, 22, 33）を含むケース、境界値 (0/0/0, 9999/12/31) を網羅。

* **Past Number（過去番号）**
  - 1〜31 の日付を単純にデジタルルート（マスターナンバーは例外）へ変換できるかテスト。

* **Future Number（未来番号）**
  - 月と日から算出される番号が正しいか検証。
  - 通常のデジタルルート、マスターナンバーの特別処理、例外規則（2 Feb 2 → 4、3 Mar 3 → 6）を含む。

* **エラーハンドリング**
  - ``calculate_life_path`` に不正な型（文字列）を渡した際に ``TypeError`` が送出されることを確認。

使用方法
--------
```bash
pytest numerology_test.py
```
"""

import pytest

from numerology import (
    calculate_future_number,
    calculate_life_path,
    calculate_past_number,
)


@pytest.mark.parametrize(
    "year, month, day, expected",
    [
        # 基本的な例
        (1990, 1, 1, 3),
        (2000, 12, 31, 9),
        (1985, 7, 23, 8),
        # マスターナンバーが出現するケース
        (1962, 9, 2, 11),
        (1964, 6, 21, 11),
        (1964, 9, 27, 11),
        (1970, 4, 10, 22),
        (1970, 11, 30, 22),
        (1971, 2, 2, 22),
        (1958, 10, 27, 33),
        (1970, 8, 26, 33),
        (1971, 8, 25, 33),
        # 境界値
        (0, 0, 0, 0),
        (9999, 12, 31, 7),
    ],
)
def test_calculate_life_path(year, month, day, expected):
    """calculate_life_path 関数が正しいライフパス番号を返すか確認する"""
    assert calculate_life_path(year, month, day) == expected


@pytest.mark.parametrize(
    "d, expected",
    [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 1),
        (11, 11),
        (12, 3),
        (13, 4),
        (14, 5),
        (15, 6),
        (16, 7),
        (17, 8),
        (18, 9),
        (19, 1),
        (20, 2),
        (21, 3),
        (22, 22),
        (23, 5),
        (24, 6),
        (25, 7),
        (26, 8),
        (27, 9),
        (28, 1),
        (29, 11),
        (30, 3),
        (31, 4),
    ],
)
def test_calculate_past_number(d, expected):
    """calculate_past_number 関数が過去の日付番号（1‑31）を正しく変換できるか確認する"""
    # 直接期待値を比較（可読性向上のため）
    assert calculate_past_number(d) == expected


@pytest.mark.parametrize(
    "m, d, expected",
    [
        (1, 1, 2),
        (1, 2, 3),
        (1, 3, 4),
        (1, 4, 5),
        (1, 5, 6),
        (1, 6, 7),
        (1, 7, 8),
        (1, 8, 9),
        (1, 9, 1),
        (1, 10, 2),
        (1, 11, 3),
        (1, 12, 4),
        (1, 13, 5),
        (1, 14, 6),
        (1, 15, 7),
        (1, 16, 8),
        (1, 17, 9),
        (1, 18, 1),
        (1, 19, 11),
        (1, 20, 3),
        (1, 21, 4),
        (1, 22, 5),
        (1, 23, 6),
        (1, 24, 7),
        (1, 25, 8),
        (1, 26, 9),
        (1, 27, 1),
        (1, 28, 11),
        (1, 29, 3),
        (1, 30, 4),
        (1, 31, 5),
        # マスターナンバー
        (2, 9, 11),
        (2, 18, 11),
        (2, 27, 11),
        (3, 8, 11),
        (3, 17, 11),
        (3, 26, 11),
        (4, 7, 11),
        (4, 16, 11),
        (4, 25, 11),
        (5, 6, 11),
        (5, 15, 11),
        (5, 24, 11),
        (6, 5, 11),
        (6, 14, 11),
        (6, 23, 11),
        (7, 4, 11),
        (7, 13, 11),
        (7, 22, 11),
        (7, 31, 11),
        (8, 3, 11),
        (8, 12, 11),
        (8, 21, 11),
        (8, 30, 11),
        (9, 2, 11),
        (9, 11, 11),
        (9, 20, 11),
        (10, 19, 11),
        (10, 28, 11),
        (11, 9, 11),
        (11, 18, 11),
        (11, 27, 11),
        (12, 8, 11),
        (12, 17, 11),
        (12, 26, 11),
        # 2月2日, 3月3日は22と33ではなく、2+2=4, 3+3=6
        (2, 2, 4),
        (3, 3, 6),
    ],
)
def test_calculate_future_number(m, d, expected):
    """calculate_future_number 関数が月日から正しい未来数を算出できるか確認する"""
    assert calculate_future_number(m, d) == expected


def test_invalid_input_type():
    """不正な型の入力に対して calculate_life_path 関数が ValueError を送出するか確認する

    Raises:
        ValueError: int以外の型が入力されたときに期待される例外
    """
    with pytest.raises(ValueError):
        calculate_life_path("abc", 2, 3)
