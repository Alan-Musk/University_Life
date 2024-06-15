package com.example;

import com.example.config.AppConfig;
import com.example.controller.MessageController;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Main {
    public static void main(String[] args) {
        ApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);
        MessageController controller = context.getBean(MessageController.class);
        controller.printMessage();
    }
}
