package com.example.chapter04;

import jakarta.servlet.*;
import jakarta.servlet.http.*;
import jakarta.servlet.annotation.*;

import java.io.IOException;
import java.io.PrintWriter;

@WebServlet(name = "RequestLineServlet", value = "/RequestLineServlet")
public class RequestLineServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();
        // 获取请求行信息
        out.println("getMethod()：" + request.getMethod() + "<br>");
        out.println("getRequestURI()：" + request.getRequestURI() + "<br>");
        out.println("getQueryString()：" + request.getQueryString() + "<br>");

    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doGet(request, response);
    }
}
