package org.example;

import com.rabbitmq.client.*;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.UUID;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.TimeoutException;


public class RPCClient implements AutoCloseable {

    private final static String RPC_QUEUE_NAME = "rabbbit-mq";
    private Connection connection;
    private Channel channel;

    public RPCClient() throws IOException, TimeoutException {
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");

        connection = factory.newConnection();
        channel = connection.createChannel();
    }

    public String call(String msg) throws Exception {
        String correlationID = UUID.randomUUID().toString();
        String replyQName = channel.queueDeclare().getQueue();


        AMQP.BasicProperties props = new AMQP.BasicProperties.Builder()
                .correlationId(correlationID)
                .replyTo(replyQName)
                .build();

        channel.basicPublish("", RPC_QUEUE_NAME, props, msg.getBytes(StandardCharsets.UTF_8));

        CompletableFuture<String> response = new CompletableFuture<>();

        String tag = channel.basicConsume(replyQName, true,
                (consumerTag, returnMsg) -> {
                    if (returnMsg.getProperties().getCorrelationId().equals(correlationID))
                        response.complete(new String(returnMsg.getBody(), "UTF-8"));
                },
                consumerTag -> {
                }
        );

        String result = response.get();
        channel.basicCancel(tag);
        return result;
    }

    public void close() throws Exception {
        channel.close();
        connection.close();
    }

    public static void main(String[] args) throws Exception {
        try (RPCClient client = new RPCClient()) {
            System.out.println("fib: " + client.call("fib 5"));
            System.out.println(client.call("sum 3 7"));
            System.out.println(client.call("sum 10 4"));
            System.out.println(client.call("fib 9"));
        }
    }
}


