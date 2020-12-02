class Node:
    def __init__(self, l, r, val=0):
        self.l = l
        self.r = r
        self.val = val
        self.lazy = 0

class SegTree(object):
    
    def __init__(self, n, update_fn, query_fn, lazy_fn):
        self.tree = [None for _ in range(n << 2)]
        self.update_fn = update_fn
        self.query_fn = query_fn
        self.lazy_fn = lazy_fn
        self.merge_fn = merge_fn
        self.__make_tree(0, n-1, 0)
        
    def __make_tree(self, l, r, idx, inits=None):
        self.tree[idx] = Node(l, r)
        if l == r:
            self.tree[idx].val = inits[l] if inits else 0
        else:
            mid = l + (r-l >> 1)
            self.__make_tree(l, mid, (idx << 1) + 1, inits)
            self.__make_tree(mid+1, r, (idx << 1) + 2, inits)
            self.__push_up(idx)
    
    def __push_down(self, idx):
        left = (idx << 1) + 1
        right = left + 1
        self.tree[left].val = self.update_fn(self.tree[idx].lazy, self.tree[left].val)
        self.tree[right].val = self.update_fn(self.tree[idx].lazy, self.tree[right].val)
        self.tree[left].lazy = self.lazy_fn(self.tree[idx].lazy, self.tree[left].lazy)
        self.tree[right].lazy = self.lazy_fn(self.tree[idx].lazy, self.tree[right].lazy)
        self.tree[idx].lazy = 0
    
    def __push_up(self, idx):
        self.tree[idx].val = self.query_fn(self.tree[(idx<<1)+1].val, self.tree[(idx<<1)+2].val)
        
    def query(self, l, r, idx):
        if l <= self.tree[idx].l and r >= self.tree[idx].r:
            return self.tree[idx].val
        else:
            if self.tree[idx].lazy:
                self.__push_down(idx)
            mid = self.tree[idx].l + (self.tree[idx].r - self.tree[idx].l >> 1)
            if r <= mid:
                return self.query(l, r, (idx << 1) + 1)
            elif l > mid:
                return self.query(l, r, (idx << 1) + 2)
            else:
                return self.query_fn(self.query(l, r, (idx<<1)+1), self.query(l, r, (idx<<1)+2))
        
    def update(self, l, r, idx, val):
        if l <= self.tree[idx].l and r >= self.tree[idx].r:
            self.tree[idx].val = self.update_fn(val, self.tree[idx].val)
            self.tree[idx].lazy = self.update_fn(val, self.tree[idx].val)
        else:
            if self.tree[idx].lazy:
                self.__push_down(idx)
            
            mid = self.tree[idx].l + (self.tree[idx].r - self.tree[idx].l >> 1)
            if r <= mid:
                self.update(l, r, (idx<<1)+1, val)
            elif l > mid:
                self.update(l, r, (idx<<1)+2, val)
            else:
                self.update(l, r, (idx<<1)+1, val)
                self.update(l, r, (idx<<1)+2, val)
            self.__push_up(idx)
