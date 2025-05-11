class Students {
    String name;
    int age;
    String program;
    int year;
    String course;
    
    void displayStudentInfo(){
        System.out.println("name: " + name + ", age " + age + ", program: " + program + ", year: " + year + ", course: " + course);
    }
}

class Main {
    public static void main(String[] args) {
        Students stud = new Students();
        stud.name = "Stanley";
        stud.age = 20;
        stud.program = "BSCS";
        stud.year = 1;
        stud.course = "OOP";
        stud.displayStudentInfo();
    }
}
