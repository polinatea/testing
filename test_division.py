
import lab
import pytest

# покрываем декоратором, чтобы прогнать несколько похожих тестов в одном
@pytest.mark.parametrize("a, b, expected_result", [(10,2,5),
                                                   (20,10,2) ,
                                                   (30,-3,-10),
                                                   (5, 2, 2.5)])
def test_division_good(a,b,expected_result):
    assert lab.division(a,b)==expected_result


def test_zero_division():
    # мы ожидаем возникновения ошибки деления на ноль
    # тест воспринимается как успешно прошедший
    with pytest.raises(ZeroDivisionError):
        # когда pytest перехватывает ошибку, он проверяет
        # параметр raises
        lab.division(10, 0)

def test_type_error():
    # отлавливаем другое исключение
    with pytest.raises(TypeError):
        lab.division(10, "2")

# тот же самый тест с ожиданием ошибки только универсальный
@pytest.mark.parametrize("expected_exception, divisionable, divider", [(ZeroDivisionError, 10, 0),
                                                                       (TypeError, 20, "2")])
def test_division_with_error(expected_exception, divider, divisionable):
    with pytest.raises(expected_exception):
        lab.division(divisionable, divider)


def test_increment():
    assert lab.increment(3) == 4

def test_decrement():
    assert lab.decrement(3) == 2



# Фикстуры — это функции, которые будут выполняться перед каждой тестовой функцией, 
# к которой они применяются. Фикстуры используются для подачи некоторых данных в тесты, 
# таких как соединения с базой данных, URL-адреса для тестирования и некоторые виды входных данных. 
# Поэтому вместо того, чтобы запускать один и тот же код для каждого теста, мы можем прикрепить к тестам 
# функцию фиксации, и она будет запускаться и возвращать данные в тест перед выполнением каждого теста.
@pytest.fixture
def input_value():
    # Тестовая функция может использовать фикстуру, указав имя фикстуры в качестве входного параметра.
   input = 39
   return input


# Здесь у нас есть функция фиксации с именем input_value, 
# которая предоставляет входные данные для тестов. Чтобы получить 
# доступ к функции фикстуры, тесты должны указать имя фикстуры 
# в качестве входного параметра.

# Pytest во время выполнения теста увидит имя прибора в качестве входного параметра. 
# Затем он выполняет функцию фиксации, и возвращаемое значение сохраняется во входном 
# параметре, который может использоваться тестом.


def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0
