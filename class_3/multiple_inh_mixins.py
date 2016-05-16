
class MailView(PrivilegedView, USOnlyView):
    pass


LinkedList:
    * Sequence: for x in lst
    * Indexed:  lst[3]
    * Sortable: lst.sort()
    * Appendable: lst.append(5)
    * Lookable: '5' in lst == True
                 lst.look(5)  == True
    
    
Set:
    * Sequence: for x in st
    * Lookable: '5' in st == True
    * hashable
    

class Lookable(object):
    def look(self, obj):
        found = False
        for x in self:
            if obj == x:
                found = True
            if found:
                return True

        return False


class AlmostLinkedList(Sequence, Lookable):


class LinkedList(AlmostLinkedList):
    pass


class Set(Appendable, Lookable):
    pass


class modified_linked_list(Sequence, hashable):
    def look(self):
        raise Sometho()