package com.example.restservice.yourpackage;

public class Person {
    private int id;
    private String name;
    private int age;
    private PersonStatus status;

    public Person() {
        this.status = PersonStatus.ACTIVE;
    }

    public Person(int id, String name, int age) {
        this.id = id;
        this.name = name;
        this.age = age;
        this.status = PersonStatus.ACTIVE;
    }

    // Gettery i settery
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }

    public PersonStatus getStatus() { return status; }
    public void setStatus(PersonStatus status) { this.status = status; }
}


