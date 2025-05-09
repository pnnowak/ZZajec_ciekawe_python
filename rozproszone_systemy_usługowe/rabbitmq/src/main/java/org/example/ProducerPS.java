package org.example;

import com.rabbitmq.client.BuiltinExchangeType;
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;

public class ProducerPS {

    private final static String EXCHANGE_NAME = "krolik";

    public static void main(String[] args) throws Exception {
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");

        Connection connection = factory.newConnection();
        Channel channel = connection.createChannel();

        channel.exchangeDeclare(EXCHANGE_NAME, BuiltinExchangeType.FANOUT);

        for (int i = 1; i <= 16; i++) {
            String msg = "Wiadomość nr " + i;
            channel.basicPublish(EXCHANGE_NAME, "", null, msg.getBytes());
            System.out.println(" [x] Wysłano: '" + msg + "'");
        }
        channel.close();
        connection.close();
    }
}