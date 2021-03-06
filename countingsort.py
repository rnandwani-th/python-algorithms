import traceback


#CountingSort: takes as input a list of Student objects, and
#a character houseOrYear, which is 'h' if we are sorting the
#Students by house, or 'y' if sorting by year.
#Returns a list of Student objects, which is sorted by the
#appropriate attribute.
def CountingSort(studentList,houseOrYear):
    A = studentList
    if houseOrYear == 'h':
        B = [0] * len(A)        # Initialize output to 0 with length = input array
        C = [0] * 4             # Know that house ranges from 0-3 to set count array to length 4
        for j in range(0,len(A)):   # Add 1 to count of each occurence of each house
            C[A[j].getIndex("h")] += 1
        for i in range(1,4):    # Sum previous values in count array
            C[i] += C[i-1]
        for i in range(len(A)-1,-1,-1): # iterate down from right of array
            house = A[i].getIndex("h")  # get the house number
            B[C[house]-1] = A[i]    # set in appropriate position in output array
            C[house] -= 1       # decrement count in count array 
        return B
    if houseOrYear == 'y':
        B = [0] * len(A)
        C = [0] * 8
        for j in range(0,len(A)):
            C[A[j].year-1] += 1
        for i in range(1,8):
            C[i] = C[i] + C[i-1]
        for i in range(len(A)-1,-1,-1):
            year = A[i].getIndex("y")
            B[C[year]-1] = A[i]
            C[year] -= 1
        return B



#  DO NOT EDIT BELOW THIS LINE

#SortStudents function. Takes as input a list of Student objects,
#sorted alphabetically by name, and outputs a list of Student objects,
#sorted by the following priority: house, then year, then name.
def SortStudents(studentList):
    yearSorted = CountingSort(studentList,'y')
    houseSorted = CountingSort(yearSorted,'h')
    return houseSorted



#Student class
#Each task has three instance variables:
#   self.name is a string representing the name of the student
#   self.house is a string representing which house the student is in
#   self.year is an integer representing what year the student is
class Student:
    def __init__(self,csvstring):
        csvdata = csvstring.split(",")
        self.name = csvdata[0]
        self.house = csvdata[1]
        self.year = int(csvdata[2])
    def __repr__(self):
        return "\n"+self.name + ": " + self.house + " " + str(self.year)
    def __eq__(self,other):
        return type(self) == type(other) and \
               self.name == other.name and \
               self.house == other.house and \
               self.year == other.year
    #A helpful method for dealing with Counting Sort.
    #Maps the houses onto integers from 0-3, and
    #years to integers from 0-7.
    def getIndex(self,houseOrYear):
        if houseOrYear == 'h':
            if self.house == 'Eagletalon':
                return 0
            elif self.house == 'Lannister':
                return 1
            elif self.house == 'Pufflehuff':
                return 2
            else:
                return 3
        else:
            return self.year-1

#Takes a string filename as an argument, and constructs a list
#  of Students from the information in the CSV file at filename
def getStudentList(filename):
    fp = open(filename)
    fp.readline()
    studentList = []
    for line in fp:
        studentList.append(Student(line))
    return studentList


tests = ['roster0.csv','roster1.csv','roster2.csv','roster3.csv']
correct = ['roster0sorted.csv','roster1sorted.csv',
           'roster2sorted.csv','roster3sorted.csv']


#Run test cases, check whether sorted list correct
count = 0

try:
    for i in range(len(tests)):
        ("\n---------------------------------------\n")
        print("TEST #",i+1)
        print("Reading student data from:",tests[i])
        roster = getStudentList(tests[i])
        print("Reading sorted student data from",correct[i])
        rosterSorted = getStudentList(correct[i])
        print("Running: SortStudents() on data list\n")
        output = SortStudents(roster)
        if i == 0:
            print("Expected:",rosterSorted,"\n\nGot:",output)
        assert len(output) == len(rosterSorted), "Output list length "\
               +str(len(output))+\
                  ", but should be "+str(len(rosterSorted))
        for j in range(len(output)):
            assert output[j] == rosterSorted[j],"Student #"\
                       +str(j+1)+" incorrect: "+\
                    str(output[j])+" \nshould be "+str(rosterSorted[i])
        print("Test Passed!\n")
        count += 1
except AssertionError as e:
    print("\nFAIL: ",e)

except Exception:
    print("\nFAIL: ",traceback.format_exc())

cursed = False
with open(__file__) as f:
    source = f.read()
    for ch in source:
        if ord(ch) == 60:
            print("Less than sign detected: Curse activated!")
            count = 0
            cursed = True
        if ord(ch) == 62:
            print("Greater than sign detected: Curse activated!")
            count = 0
            cursed = True

print()
if cursed:
    print("You are now a newt.  Don't worry, you'll get better.")
print(count,"out of",len(tests),"tests passed.")
