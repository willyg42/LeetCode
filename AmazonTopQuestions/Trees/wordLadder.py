from collections import defaultdict, deque

def ladderLength(beginWord, endWord, wordList):
    linkMap = defaultdict(set)
    for w in wordList:
        for i in range(len(w)):
            linkMap[w[:i] + '*' + w[i+1:]].add(w)
    
    queue = deque([(beginWord, 1)])
    visited = {}
    while queue:
        nextWord, level = queue.popleft()
        for i in range(len(nextWord)):
            link = nextWord[:i] + '*' + nextWord[i + 1:]
            for child in linkMap[link]:
                if child == endWord:
                    return level + 1
                if child not in visited:
                    visited[child] = True
                    queue.append((child, level + 1))
            linkMap[link] = []        
    return 0