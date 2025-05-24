package org.example.jaxws.server;
import jakarta.jws.WebMethod;
import jakarta.jws.WebService;
import java.util.List;

@WebService(serviceName = "PersonService",
        endpointInterface = "org.example.jaxws.server.PersonService")
public class PersonServiceImpl implements PersonService {

    private PersonRepository dataRepository = new PersonRepositoryImpl();

    @Override
    @WebMethod
    public List<Person> getAllPersons() {
        System.out.println("...called getAllPersons");
        return dataRepository.getAllPersons();
    }

    @Override
    @WebMethod
    public Person getPerson(int id) throws PersonNotFoundEx {
        System.out.println("...called getPerson");
        return dataRepository.getPerson(id);
    }

    @Override
    @WebMethod
    public Person addPerson(int id, String name, int age) throws PersonExistsEx {
        System.out.println("...called addPerson");
        return dataRepository.addPerson(id, name, age);
    }

    @Override
    @WebMethod
    public boolean deletePerson(int id) throws PersonNotFoundEx {
        System.out.println("...called deletePerson");
        return dataRepository.deletePerson(id);
    }

    @Override
    @WebMethod
    public int countPersons() {
        System.out.println("...called countPersons");
        return dataRepository.countPersons();
    }
    @Override
    public Person updatePerson(int id, String newName, int newAge) {
        return dataRepository.update(id, newName, newAge);
    }

}