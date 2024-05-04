from timeit import timeit
from kmp import kmp_search
from boyer_moore import boyer_moore_search
from rabin_karp import rabin_karp_search
import pandas as pd


def read_file(filename, encoding='utf-8'):
    with open(filename, 'r', encoding=encoding) as file:
        return file.read()


def get_search_results_ms(text, pattern):
    results = []
    boyer_moore_time = timeit(
        lambda: boyer_moore_search(text, pattern), number=1) * 1000
    kmp_time = timeit(lambda: kmp_search(text, pattern), number=1) * 1000
    rabin_karp_time = timeit(
        lambda: rabin_karp_search(text, pattern), number=1) * 1000
    return [boyer_moore_time, kmp_time, rabin_karp_time]


def print_search_results(name, text, existing_start, existing_end, nonexisting):

    df = pd.DataFrame({
        "Алгоритм": ["Боєра-Мура", "Кнута-Морріса-Пратта", "Рабіна-Карпа"],
        "На початку": get_search_results_ms(text, existing_start),
        "В кінці": get_search_results_ms(text, existing_end),
        "Не знайдено": get_search_results_ms(text, nonexisting)
    })

    print(f"Результати для {name}:")
    print(df.to_string(index=False))
    print()


if __name__ == "__main__":
    text1 = read_file('article1.txt')
    text2 = read_file('article2.txt')

    exist_t1_end = "Жадібні алгоритми."
    exist_t2_end = "Искусство программирования,"
    exist_t1_start = "Коваленко О.О."
    exist_t2_start = "Міхав В.В."
    nonexist_t1 = "Искусство программирования,"
    nonexist_t2 = "Жадібні алгоритми."

    print_search_results("Тексту 1", text1, exist_t1_start,
                         exist_t1_end, nonexist_t1)
    print_search_results("Тексту 2", text2, exist_t2_start,
                         exist_t2_end, nonexist_t2)
