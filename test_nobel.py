from model import Laureat, Prize
from nobel import include_year, include_gender, include_category


def test_include_year_one_win():
    prize1 = Prize('1900', 'physics', 'aa')
    prize2 = Prize('1902', 'physics', 'aa')
    prize3 = Prize('1903', 'physics', 'aa')
    prize4 = Prize('1902', 'physics', 'aa')
    laureat1 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'male', [prize1, prize2])
    laureat2 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'male', [prize3, prize4])
    only_1900 = include_year([laureat1, laureat2], '1900')
    assert len(only_1900) == 1


def test_include_year_two_win():
    prize1 = Prize('1900', 'physics', 'aa')
    prize2 = Prize('1902', 'physics', 'aa')
    prize3 = Prize('1903', 'physics', 'aa')
    prize4 = Prize('1902', 'physics', 'aa')
    laureat1 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'male', [prize1, prize2])
    laureat2 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'male', [prize3, prize4])
    only_1902 = include_year([laureat1, laureat2], '1902')
    assert len(only_1902) == 2


def test_include_year_no_matches():
    prize1 = Prize('1900', 'physics', 'aa')
    prize2 = Prize('1902', 'physics', 'aa')
    prize3 = Prize('1903', 'physics', 'aa')
    prize4 = Prize('1902', 'physics', 'aa')
    laureat1 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'male', [prize1, prize2])
    laureat2 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'male', [prize3, prize4])
    only_1910 = include_year([laureat1, laureat2], '1910')
    assert len(only_1910) == 0


def test_gender_year_one_win():
    prize1 = Prize('1900', 'physics', 'aa')
    prize2 = Prize('1902', 'physics', 'aa')
    prize3 = Prize('1903', 'physics', 'aa')
    prize4 = Prize('1902', 'physics', 'aa')
    laureat1 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'male', [prize1, prize2])
    laureat2 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'female', [prize3, prize4])
    only_female = include_gender([laureat1, laureat2], 'female')
    assert len(only_female) == 1


def test_gender_year_two_win():
    prize1 = Prize('1900', 'physics', 'aa')
    prize2 = Prize('1902', 'physics', 'aa')
    prize3 = Prize('1903', 'physics', 'aa')
    prize4 = Prize('1902', 'physics', 'aa')
    laureat1 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'male', [prize1, prize2])
    laureat2 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'female', [prize3, prize4])
    only_male = include_gender([laureat1, laureat2], 'male')
    assert len(only_male) == 1


def test_gender_year_no_win():
    prize1 = Prize('1900', 'physics', 'aa')
    prize2 = Prize('1902', 'physics', 'aa')
    prize3 = Prize('1903', 'physics', 'aa')
    prize4 = Prize('1902', 'physics', 'aa')
    laureat1 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'male', [prize1, prize2])
    laureat2 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'male', [prize3, prize4])
    only_female = include_gender([laureat1, laureat2], 'female')
    assert len(only_female) == 0


def test_gender_category_one_win():
    prize1 = Prize('1900', 'physics', 'aa')
    prize2 = Prize('1902', 'physics', 'aa')
    prize3 = Prize('1903', 'ce', 'aa')
    prize4 = Prize('1902', 'aa', 'aa')
    laureat1 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'male', [prize1, prize2])
    laureat2 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'female', [prize3, prize4])
    only_physics = include_category([laureat1, laureat2], 'physics')
    assert len(only_physics) == 1


def test_gender_category_two_win():
    prize1 = Prize('1900', 'physics', 'aa')
    prize2 = Prize('1902', 'physics', 'aa')
    prize3 = Prize('1903', 'physics', 'aa')
    prize4 = Prize('1902', 'chemistry', 'aa')
    laureat1 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'male', [prize1, prize2])
    laureat2 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'female', [prize3, prize4])
    only_physics = include_category([laureat1, laureat2], 'physics')
    assert len(only_physics) == 2


def test_gender_category_gender_1_win():
    prize1 = Prize('1900', 'physics', 'aa')
    prize2 = Prize('1902', 'physics', 'aa')
    prize3 = Prize('1903', 'physics', 'aa')
    prize4 = Prize('1902', 'chemistry', 'aa')
    laureat1 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'male', [prize1, prize2])
    laureat2 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'female', [prize3, prize4])
    only_physics = include_category([laureat1, laureat2], 'physics')
    only_female = include_gender(only_physics, 'female')
    assert len(only_female) == 1


def test_gender_category_gender_2_win():
    prize1 = Prize('1900', 'physics', 'aa')
    prize2 = Prize('1902', 'physics', 'aa')
    prize3 = Prize('1903', 'physics', 'aa')
    prize4 = Prize('1902', 'chemistry', 'aa')
    laureat1 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'female', [prize1, prize2])
    laureat2 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'female', [prize3, prize4])
    only_physics = include_category([laureat1, laureat2], 'physics')
    only_female = include_gender(only_physics, 'female')
    assert len(only_female) == 2


def test_gender_category_gender_2_win():
    prize1 = Prize('1900', 'physics', 'aa')
    prize2 = Prize('1902', 'physics', 'aa')
    prize3 = Prize('1903', 'physics', 'aa')
    prize4 = Prize('1902', 'chemistry', 'aa')
    laureat1 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'female', [prize1, prize2])
    laureat2 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'female', [prize3, prize4])
    only_physics = include_category([laureat1, laureat2], 'physics')
    only_female = include_gender(only_physics, 'female')
    assert len(only_female) == 2


def test_gender_category_gender_year_1_win():
    prize1 = Prize('1900', 'physics', 'aa')
    prize2 = Prize('1902', 'physics', 'aa')
    prize3 = Prize('1903', 'physics', 'aa')
    prize4 = Prize('1902', 'chemistry', 'aa')
    laureat1 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'female', [prize1, prize2])
    laureat2 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'female', [prize3, prize4])
    only_physics = include_category([laureat1, laureat2], 'physics')
    only_female = include_gender(only_physics, 'female')
    only_1900 = include_year(only_female, '1900')
    assert len(only_1900) == 1


def test_gender_category_gender_year_2_win():
    prize1 = Prize('1900', 'physics', 'aa')
    prize2 = Prize('1902', 'physics', 'aa')
    prize3 = Prize('1900', 'physics', 'aa')
    prize4 = Prize('1902', 'chemistry', 'aa')
    laureat1 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'female', [prize1, prize2])
    laureat2 = Laureat('dawid', 'kak', '12', '12', 'polska', 'kielce', 'female', [prize3, prize4])
    only_physics = include_category([laureat1, laureat2], 'physics')
    only_female = include_gender(only_physics, 'female')
    only_1900 = include_year(only_female, '1900')
    assert len(only_1900) == 2