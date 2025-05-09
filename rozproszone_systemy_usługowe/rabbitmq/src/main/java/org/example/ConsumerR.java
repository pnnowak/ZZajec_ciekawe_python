package org.example;

import com.rabbitmq.client.*;

import java.io.IOException;
import java.util.Scanner;

public class ConsumerR {

    private final static String EXCHANGE_NAME = "krolik-ex";

    public static void main(String[] args) throws Exception {
        if (args.length < 1) {
            System.err.println("Podaj co najmniej jeden routing key (np. info alert)");
            System.exit(1);
        }

        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");

        Connection connection = factory.newConnection();
        Channel channel = connection.createChannel();

        channel.exchangeDeclare(EXCHANGE_NAME, BuiltinExchangeType.DIRECT);

        String queueName = channel.queueDeclare().getQueue();

        for (String routingKey : args) {
            channel.queueBind(queueName, EXCHANGE_NAME, routingKey);
        }

        System.out.println(" [*] Konsument czeka na wiadomości (klucze: " + String.join(", ", args) + ")");

        DefaultConsumer consumer = new DefaultConsumer(channel) {
            public void handleDelivery(String consumerTag,
                                       Envelope envelope,
                                       AMQP.BasicProperties properties,
                                       byte[] body) throws IOException {
                String msg = new String(body, "UTF-8");
                System.out.println(" [x] Otrzymano (key = " + envelope.getRoutingKey() + "): '" + msg + "'");
            }
        };

        channel.basicConsume(queueName, true, consumer);

        System.out.println("Naciśnij Enter, aby zakończyć...");
        new Scanner(System.in).nextLine();

        channel.close();
        connection.close();
    }
}
