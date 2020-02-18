import math

__all__ = ["Sheet"]

class Sheet:
    page = {}
    pageNo = 1
    def __init__(self, date, week, txt, tag = ''):
        itemPage1 = [date, week, txt, tag]
        self.page[0] = [itemPage1]
        
    def add(self,item,page=-1):
        item.extend([''])
        if len(self.page)+1 > page:
            self.page[self.pageNo] = self.page.get(self.pageNo-1).extend([item])
        else:
            page = len(self.page)
            self.page[page-1] = [self]
        self.pageNo += 1
    def replce(self, pageno=0, keyword=[]):
        finder = self.page.get(pageno)
        if keyword in finder:
            for text in finder:
                if keyword  == text:
                    while True:
                        reItem1 = input('what do you want to replace with')
                        reItem2 = reItem1.split(',',-1)
                        if len(reItem2) == 4:
                            break
                    finder.remove(text)
                    finder.insert(-1,reItem2)
                    break

    #def edit(self, no, **kwargs):
    #   self.__dict__.update(kwargs)
    #  self.replace(no)
    def delet(self,pagen=0,keyword=[]):
        finder = self.page.get(pagen)
        if keyword in finder:
            for text in finder:
                if keyword  == text:
                    finder.remove(text)
                    break

    
if __name__=='__main__':
    notBook = Sheet(2020, 3, 'i am sad')
    notBook.add(['2031/4/3',3,'lol'])
    notBook.delet(0,[2020, 3, 'i am sad',''])
    notBook.replce(0,['2031/4/3',3,'lol',''])
    for x,y in Sheet.page.items():
        print(f'page{x+1}')
        if y != None:
            for z in y:
                print(z)
        else:
            print('empty')
