package com.example.restservice.yourpackage;

import org.springframework.hateoas.EntityModel;
import org.springframework.hateoas.CollectionModel;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.stream.Collectors;

import static org.springframework.hateoas.server.mvc.WebMvcLinkBuilder.*;

@RestController
@CrossOrigin(origins = "*")
public class PersonController {

    private PersonRepository dataRepo = new PersonRepositoryImpl();
    @GetMapping("/persons")
    public List<Person> getAllPersons() {
        return dataRepo.getAllPersons();
    }
//    @GetMapping("/persons")
//    public CollectionModel<EntityModel<Person>> getAllPersons() {
//        List<EntityModel<Person>> persons = dataRepo.getAllPersons().stream()
//                .map(person -> EntityModel.of(person,
//                        linkTo(methodOn(PersonController.class).getPerson(person.getId())).withSelfRel(),
//                        linkTo(methodOn(PersonController.class).deletePerson(person.getId())).withRel("delete"),
//                        linkTo(methodOn(PersonController.class).getAllPersons()).withRel("list all")
//                ))
//                .collect(Collectors.toList());
//
//        return CollectionModel.of(persons,
//                linkTo(methodOn(PersonController.class).getAllPersons()).withSelfRel());
//    }

    @GetMapping("/persons/{id}")
    public EntityModel<Person> getPerson(@PathVariable int id) {
        Person thePerson = dataRepo.getPerson(id);
        EntityModel<Person> em = EntityModel.of(thePerson,
                linkTo(methodOn(PersonController.class).getPerson(id)).withSelfRel()
        );

        if (thePerson.getStatus() == PersonStatus.ACTIVE) {
            em.add(linkTo(methodOn(PersonController.class).deletePerson(id)).withRel("delete"));
            em.add(linkTo(methodOn(PersonController.class).hirePerson(id)).withRel("hire"));
        } else if (thePerson.getStatus() == PersonStatus.HIRED) {
            em.add(linkTo(methodOn(PersonController.class).vacatePerson(id)).withRel("vacate"));
        }

        em.add(linkTo(methodOn(PersonController.class).getAllPersons()).withRel("list all"));
        return em;
    }

    @PutMapping("/persons/{id}")
    public ResponseEntity<?> updatePerson(@PathVariable int id, @RequestBody Person person) {
        if (id != person.getId()) {
            return ResponseEntity.badRequest()
                    .body("ID in path (" + id + ") does not match ID in body (" + person.getId() + ")");
        }

        Person updatedPerson = dataRepo.updatePerson(person);
        return ResponseEntity.ok()
                .header(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE)
                .body(updatedPerson);
    }

    @DeleteMapping("/persons/{id}")
    public ResponseEntity<Void> deletePerson(@PathVariable int id) {
        dataRepo.deletePerson(id);
        return ResponseEntity.noContent().build();
    }
    @PatchMapping("/persons/{id}/hire")
    public EntityModel<Person> hirePerson(@PathVariable int id) {
        Person thePerson = dataRepo.getPerson(id);
        if (thePerson.getStatus() != PersonStatus.ACTIVE) {
            throw new ConflictEx("You CAN'T hire a person with status " + thePerson.getStatus());
        }
        thePerson.setStatus(PersonStatus.HIRED);

        return EntityModel.of(thePerson,
                linkTo(methodOn(PersonController.class).getPerson(id)).withSelfRel(),
                linkTo(methodOn(PersonController.class).vacatePerson(id)).withRel("vacate"),
                linkTo(methodOn(PersonController.class).getAllPersons()).withRel("list all")
        );
    }

    @PatchMapping("/persons/{id}/vacate")
    public EntityModel<Person> vacatePerson(@PathVariable int id) {
        Person thePerson = dataRepo.getPerson(id);
        thePerson.setStatus(PersonStatus.ACTIVE);

        return EntityModel.of(thePerson,
                linkTo(methodOn(PersonController.class).getPerson(id)).withSelfRel(),
                linkTo(methodOn(PersonController.class).deletePerson(id)).withRel("delete"),
                linkTo(methodOn(PersonController.class).hirePerson(id)).withRel("hire"),
                linkTo(methodOn(PersonController.class).getAllPersons()).withRel("list all")
        );
    }
//    @PostMapping("/persons/{id}")
//    public ResponseEntity<?> addPerson(@PathVariable int id, @RequestBody Person person) {
//        if (id != person.getId()) {
//            return ResponseEntity.badRequest()
//                    .body("ID in path (" + id + ") does not match ID in body (" + person.getId() + ")");
//        }
//
//        Person addedPerson = dataRepo.addPerson(person);
//        return ResponseEntity.status(HttpStatus.CREATED)
//                .header(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE)
//                .body(addedPerson);
//    }
    @PostMapping("/persons")
    public Person addPerson(@RequestBody Person person) {
        return dataRepo.addPerson(person);
    }



}




