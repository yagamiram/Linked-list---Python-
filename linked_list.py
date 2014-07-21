class node:
    def __init__(self):
        self._data = None
        self._next = None
    def set_data(self, data):
        self._data = data
    def set_next(self, next_ptr):
        self._next = next_ptr
    def go_next(self, ):
        pass
    def get_data(self):
        return self._data
    def get_next(self):
        return self._next
class Linkedlist:
    def __init__(self):
        self.head = None
    def insert(self, data):
        if self.head == None:
            new_node = node()
            new_node.set_data(data)
            new_node.set_next(None)
            self.head = new_node
        else:
            self.temp = self.head
            while(self.temp.get_next() != None):
                self.temp = self.temp.get_next()
            new_node = node()
            new_node.set_data(data)
            new_node.set_next(None)
            self.temp.set_next(new_node)
    def __str__(self):
        print("printing the linked list")
        self.temp = self.head
        if self.temp == None:
            print("None")
        else:
            while(self.temp != None):
                print(self.temp.get_data())
                self.temp = self.temp.get_next()
        return " "
    def push(self, data):
        if self.head == None:
            new_node = node()
            new_node.set_data(data)
            new_node.set_next(None)
            self.head = new_node
        else:
            self.temp = self.head
            new_node = node()
            new_node.set_data(data)
            new_node.set_next(self.temp)
            self.head = new_node
    def count(self):
        self.temp = self.head
        if self.temp == None:
            return None
        else:
            counter = 0
            while(self.temp != None):
                counter = counter + 1
                self.temp = self.temp.get_next()
            return counter
    def GetNth(self, pos):
        if self.head == None:
            return None
        else:
            counter = 0
            self.temp = self.head
            while(self.temp != None):
                counter = counter + 1
                if(counter == pos):
                    return self.temp.get_data()
                self.temp = self.temp.get_next()
    def deletelist(self):
        self.temp = self.head
        while(self.temp != None):
            node = self.temp
            self.temp = self.temp.get_next()
        self.head = self.temp
    def pop(self):
        self.temp = self.head
        if self.temp == None:
            return None
        else:
            data = self.temp.get_data()
    def sorted_insert(self, node):
        if self.head == None:
            self.head = node
        else:
            self.temp = self.head
            self.prev = None
            while(self.temp != None):
                if self.temp.get_data() > node.get_data():
                    break
                else:
                    self.prev = self.temp
                    self.temp = self.temp.get_next()
            if self.prev == None:
                node.set_next(self.temp)
                self.temp = node
                self.head = self.temp
            else:
                self.prev.set_next(node)
                node.set_next(self.temp)
    def insert_sort(self):
        self.temp = self.head
        result = Linkedlist()
        #print(result)
        while(self.temp != None):
            new_node = node()
            new_node.set_data(self.temp.get_data())
            new_node.set_next(None)
            result.sorted_insert(new_node)
            self.temp = self.temp.get_next()
        self.head = result.head
    def append(self, end_list):
        if self.head == None:
            self.head = end_list.head
            end_list.head = None
        else:
            self.temp = self.head
            while(self.temp.get_next() != None):
                self.temp = self.temp.get_next()
            self.temp.set_next(end_list.head)
            end_list.head = None
    def frontbacksplit(self, back):
        if self.head == None:
            back.head = None
        else:
            self.fast = self.head
            self.slow = self.head
            while(self.fast.get_next() != None):
                self.fast = self.fast.get_next()
                if(self.fast.get_next() != None):
                    self.slow = self.slow.get_next()
                    self.fast = self.fast.get_next()
            back.head = self.slow.get_next()        
            self.slow.set_next(None)
    def remove_duplicates(self):
        result = Linkedlist()
        current_value = None
        self.temp = self.head
        while(self.temp != None):
            if(current_value != self.temp.get_data()):
                result.insert(self.temp.get_data())
                current_value = self.temp.get_data()
            self.temp = self.temp.get_next()
        self.head = result.head       
    def move_node(self,	slist):
        if slist.head != None:
            node = slist.head
            slist.head = slist.head.get_next()
            node.set_next(self.head)
            if self.head == None:
                self.head = node
                self.head.set_next(None)
            else:
                self.head = node
    def alternating_split(self, alist, blist):
        while(self.head != None):
            alist.move_node(self)
            if(self.head != None):
                blist.move_node(self)
    def sorted_merge(self, alist, blist):
        len_a = alist.count()
        len_b = blist.count()
        #print len_a, len_b
        self.dummy = None
        while len_a > 0 or len_b > 0:
            #print "alist", alist
            #print "blist", blist
            #print "self", self
            if len_a == 0 or len_a == None:
                if self.head == None:
                    self.head = blist.head
                else:
                    self.dummy.set_next(blist.head)
                break
            elif len_b == 0 or len_b == None:
                if self.head == None:
                    self.head = alist.head
                else:
                    self.dummy.set_next(alist.head)
                break
            else:
                if self.head == None:
                    if alist.head.get_data() > blist.head.get_data():
                        self.head = blist.head
                        blist.head = blist.head.get_next()
                        self.dummy = self.head
                        len_b -= 1
                    elif alist.head.get_data() == blist.head.get_data():
                        self.head = blist.head
                        blist.head = blist.head.get_next()
                        self.dummy = alist.head
                        alist.head = alist.head.get_next()
                        self.dummy.set_next(None)	
                        self.head.set_next(self.dummy)
                        len_a -= 1
                        len_b -= 1
                    else:
                        self.head = alist.head
                        alist.head = alist.head.get_next()
                        self.dummy = self.head
                        len_a -= 1
                else:
                    if alist.head.get_data() > blist.head.get_data():
                        self.dummy.set_next(blist.head)
                        blist.head = blist.head.get_next()
                        self.dummy = self.dummy.get_next()
                        len_b -= 1
                    else:                    
                        self.dummy.set_next(alist.head)
                        alist.head = alist.head.get_next()
                        self.dummy = self.dummy.get_next()
                        len_a -= 1
    def shuffle_merge(self, alist, blist):
        len_a = alist.count()
        len_b = blist.count()
        self.dummy = None
        while len_a > 0 or len_b > 0:
            if len_a == 0:
                self.dummy.set_next(blist.head)
                break
            elif len_b == 0:
                self.dummy.set_next(alist.head)
                break
            else:
                if self.head == None:
                    self.push(alist.head.get_data())
                    alist.head = alist.head.get_next()
                    self.dummy = blist.head
                    blist.head = blist.head.get_next()
                    self.dummy.set_next(None)
                    self.head.set_next(self.dummy)
                    
                    
                else:
                    self.dummy.set_next(alist.head)
                    alist.head = alist.head.get_next()
                    self.dummy = self.dummy.get_next()
                    self.dummy.set_next(None)
                    
                    self.dummy.set_next(blist.head)
                    blist.head = blist.head.get_next()
                    self.dummy = self.dummy.get_next()
                    self.dummy.set_next(None)
                    
                len_a -=1 
                len_b -=1
    def merge_sort(self):
        if self.count() < 2:
            return self
        else:
            back = Linkedlist()
            self.frontbacksplit(back)
            result1 = self.merge_sort()
            result2 = back.merge_sort()
            result = Linkedlist()
            result.sorted_merge(result1, result2)
            self.head = result.head
            return result
    def sorted_intersect(self,alist, blist):
        self.dummy = None
        while alist.head != None and blist.head != None:
            if alist.head.get_data() == blist.head.get_data():
                if self.head == None:                        
                    self.head = alist.head
                    alist.head = alist.head.get_next()
                    blist.head = blist.head.get_next()
                    self.dummy= self.head
                    #self.head.set_next(self.dummy)
                else:
                    self.dummy.set_next(alist.head)
                    alist.head = alist.head.get_next()
                    blist.head = blist.head.get_next()
                    self.dummy = self.dummy.get_next()
            elif alist.head.get_data() > blist.head.get_data():
                blist.head = blist.head.get_next()
            else:
                alist.head = alist.head.get_next()
        self.dummy.set_next(None)
    def reverse(self):
        prev = None
        current = self.head
        fwd = self.head.get_next()        
        while(fwd != None):
            temp = current
            current.set_next(prev)           
            prev = current
            current = fwd
            fwd = fwd.get_next()
        current.set_next(prev)
        self.head = current
    def recursive_reverse(self):        
        if self.head.get_next() == None:
            return 
        else:
            head = self.head
            rest = Linkedlist()
            rest.head = self.head.get_next()
            rest.recursive_reverse()
            head.get_next().set_next(head)
            head.set_next(None)
            self.head = rest.head
            return
        
def main():
    ll = Linkedlist()
    ll2 = Linkedlist()
    ll.insert(1)
    ll.insert(3)
    ll.insert(2)
    ll2.insert(3)
    ll.insert(15)    
    ll2.insert(5)
    ll.insert(5)
    ll2.insert(10)
    ll.insert(11)
    ll.insert(44)
    ll2.insert(55)    
    ll.insert(11)
    ll.insert(12)
    ll2.insert(15)
    ll.insert(13)
    ll2.insert(14)    
    ll.insert(6)
    print "ll"
    print ll
    ll.recursive_reverse()
    print(ll)
if __name__ == "__main__" : main()
