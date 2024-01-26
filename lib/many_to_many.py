class Author:
    all = []
    def __init__(self, name):
        self._name = name
        Author.all.append(self)
            
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else: 
            raise Exception("Name should be a string.")

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    def books(self):
        books = []
        for contract in self.contracts():
           books.append(contract.book)
        return books  
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract
    def total_royalties(self):
        total_amount_of_royalties = 0
        for contract in self.contracts():
            total_amount_of_royalties += contract.royalties
        return total_amount_of_royalties    




class Book:
    all=[]
    def __init__(self, title):
        self._title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if type(title) == str:
            self.title = title
        else:
            raise Exception("Title should be a string.") 

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self] 

    def authors(self):
        authors = []
        for contract in self.contracts():
            authors.append(contract.author)
        return authors    



class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        self._royalties = royalties
        self._date = date
        if type(author) == Author:
            self.author = author
        else: 
            raise Exception("Author should be a type of Author.")
        if type(book) == Book:
            self.book = book 
        else: 
            raise Exception("Book should be a type of Book.")
        if type(date) == str:
            self.date = date
        else:
            raise Exception("Type of date should be a string.")
        if type(royalties) == int:
            self.royalties = royalties
        else:
            raise Exception("Type of royalties should be a integer. ") 
        Contract.all.append(self)    

    @classmethod    
    def contracts_by_date(cls, date):
        same_day_contracts = []
        for contract in cls.all:
            if contract.date == date:
                same_day_contracts.append(contract)
        return same_day_contracts        
