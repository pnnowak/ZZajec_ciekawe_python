package org.example.jaxws.server;
import jakarta.jws.WebMethod;
import jakarta.jws.WebParam;
import jakarta.jws.WebService;
import org.example.jaxws.server.PersonRepositoryImpl;

import java.util.List;

@WebService
public interface PersonService {

    @WebMethod
    List<Person> getAllPersons() throws EmptyListException;

    @WebMethod
    Person getPerson(@WebParam(name = "id") int id) throws PersonNotFoundEx;

    @WebMethod
    Person addPerson(
            @WebParam(name = "id") int id,
            @WebParam(name = "name") String name,
            @WebParam(name = "age") int age
    ) throws PersonExistsEx;

    @WebMethod
    boolean deletePerson(@WebParam(name = "id") int id) throws PersonNotFoundEx;

    @WebMethod
    int countPersons();

    @WebMethod
    Person updatePerson(int id, String newName, int newAge);

}
