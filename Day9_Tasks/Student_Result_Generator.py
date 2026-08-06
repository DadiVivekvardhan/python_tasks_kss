#7. Student Result Generator (Method Overloading Concept) A school system calculates student results differently depending on available data.
#Create a Result class where a method can calculate the result using either two subjects or three subjects.


class Result:

    def calculate(self, *marks):

        if len(marks) == 2:
            total = marks[0] + marks[1]
            print("Total Marks :", total)

        elif len(marks) == 3:
            total = marks[0] + marks[1] + marks[2]
            print("Total Marks :", total)


r = Result()

r.calculate(80, 90)
r.calculate(80, 90, 85)
