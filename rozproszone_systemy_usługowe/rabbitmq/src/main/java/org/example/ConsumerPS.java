package org.example;

import com.rabbitmq.client.*;

import java.io.IOException;
import java.util.Scanner;

public class ConsumerPS {

    private final static String QUEUE_NAME = "rabbbit-mq";
    private final static String EXCHANGE_NAME = "krolik";

    public static void main(String[] args) throws Exception {
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");

        Connection connection = factory.newConnection();
        Channel channel = connection.createChannel();

        channel.exchangeDeclare(EXCHANGE_NAME, BuiltinExchangeType.FANOUT);
        String queueName = channel.queueDeclare().getQueue();
        channel.queueBind(queueName, EXCHANGE_NAME, "");

        System.out.println("Konsument czeka na wiadomości z kolejki: " + QUEUE_NAME);

        DefaultConsumer consumer = new DefaultConsumer(channel) {
            public void handleDelivery(String consumerTag,
                                       Envelope envelope,
                                       AMQP.BasicProperties properties,
                                       byte[] body) throws IOException {
                String msg = new String(body, "UTF-8");
                try {
                    Thread.sleep(600);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }

                System.out.println(" [x] Otrzymano: '" + msg + "'");
            }
        };

        channel.basicConsume(queueName, true, consumer);

        System.out.println("Naciśnij Enter, aby zakończyć...");
        new Scanner(System.in).nextLine();

        channel.close();
        connection.close();
        System.out.println("Połączenie zamknięte.");
    }
}
