package org.example.jaxws.server_topdown;

import jakarta.xml.ws.Endpoint;

public class ServiceHost2 {
    public static void main(String[] args) {
        String url = "http://localhost:8082/personservice";
        Endpoint.publish(url, new PersonService2Impl());
        System.out.println("✔ Serwis SOAP działa pod adresem: " + url + "?wsdl");
    }
}

