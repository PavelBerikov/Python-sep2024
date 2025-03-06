# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
def notebook() -> list:
    todo_list: list[str] = []

    def add_todo(todo: str):
        todo_list.append(todo)

    def get_todos():
        print(todo_list)

    return [add_todo, get_todos]


add_todo, get_todos = notebook()
add_todo('Work')
add_todo('study')
get_todos()


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
def foo(num: int):
    digits = str(num)
    a = len(digits)
    parts = []
    for i, digit in enumerate(digits):
        if digit != '0':
            part = str(int(digit) * 10 ** (a - i - 1))
            parts.append(part)
    return "+".join(parts)


print(foo(1234))
# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором, та буде виводити це значення після виконання функцій
def dec(func):
    def inner():
        inner.call += 1
        func()
        print(f'Функція {func.__name__} викликана {inner.call}')
    inner.call = 0
    return inner

@dec
def greet():
    print('Hello World!')
@dec
def greet2():
    print('Hello World 2')
greet()
greet2()
greet()
greet2()


