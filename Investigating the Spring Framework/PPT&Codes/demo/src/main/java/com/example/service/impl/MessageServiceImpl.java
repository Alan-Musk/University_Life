package com.example.service.impl;

import com.example.service.MessageService;
import org.springframework.stereotype.Service;

@Service
public class MessageServiceImpl implements MessageService {
    @Override
    public String getMessage() {
        return "Hello, Spring IoC!";
    }
}
