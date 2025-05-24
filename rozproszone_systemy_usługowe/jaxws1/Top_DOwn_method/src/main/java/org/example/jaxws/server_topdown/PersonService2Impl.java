package org.example.jaxws.server_topdown;

import jakarta.jws.WebService;

@WebService(
        serviceName = "PersonService",
        portName = "PersonServiceImplPort",
        targetNamespace = "http://server.jaxws.example.org/",
        endpointInterface = "org.example.jaxws.server_topdown.PersonService"
)
public class PersonService2Impl implements PersonService {

    private final PersonRepository2 repository = new PersonRepository2Impl();

    @Override
    public Person addPerson(int id, String name, int age) throws PersonExistsEx_Exception {
        Person p = new Person();
        p.setId(id);
        p.setFirstName(name);
        p.setAge(age);
        return repository.addPerson(p);
    }

    @Override
    public Person getPerson(int id) throws PersonNotFoundEx_Exception {
        return repository.getPerson(id);
    }

    @Override
    public java.util.List<Person> getAllPersons() {
        return repository.getAllPersons();
    }

    @Override
    public boolean deletePerson(int id) throws PersonNotFoundEx_Exception {
        return repository.deletePerson(id);
    }

    @Override
    public int countPersons() {
        return repository.countPersons();
    }
}
