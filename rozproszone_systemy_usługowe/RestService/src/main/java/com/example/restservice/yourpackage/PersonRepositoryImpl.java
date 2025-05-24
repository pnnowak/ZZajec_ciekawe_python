package com.example.restservice.yourpackage;

import java.util.ArrayList;
import java.util.List;

public class PersonRepositoryImpl implements PersonRepository {

    private List<Person> personList = new ArrayList<>();

    public PersonRepositoryImpl() {
        personList.add(new Person(1, "John Doe", 30));
        personList.add(new Person(2, "Jane Smith", 25));
    }

    @Override
    public List<Person> getAllPersons() {
        return personList;
    }

    @Override
    public Person getPerson(int id) {
        return personList.stream()
                .filter(p -> p.getId() == id)
                .findFirst()
                .orElseThrow(() -> new PersonNotFoundEx(id));
    }

    @Override
    public Person updatePerson(Person person) {
        Person existing = getPerson(person.getId());
        existing.setName(person.getName());
        existing.setAge(person.getAge());
        return existing;
    }

    @Override
    public boolean deletePerson(int id) {
        Person existing = getPerson(id);
        return personList.remove(existing);
    }

    @Override
    public Person addPerson(Person person) {
        if (personList.stream().anyMatch(p -> p.getId() == person.getId())) {
            throw new BadRequestEx("Person with id " + person.getId() + " already exists.");
        }
        personList.add(person);
        return person;
    }
}
