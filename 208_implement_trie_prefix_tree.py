# -*- coding: utf-8 -*-

class Trie(object):

    def __init__(self, val=None, is_end=False):
        """
        Initialize your data structure here.
        """
        self.val = val
        self.children = {}
        self.is_end = is_end

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if word[0] not in self.children:
            self.children[word[0]] = Trie(word[0])

        if len(word) == 1:
            self.children[word[0]].is_end = True
        else:
            self.children[word[0]].insert(word[1:])


    def _find(self, word, exact):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if word[0] in self.children:
            if len(word) > 1:
                return self.children[word[0]]._find(word[1:], exact)
            else:
                return self.children[word[0]].is_end if exact else True
        return False


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return self._find(word, True)


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self._find(prefix, False)

obj = Trie()
obj.insert('apple')
obj.search('apple')
obj.search('app')
print(obj.startsWith('app'))
