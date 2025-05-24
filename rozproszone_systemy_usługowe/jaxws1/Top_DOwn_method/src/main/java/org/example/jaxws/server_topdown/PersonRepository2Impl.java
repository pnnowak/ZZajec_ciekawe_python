package org.example.jaxws.server_topdown;

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

public class PersonRepository2Impl implements PersonRepository2 {

    private final Map<Integer, Person> database = new ConcurrentHashMap<>();

    @Override
    public Person addPerson(Person person) throws PersonExistsEx_Exception {
        if (database.containsKey(person.getId())) {
            throw new PersonExistsEx_Exception("Person with ID " + person.getId() + " already exists", new PersonExistsEx());
        }
        database.put(person.getId(), person);
        return person;
    }

    @Override
    public Person getPerson(int id) throws PersonNotFoundEx_Exception {
        Person p = database.get(id);
        if (p == null) {
            throw new PersonNotFoundEx_Exception("Person with ID " + id + " not found", new PersonNotFoundEx());
        }
        return p;
    }

    @Override
    public List<Person> getAllPersons() {
        return new ArrayList<>(database.values());
    }

    @Override
    public boolean deletePerson(int id) throws PersonNotFoundEx_Exception {
        if (!database.containsKey(id)) {
            throw new PersonNotFoundEx_Exception("Person with ID " + id + " not found", new PersonNotFoundEx());
        }
        database.remove(id);
        return true;
    }

    @Override
    public int countPersons() {
        return database.size();
    }
}

