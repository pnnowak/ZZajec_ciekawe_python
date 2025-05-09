package org.example;

import com.rabbitmq.client.BuiltinExchangeType;
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;

public class ProducerR {

    private final static String EXCHANGE_NAME = "krolik-ex";

    public static void main(String[] args) throws Exception {
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");

        Connection connection = factory.newConnection();
        Channel channel = connection.createChannel();

        channel.exchangeDeclare(EXCHANGE_NAME, BuiltinExchangeType.DIRECT);
        String[] keys = {"uwaga", "spokojnie", "czujnie"};

        for (int i = 1; i <= 16; i++) {
            String key = keys[i % keys.length];
            String msg = "[" + key.toUpperCase() + "]" + "Wiadomość nr " + i;
            channel.basicPublish(EXCHANGE_NAME, key, null, msg.getBytes());
            System.out.println(" [x] Wysłano: '" + msg + "' do klucza: " + key);
        }
        channel.close();
        connection.close();
    }
}
