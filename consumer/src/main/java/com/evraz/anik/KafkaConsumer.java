package com.evraz.anik;

import org.apache.kafka.clients.consumer.Consumer;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.common.TopicPartition;
import org.apache.kafka.common.serialization.LongDeserializer;
import org.apache.kafka.common.serialization.StringDeserializer;

import java.util.Arrays;
import java.util.List;
import java.util.Properties;

public class KafkaConsumer {

    public static void main(String[] args) {

        //String host="rc1a-b5e65f36lm3an1d5.mdb.yandexcloud.net:9091";
        String host = "rc1a-2ar1hqnl386tvq7k.mdb.yandexcloud.net:9091";
        String topic = "zsmk-9433-dev-01";
        String user = "9433_reader";
        String password = "eUIpgWu0PWTJaTrjhjQD3.hoyhntiK";
        String SASL_MECHANISM = "SCRAM-SHA-512";
        String SASL_SSL = "SASL_SSL";

        String server = host;//"localhost:9092";
        String topicName = topic; //"test.topic";
        String groupName = "cs"; //"test.group";

        final Properties props = new Properties();

        props.put(ConsumerConfig.GROUP_ID_CONFIG,
                groupName);
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG,
                server);
        props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG,
                LongDeserializer.class.getName());
        props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG,
                StringDeserializer.class.getName());

        props.setProperty("sasl.mechanism", "SCRAM-SHA-512");

        props.setProperty("security.protocol", "SASL_SSL");

        System.setProperty("java.security.auth.login.config", "src/main/resources/jaas.conf");
        System.setProperty("security.protocol", "SSL");
        System.setProperty("ssl.keystore.location", "src/main/resources/truststore.pem");
        //System.setProperty("ssl.keystore.","src/main/resources/truststore.pem");
        System.setProperty("ssl.truststore.type", "pem");
        //: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target

        //sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required username="USERNAME" password="PASSWORD";
        final Consumer<Long, String> consumer =
                new org.apache.kafka.clients.consumer.KafkaConsumer<>(props);


        TopicPartition tp = new TopicPartition(topicName, 0);
        List<TopicPartition> tps = Arrays.asList(tp);

        consumer.assign(tps);
        consumer.seekToBeginning(tps);

        ConsumerRecords<Long, String> consumerRecords = consumer.poll(30000);
        if (!consumerRecords.isEmpty()) {
            System.out.println("SUCCESS");
            System.out.println(consumerRecords.iterator().next().value());
        }

        consumer.close();
    }

}