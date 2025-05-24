package org.example.jaxws.client;

import org.example.jaxws.server_topdown.*;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.List;

public class PS2Client {
    public static void main(String[] args) throws MalformedURLException, PersonNotFoundEx_Exception, PersonExistsEx_Exception {
        // Adres serwisu zgodny z WSDL
        URL address = new URL("http://localhost:8082/personservice?wsdl");

        // Tworzymy obiekt serwisu i pobieramy proxy
        PersonService_Service service = new PersonService_Service(address);
        PersonService proxy = service.getPersonServiceImplPort();

        List<Person> all = proxy.getAllPersons();
        System.out.println("Lista wszystkich osób:");
        for (Person p : all) {
            System.out.println(" - " + p.getFirstName() + ", id: " + p.getId());
        }

//        System.out.println("Liczba osób: " + proxy.countPersons());

        try {
            proxy.addPerson(2, "Kacper", 22);
            System.out.println("Osoba dodana.");
        } catch (PersonExistsEx_Exception ex) {
            System.out.println("Osoba już istnieje: " + ex.getMessage());
        }

        try {
            proxy.addPerson(1, "Piotr", 22);
            System.out.println("Osoba dodana.");
        } catch (PersonExistsEx_Exception ex) {
            System.out.println("Osoba już istnieje: " + ex.getMessage());
        }

        try {
            boolean deleted = proxy.deletePerson(1);
            System.out.println("Usunięto osobę? " + deleted);
        } catch (PersonNotFoundEx_Exception ex) {
            System.out.println("Nie znaleziono osoby do usunięcia: " + ex.getMessage());
        }

        List<Person> all1 = proxy.getAllPersons();
        System.out.println("Lista wszystkich osób:");
        for (Person p : all1) {
            System.out.println(" - " + p.getFirstName() + ", id: " + p.getId());
        }
        try {
            Person p = proxy.getPerson(2);
            System.out.println("Pobrano osobę: " + p.getFirstName() + ", id: " + p.getId());
        } catch (PersonNotFoundEx_Exception ex) {
            System.out.println("Nie znaleziono osoby: " + ex.getMessage());

        }
    }
}