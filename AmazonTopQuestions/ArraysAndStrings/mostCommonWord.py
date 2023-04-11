from collections import Counter


def mostCommonWord(paragraph, banned):
    removePunc = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
    splitStr = removePunc.split()
    wordCount = Counter(splitStr)
    for word in banned:
        wordCount.pop(word, None)
    return wordCount.most_common()[0][0]


if __name__ == '__main__':
    assert mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.', ['hit']) == 'ball'
    