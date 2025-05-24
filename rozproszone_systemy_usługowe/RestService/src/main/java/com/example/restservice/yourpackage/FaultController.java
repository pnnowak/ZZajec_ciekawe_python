package com.example.restservice.yourpackage;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.ResponseStatus;

@ControllerAdvice
public class FaultController {

    @ResponseBody
    @ExceptionHandler(PersonNotFoundEx.class)
    @ResponseStatus(value = HttpStatus.NOT_FOUND)
    public String PNFEHandler(PersonNotFoundEx e) {
        return HttpStatus.NOT_FOUND + " - The person of ID=" + e.getMessage() + " DOES NOT EXIST";
    }

    @ResponseBody
    @ExceptionHandler(BadRequestEx.class)
    @ResponseStatus(value = HttpStatus.BAD_REQUEST)
    public String BREHandler(BadRequestEx e) {
        return HttpStatus.BAD_REQUEST + " - " + e.getMessage();
    }
    @ResponseBody
    @ExceptionHandler(ConflictEx.class)
    @ResponseStatus(HttpStatus.CONFLICT)
    public String conflictHandler(ConflictEx e) {
        return e.getMessage();
    }
}

