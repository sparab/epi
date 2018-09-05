from test_framework import generic_test


def levenshtein_distance_recur(A, B):
    if not A:
        return len(B)
    elif not B:
        return len(A)

    return min(min(levenshtein_distance(A[:-1], B), levenshtein_distance(A, B[:-1])) + 1,
               levenshtein_distance(A[:-1], B[:-1])
               if A[-1] == B[-1] else
               levenshtein_distance(A[:-1], B[:-1]) + 1)


def levenshtein_distance(word1, word2):
    distance = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
    for i in range(len(word1) + 1):
        distance[i][0] = i

    for j in range(len(word2) + 1):
        distance[0][j] = j

    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            distance[i][j] = min(min(distance[i][j - 1], distance[i - 1][j]) + 1,
                                 distance[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else distance[i - 1][j - 1] + 1)

    return distance[-1][-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))
