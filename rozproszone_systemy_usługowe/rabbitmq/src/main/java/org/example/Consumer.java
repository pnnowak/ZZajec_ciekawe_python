package org.example;

import com.rabbitmq.client.*;

import java.io.IOException;
import java.util.Scanner;

public class Consumer {

    private final static String QUEUE_NAME = "rabbbit-mq";

    public static void main(String[] args) throws Exception {
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");

        Connection connection = factory.newConnection();
        Channel channel = connection.createChannel();

        channel.queueDeclare(QUEUE_NAME, false, false, false, null);
        System.out.println("Konsument czeka na wiadomości z kolejki: " + QUEUE_NAME);

        DefaultConsumer consumer = new DefaultConsumer(channel) {
            public void handleDelivery(String consumerTag,
                                       Envelope envelope,
                                       AMQP.BasicProperties properties,
                                       byte[] body) throws IOException {
                String msg = new String(body, "UTF-8");
                System.out.println(" [x] Otrzymano: '" + msg + "'");
            }
        };

        try {
            Thread.sleep(400);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        channel.basicConsume(QUEUE_NAME, true, consumer);

        System.out.println("Naciśnij Enter, aby zakończyć...");
        new Scanner(System.in).nextLine();

        channel.close();
        connection.close();
        System.out.println("Połączenie zamknięte.");
    }
}