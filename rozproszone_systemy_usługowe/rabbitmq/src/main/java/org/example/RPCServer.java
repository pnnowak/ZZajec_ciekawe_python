package org.example;

import com.rabbitmq.client.*;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.TimeoutException;

public class RPCServer {

    private final static String RPC_QUEUE_NAME = "rabbbit-mq";
    ;

    public static void main(String[] argv) throws IOException, TimeoutException {
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        Connection connection = factory.newConnection();
        Channel channel = connection.createChannel();

        channel.queueDeclare(RPC_QUEUE_NAME, false, false, false, null);

        channel.basicQos(1);

        System.out.println(" [x] Serwer RPC oczekuje...");

        channel.basicConsume(RPC_QUEUE_NAME, false, new DefaultConsumer(channel) {
            @Override
            public void handleDelivery(String consumerTag,
                                       Envelope envelope,
                                       AMQP.BasicProperties properties,
                                       byte[] body) throws IOException {

                String response = "";

                try {
                    String msg = new String(body, "UTF-8");
                    String[] p = msg.split(" ");
                    String cmd = p[0];

                    if (cmd.equals("fib")) {
                        int n = Integer.parseInt(p[1]);
                        response = "" + fib(n);
                    } else if (cmd.equals("sum")) {
                        int a = Integer.parseInt(p[1]);
                        int b = Integer.parseInt(p[2]);
                        response = "" + (a + b);
                    } else {
                        response = "Nieznane";
                    }
                }
                catch (RuntimeException e) {
                    System.out.println(" [!] Błąd: " + e.getMessage());
                } finally {
                    channel.basicPublish("",
                            properties.getReplyTo(),
                            properties,
                            response.getBytes("UTF-8"));

                    channel.basicAck(envelope.getDeliveryTag(), false);
                }
            }
        });
    }

    // Funkcja obliczeniowa (przykład: ciąg Fibonacciego)
    private static int fib(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;
        return fib(n - 1) + fib(n - 2);
    }

    private static int sum(int a, int b) {
        return a + b;
    }
}

