"""数秘術の計算モジュール

数秘術（Numerology）における「運命数（ライフパスナンバー）」や
「過去数」「未来数」を計算するユーティリティ関数群。

数秘術では、数値の各桁を足し合わせて一桁（1‑9）にするか、
マスターナンバー（11, 22, 33）の場合はそのまま残します。
本モジュールはその標準的な還元アルゴリズムを実装しています。

本モジュールは純粋な Python で記述されており、外部依存はありません。
そのため、他のプロジェクトに組み込んだり、
インタラクティブに手軽に利用したりするのに適しています。

"""


def calculate_life_path(y: int, m: int, d: int) -> int:
    """誕生日から運命数（ライフパスナンバー）を計算する。

    Args:
        y(int): 例 1990
        m(int): 1‑12 の整数
        d(int): 1‑31 の整数

    Returns:
        int: 運命数（1‑9 または 11, 22, 33 のいずれか）
    """
    total = __reduce_to_one_digit(int(str(y) + str(m) + str(d)))
    return total


def calculate_past_number(d: int) -> int:
    """「過去数」＝ d の和を 1 桁（またはマスターナンバー）に縮小した結果。

    Args:
        d(int): 任意の整数（例: 日、別の数値など）

    Returns:
        int: 過去数（1‑9 または 11, 22, 33 のいずれか）
    """
    return __reduce_to_one_digit(d)


def calculate_future_number(m: int, d: int) -> int:
    """「未来数」＝ m と d の和を 1 桁（またはマスターナンバー）に縮小した結果。

    Args:
        m(int): 任意の整数（例: 月、年の縮小結果など）
        d(int): 任意の整数（例: 日、別の数値など）

    Returns:
        int: 未来数（1‑9 または 11, 22, 33 のいずれか）
    """
    if m == d and d in (1, 2, 3):
        return m + d

    return __reduce_to_one_digit(int(str(m) + str(d)))


def __digit_sum(n: int) -> int:
    """整数 n の各桁の合計を返す

    Args:
        n(int): 合計する数値

    Returns:
        int: 合計した数値
    """
    return sum(int(d) for d in str(n))


def __reduce_to_one_digit(n: int) -> int:
    """数値算出

    1 桁になるまで数字を足し続ける。
    11, 22, 33 はマスターナンバーとしてそのまま残す（必要に応じて変更可）。

    Args:
        n(int): 計算する数値

    Returns:
        int: 計算した数値（1‑9 または 11, 22, 33 のいずれか）
    """
    while n > 9 and n not in (11, 22, 33):
        n = __digit_sum(n)
    return n
