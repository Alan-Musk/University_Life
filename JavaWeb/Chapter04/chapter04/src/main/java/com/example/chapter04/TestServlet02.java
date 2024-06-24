package com.example.chapter04;

import jakarta.servlet.*;
import jakarta.servlet.http.*;
import jakarta.servlet.annotation.*;

import java.io.IOException;

@WebServlet(name = "TestServlet02", value = "/TestServlet02")
public class TestServlet02 extends HttpServlet {
    @Override
    public void init() throws ServletException {
        System.out.println("init method is called");
    }

    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        System.out.println("service method is called");
    }

    @Override
    public void destroy() {
        System.out.println("destroy method is called");
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }
}
