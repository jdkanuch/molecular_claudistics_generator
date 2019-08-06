import random
import time
import functools
import itertools

def time_probe(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'Time to complete {func.__name__}: {t2}')
        return result
    return wrapper


def generate_sequence(seq_length, sequences):
    choices = ['a', 't', 'g', 'c']
    return ["".join((random.choice(choices) for i in range(seq_length))) for i in range(sequences)]


@time_probe
def count_diff(sequences):
    diff_matrix = [[0 for col in range(len(sequences))] for row in range(len(sequences))]
    combo_mapper = itertools.combinations(range(len(sequences)), 2)
    combinations = itertools.combinations(sequences, 2)

    def compare_seq(a, b):
        for achar, bchar in zip(a, b):
            if achar != bchar:
                yield 1

    for combination, combo_mapping in zip(combinations, combo_mapper):
        count = 0
        compare_gen = compare_seq(combination[0], combination[1])
        for comparison in compare_gen:
            count += comparison

        diff_matrix[combo_mapping[0]][combo_mapping[1]] = diff_matrix[combo_mapping[1]][combo_mapping[0]] = count

    return diff_matrix


def main():
    seq_length = 40
    sequence_amount = 1000

    sequences = generate_sequence(seq_length, sequence_amount)
    print(sequences)

    diff_matrix = count_diff(sequences)
    #print(f"Diff Matrix : {diff_matrix}")


if __name__ == "__main__":
    main()
