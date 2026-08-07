"""
Property Decorators: @property, setter, deleter
================================================

@property turns a method into a read-only attribute (computed on access). The
matching @x.setter and @x.deleter add write/delete behaviour. This lets you
expose a clean attribute API while keeping logic/validation behind it -- without
changing how callers access it.

Key idea:
    Start with a plain attribute; when you later need validation or a computed
    value, convert to a property -- callers keep using `obj.x`, nothing breaks.
"""


class Employee:
    def __init__(self, first: str, last: str) -> None:
        self.first = first
        self.last = last

    @property
    def email(self) -> str:
        # Computed on every access -- always consistent with first/last.
        return f"{self.first}.{self.last}@company.com"

    @property
    def fullname(self) -> str:
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name: str) -> None:
        # Lets `emp.fullname = "First Last"` update the backing fields.
        self.first, self.last = name.split(" ")

    @fullname.deleter
    def fullname(self) -> None:
        print("deleting name")
        self.first = None
        self.last = None


if __name__ == "__main__":
    emp = Employee("Subham", "Bhattacharya")
    print(emp.email)             # accessed like an attribute, not email()
    print(emp.fullname)          # Subham Bhattacharya

    emp.fullname = "Riya Sen"    # invokes the setter -> updates first/last
    print(emp.first)             # Riya
    print(emp.email)             # email recomputes -> Riya.Sen@company.com

    del emp.fullname             # invokes the deleter
    print(emp.first)             # None

    # Expected output:
    #   Subham.Bhattacharya@company.com
    #   Subham Bhattacharya
    #   Riya
    #   Riya.Sen@company.com
    #   deleting name
    #   None
