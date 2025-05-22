import java.util.Scanner;

class Student{
    private String name;
    private int age;
    private String program;
    private int yearLevel;
    private String course;
    
    public Student(String name, int age, String program, int yearLevel, String course){
        this.name = name;
        this.age = age;
        this.program = program;
        this.yearLevel = yearLevel;
        this.course = course;
    }
    
    public String getName(){
        return name;
    }
    
    public int getAge(){
        return age;
    }
    
    public String getProgram(){
        return program;
    }
    
    public int getYearLevel(){
        return yearLevel;
    }
    
    public String getCourse(){
        return course;
    }
    
    public void displayStudInfo(){
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Program: " + program);
        System.out.println("Year Level: " + yearLevel);
        System.out.println("Course: " + course);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.print("Enter your age: ");
        int age = scanner.nextInt();
        scanner.nextLine();
        System.out.print("Enter your program: ");
        String program = scanner.nextLine();
        System.out.print("Enter your Year Level: ");
        int yearLevel = scanner.nextInt();
        scanner.nextLine();
        System.out.print("Enter your course: ");
        String course = scanner.nextLine();
        
        Student stud = new Student(name, age, program, yearLevel, course);
        
        stud.displayStudInfo();
    }
}
