def reorderLogFiles(logs):
        
        def get_key(log):
            iD, contents = log.split(' ', maxsplit=1)
            return (0, contents, iD) if contents[0].isalpha() else (1, )

        return sorted(logs, key=get_key)


if __name__ == '__main__':
      assert reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]) == ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
      assert reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]) == ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]