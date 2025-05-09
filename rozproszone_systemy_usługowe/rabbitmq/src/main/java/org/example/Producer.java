package org.example;

import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;

public class Producer {

    private final static String QUEUE_NAME = "rabbbit-mq";

    public static void main(String[] args) throws Exception {
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");

        Connection connection = factory.newConnection();
        Channel channel = connection.createChannel();

        channel.queueDeclare(QUEUE_NAME, false, false, false, null);

        for (int i = 1; i <= 16; i++) {
            String msg = "Wiadomość nr " + i;
            channel.basicPublish("", QUEUE_NAME, null, msg.getBytes());
            System.out.println(" [x] Wysłano: '" + msg + "'");
            Thread.sleep(500); // 0,5 sekundy
        }
        channel.close();
        connection.close();
    }
}
