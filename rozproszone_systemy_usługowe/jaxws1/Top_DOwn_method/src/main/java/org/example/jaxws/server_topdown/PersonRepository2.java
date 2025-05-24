package org.example.jaxws.server_topdown;

import java.util.List;

public interface PersonRepository2 {
    Person addPerson(Person person) throws PersonExistsEx_Exception;
    Person getPerson(int id) throws PersonNotFoundEx_Exception;
    List<Person> getAllPersons();
    boolean deletePerson(int id) throws PersonNotFoundEx_Exception;
    int countPersons();
}

