class BtreeNode:
    
    def __init__(self, string):
        self._string = string
        self._lt, self._gt = None, None

    def _insert(self, string):
        if string == self._string:
            return
        if string < self._string:
            if self._lt is None:
                self._lt = BtreeNode(string)
            else:
                self._lt._insert(string)
        elif string > self._string:
            if self._gt is None:
                self._gt = BtreeNode(string)
            else:
                self._gt._insert(string)
    
    def _search(self, string):
        if string == self._string:
            return True
        elif string < self._string:
            return self._lt is not None and self._lt._search(string)
        else:
            return self._gt is not None and self._gt._search(string)
    
    def _all_strings(self):
        strings = [self._string]
        if self._lt is not None:
            strings.extend(self._lt._all_strings())
        if self._gt is not None:
            strings.extend(self._gt._all_strings())
        return strings

    def __len__(self):
        length = 1
        if self._lt is not None:
            length += len(self._lt)
        if self._gt is not None:
            length += len(self._gt)
        return length

    def _to_string(self, indent=''):
        repr_str = indent + repr(self)
        if self._lt is not None:
            repr_str += '\n' + self._lt._to_string(indent + '  ')
        if self._gt is not None:
            repr_str += '\n' + self._gt._to_string(indent + '  ')
        return repr_str

    def __repr__(self):
        return self._string


class Btree:
    
    def __init__(self):
        self._root = None
        
    def insert(self, string):
        if self._root is None:
            self._root = BtreeNode(string)
        else:
            self._root._insert(string)

    def search(self, string):
        if self._root is None:
            return False
        else:
            return self._root._search(string)
        
    def all_strings(self):
        if self._root is None:
            return []
        else:
            return self._root._all_strings()
        
    def __len__(self):
        if self._root is None:
            return 0
        else:
            return len(self._root)
    
    def __repr__(self):
        if self._root is None:
            return 'empty tree'
        else:
            return self._root._to_string('')
