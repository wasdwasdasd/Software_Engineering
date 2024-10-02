#Tema5_SR2

def top_three_results(results):
    return sorted(results)[:3]


def worst_three_results(results):
    return sorted(results)[-3:]


def results_from_10(results):
    return results[9:]


if __name__ == '__main__':
    results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1,
               30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

    print("Три лучшие результата:", top_three_results(results))
    print("Три худшие результата:", worst_three_results(results))
    print("Результаты начиная с 10-го:", results_from_10(results))
