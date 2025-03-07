class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def calculate_avg(self):
        print(sum(self.mark)/len(self.mark))
    def get_grade(self):
         
         avg = sum(self.mark) / len(self.mark)
         if avg>=90:
             print(self.name,":GRade A")
         elif avg>=80 and avg<=89:
             print(self.name," :grade B")
         elif avg>=70 and avg<=79:
             print(self.name,":grade C")
         else:
             print(self.name,":grade D")

students = {
    "Alice": [85, 90, 88],
    "Bob": [78, 65, 72],
    "Charlie": [95, 92, 97]
}




